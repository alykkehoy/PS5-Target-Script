import time
import datetime
import winsound
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# URL = 'https://www.target.com/p/sackboy-a-big-adventure-playstation-5/-/A-81255581'
URL = 'https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab'
wd = webdriver.Chrome(ChromeDriverManager().install())
wd.get(URL)

def main():
    while True:
        loaded = False
        while not loaded:
            try:
                wd.find_element_by_css_selector('[data-test="preorderButton"]').click()
                winsound.Beep(700, 1500)
                print('*************************************')
                print(datetime.datetime.now().strftime("[%m-%d-%Y %H:%M:%S]") + ' Available')
                print('*************************************')
                loaded = True

            except:
                try:
                    wd.find_element_by_css_selector('[data-test="preorderUnsellable"]')
                    print(datetime.datetime.now().strftime("[%m-%d-%Y %H:%M:%S]") + ' Unavailable')
                    loaded = True
                except:
                    pass

        wd.refresh()
                

if __name__ == '__main__':
    main()


