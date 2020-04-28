#By Zippyzzzzzzz
#Use Python,requests,Beautifulsoup,Sendline
from bs4 import BeautifulSoup as soup 
import requests

userct = str(input('Please input country : '))
def Covid19(usercountry):
    try:
        url = requests.get('https://epidemic-stats.com/coronavirus/' + str(usercountry)) #Url Website

        page_html = url.content

        data = soup(page_html,'html.parser')
        Infected = data.find_all('span')
        Recovered = data.find_all('span',{'class':'h5 card-title'})
        Deaths = data.find_all('span',{'class':'h5 card-title'})
        Updated = data.find_all('p',{'class':'text-center mt-4 lead'})
        percent = data.find_all('span',{'class':'small text-opacity'})
        percentv2 = data.find_all('span',{'class':'small text-opacity'})

        percent = percent[0].text
        percentv2 = percentv2[1].text
        Infected = Infected[1].text
        Recovered = Recovered[2].text.replace(percentv2,'')
        Deaths = Deaths[1].text.replace(percent,'')
        Updated = Updated[0].text
        

        print(' Country: {} \n\n Infected: {} \n\n Recovered: {} Deaths: {} {}'.format(userct,Infected,Recovered,Deaths,Updated))
        text = ' Country: {} \n\n Infected: {}\n\n Recovered: {} Deaths: {} {}'.format(userct,Infected,Recovered,Deaths,Updated)
        return text
    except:
        print('No Result')
        return 'No Result'

#SendLine 
from songline import Sendline as line
token = 'w783ZlSDPnBg866WuXawIAIIhTknvhMiss5kFeOuoxx' #input line token
messenger = line(token)
ct = Covid19(userct)
messenger.sendtext(ct)
