from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

opts = Options()
opts.add_argument("user-agent=Googlebot/2.1(+http://www.googlebot.com/bot.html)")

ticker_list = ["AMZN","BDK","BA","CAT","CHTR","CMCSA","COST","DHR","EK","EBAY","F","GD","GM","HON",
               "JCI","LB","LMT","LOW","MCD","RTN","ROK","SPG","SBUX","TGT","DIS","TWX","FOXA","FOX",
               "WMT","WY","MO","BUD","AVP","BKNG","CPB","CBS","CL","HNZ","HSH","HD","KHC","MDLZ","NKE",
               "PEP","PM","KO","APC","APA","BHI","CVX","COP","DVN","DUK","EP","EMR","XOM","GE","HAL","NOV",
               "SLB","AIG","ALL","AXP","BAC","BRK.B","BLK","BK","COF","C","GS","HIG","JPM","LEH","MA","MER",
               "MET","MS","NYX","PYPL","V","WB","WFC","RF","USB","SGP","UNH","WBA","WYE","MMM","ABT",
               "AGN","AMGN","BAX","BIIB","BMY","CELG","CI","COV","CVS","LLY","GILD","JNJ","MDT","MRK","PFE",
               "PG","NSC","AES","BNI","DWDP","DD","FDX","FCX","MON","NSM","UNP","UPS","IP","ACN",
               "GOOG","AAPL","CSCO","CSC","DELL","EMC","FB","HPQ","IBM","MSFT","ORCL","QCOM","TXN","INTC",
               "XRX","AA","ATI","VZ","AEP","T","ETR","EXC","KMI","NEE","SO","S","WMB"]
print("Number of equities: ",len(ticker_list))

for ticker in ticker_list:
    print(ticker)
    url = "https://www.stocksplithistory.com/?symbol="+ticker
    driver = webdriver.Chrome(chrome_options=opts,executable_path="F:\PythonApps\ChromeDriver\chromedriver.exe")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.quit()

    split_rows = soup.find('table', attrs={'border': '0', 'width': '208', 'style':'font-family: Arial; font-size: 12px'}).find_all("tr")

    output_filename = "F:\System\PVWAVE\Scraped_Data\EquitySplits\%s.csv"%ticker
    output_file = open(output_filename,'w',newline='')
                            
    for row in split_rows:
        columns= list(row.stripped_strings)
        if len(columns) != 2:
            continue
        output_file.write("{}, {} \n".format(columns[0],columns[1]))
    
    output_file.close()   

