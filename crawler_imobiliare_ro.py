from lxml import html
import requests

SEARCH_URL = "https://www.imobiliare.ro/vanzare-apartamente/timisoara?pagina={}"

MAX_PAGES = 68


def crawl():
    apartments = []
    for page in range(1, MAX_PAGES):
        apartments.extend(get_apartments_from_search_results(page))

    print("Number of apartments:", len(apartments))
    for ap in apartments:
        print(ap['title'])


def get_apartments_from_search_results(page):
    apartments = []
    url = SEARCH_URL.format(page)
    print("Parsing",page, url)
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # results = tree.xpath("//div[@id='container-lista-rezultate']")
    # posts = tree.xpath("//div[@class='box-anunt']//")
    post_links = tree.xpath("//h2[@class='titlu-anunt']/a")

    for link in post_links:
        apartment = {}
        apartment['title'] = link.attrib['title']
        apartment['link'] = link.attrib['href']
        apartments.append(apartment)

    print("Found ",len(apartments))
    return apartments


crawl()
