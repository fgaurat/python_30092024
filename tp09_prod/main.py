import requests  

def main():
    url = r"https://logs.eolem.com/"
    response = requests.get(url)
    print(response.text)

if __name__=='__main__':
    main()
