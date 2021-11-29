from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time


class Crawler:
    """
    NOME:
        Crawler

    DESCRIÇÃO:
        Módulo Crawler
        =============================
        Este módulo realiza o acesso ao site
        "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
        para coleta de dados da página.

    MÉTODOS
        Construtor: Instancia o crawler, indicando a página de acesso
        searching_notebooks: Faz a busca de todos os notebooks anúnciados
    """
    def __init__(self) -> None:
        self.URL = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        
        service = Service('chromedriver.exe')

        self.chrome = webdriver.Chrome(options=options)

    def searching_notebooks(self) -> dict:
        """
            Faz a busca de todos os dados de todos os notebooks.
            Arguments:

            Returns
                :yeld dict: Um dicionário com os dados recolhidos de cada produto em anúncio.
        """
        self.chrome.get(self.URL)

        thumbnails = self.chrome.find_elements(By.CLASS_NAME, 'thumbnail')
        urls = [(thumbnail.find_element(By.CLASS_NAME, 'title').get_attribute('href')) for thumbnail in thumbnails]        

        for url in urls:
            self.chrome.get(url)
            time.sleep(2)
            self.chrome.find_element_by_id('closeCookieBanner').click()
            img = self.chrome.find_element(By.CLASS_NAME, 'img-responsive').get_attribute('src')
            
            h4 = self.chrome.find_element(By.CLASS_NAME, 'caption').find_elements(By.TAG_NAME, 'h4')
            try:
                price = float(h4[0].text.replace('$', ''))
            except:
                price = h4[0].text.replace('$', '')
            
            title = h4[1].text.lower()
            description = self.chrome.find_element(By.CLASS_NAME, 'description').text
            reviews = self.chrome.find_element(By.CLASS_NAME, 'ratings').find_element(By.TAG_NAME, 'p').text.replace(' reviews', '')
            stars = len(self.chrome.find_elements(By.CLASS_NAME, 'glyphicon-star'))
            hds = self.chrome.find_elements_by_class_name('swatch')
            prices = {}
            for hd in hds:
                if 'disabled' not in hd.get_attribute('class'):
                    hd.click()
                    prices[hd.text] = self.chrome.find_element(By.CLASS_NAME, 'price').text

            yield {'img': img,
                   'price': price,
                   'prices': prices,
                   'title': title,
                   'description': description,
                   'reviews': reviews,
                   'stars': stars}
