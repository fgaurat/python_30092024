import requests  
from bs4 import BeautifulSoup
from pprint import pprint
def main():
    # sauvegarde des dépendances
    # pip freeze > requirements.txt
    
    # installation des dépendances
    # pip install -r requirements.txt
    
    url = r"https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    # log_files = []    
    # for a in all_a:
    #     if ".log" in a['href']: 
    #         log_files.append(a['href'])

    log_files = [a['href'] for a in all_a if ".log" in a['href']]    

    for log_file in log_files:
        full_url = url+log_file
        response = requests.get(full_url)
        with open(log_file,'w') as f:
            f.write(response.text)




if __name__=='__main__':
    main()
