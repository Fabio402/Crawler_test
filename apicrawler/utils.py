from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service


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
        options.add_argument('--headless')
        
        #service = Service('../chromedriver.exe')

        self.chrome = webdriver.Chrome(chrome_options=options)

    def searching_notebooks(self) -> dict:
        """
            Faz a busca de todos os dados de todos os notebooks.
            Arguments:

            Returns
                :yeld dict: Um dicionário com os dados recolhidos de cada produto em anúncio.
        """
        self.chrome.get(self.URL)

        thumbnails = self.chrome.find_elements(By.CLASS_NAME, 'thumbnail')
        for thumbnail in thumbnails:
            img = thumbnail.find_element(By.CLASS_NAME, 'img-responsive').get_attribute('src')
            price = thumbnail.find_element(By.CLASS_NAME, 'price').text
            title = thumbnail.find_element(By.CLASS_NAME, 'title').text.lower()
            description = thumbnail.find_element(By.CLASS_NAME, 'description').text
            reviews = thumbnail.find_element(By.CLASS_NAME, 'ratings').find_element(By.CLASS_NAME, 'pull-right').text.replace(' reviews', '')
            stars = thumbnail.find_element(By.CLASS_NAME, 'ratings').find_element(By.XPATH, 'p[@data-rating]').get_attribute('data-rating')
            yield {'img': img,
                   'price': price,
                   'title': title,
                   'description': description,
                   'reviews': reviews,
                   'stars': stars}
