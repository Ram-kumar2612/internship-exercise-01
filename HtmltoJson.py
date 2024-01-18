from bs4 import BeautifulSoup
import json
HtmlPath = 'index.html'
JsonPath = 'result.json'
with open(HtmlPath, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content,'html.parser')
        CapitalData = soup.find_all('strong',attrs = {'class' : 'capital' })
        StateData = soup.find_all('span',attrs = {'class' : 'state' })
        CapitalList = []
        StateList = []
        for s in StateData:
            StateList.extend(s.contents)
        for c in CapitalData:
            CapitalList.extend(c.contents)
        JsonString={}
        temp={}
        JsonString['capitals'] = []
        count = 0
        i = 0
        while i < len(a):
                temp["capital"] = a[i]
                temp["state"] = b[i]
                count += 1
                JsonString['capitals'].append(temp)
                temp = {}
                i += 1
        JsonString['summary'] = {"Number of Capitals " : count}
        with open(JsonPath,'w', encoding='utf-8') as f:
            json.dump(d,f,indent=3)
            f.close()
        file.close()
