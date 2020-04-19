import requests 
from bs4 import BeautifulSoup 
import csv 
import time
import schedule

def remind():
    newLine = """
    """ 

    URL1 = "https://www.codechef.com/contests"
    r1 = requests.get(URL1) 

    soup1 = BeautifulSoup(r1.content, 'html5lib') 

    quotes1=[] # a list to store quotes 

    table1 = soup1.findAll('table', attrs = {'class':'dataTable'}) 
    #print(table1[1])
    contests1 = table1[1].findAll('td')
    #print(len(contests1))

    i = 0
    quote1 = {}
    for row in contests1:
            if(i%4 == 1):
                quote1['name'] = row.text.strip()
            if(i%4 == 2):
                quote1['start'] = row.text.strip()
            if(i%4 == 3):
                quote1['end'] = row.text.strip()
            if(i%4 == 3):
                quotes1.append(quote1)
                quote1 = {} 
            i += 1;

    #print(str(quotes1))


    bot_message1 = """*Codechef Contests*
    """ + newLine


    for entry in quotes1:
        bot_message1 += '*' + str(entry['name']) + '*' + newLine
        bot_message1 += '   Start: ' + str(entry['start']) + newLine
        bot_message1 += '   End: ' + str(entry['end']) + newLine
        bot_message1 += newLine





    URL2 = "https://www.codeforces.com/contests"
    r2 = requests.get(URL2) 

    soup2 = BeautifulSoup(r2.content, 'html5lib') 

    quotes2=[] # a list to store quotes 

    table2 = soup2.findAll('tbody')

    #print(table2[0])

    contests2 = table2[0].findAll('tr')  #.findAll('td')
    # print(contests2)
    # print(len(contests2)) # 0 2 3

    quotes2 = []
    quote2 = {}
    j = 0
    f = False

    for tr in contests2:
        j = 0
        quote2 = {}
        if(f):
            for row in tr.findAll('td'):
                    if(j%6 == 0):
                        quote2['name'] = row.text.strip().replace('#', "") 
                    if(j%6 == 2):
                        quote2['start'] = row.text.strip().replace('#', "") 
                    if(j%6 == 3):
                        quote2['len'] = row.text.strip().replace('#', "") 
                    if(j%6 == 3):
                        quotes2.append(quote2)
                        quote2 = {} 
                    j += 1;
        else:
            f = True

    # print(quotes2)

    bot_message2 = """*Codeforces Contests*
    """ + newLine 


    for entry in quotes2:
        bot_message2 += '*' + str(entry['name']) + '*' + newLine
        bot_message2 += '   Start: ' + str(entry['start']) + newLine
        bot_message2 += '   Length: ' + str(entry['len']) + newLine
        bot_message2 += newLine

    # print(bot_message2)

    bot_token = '1198731488:AAHK3JI7Ltv9gkt3dSUzNujywVl7j5_VZDA'
    bot_chatID = '-1001474350565'

    send_text1 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message1
    response1 = requests.get(send_text1)
    print(response1)

    send_text2 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message2
    response2 = requests.get(send_text2)
    print(response2)


schedule.every(1).minutes.do(remind)

while True:
    schedule.run_pending()
    time.sleep(1)