from lxml import html
import requests
import constants

MAX_PAGES = 68


def get_search_result_url(page):
    return constants.IMOBILIARE_RO['SEARCH_RESULTS_URL'].format(page)


def crawl():
    apartments = []
    for page in range(1, MAX_PAGES):
        search_results_url = get_search_result_url(page)
        results = get_apartments_from_search_results(search_results_url)
        apartments.extend(results)

    print("Number of apartments:", len(apartments))


def get_apartments_from_search_results(url):

    print("Parsing: ", url)
    response = requests.get(url)
    tree = html.fromstring(response.content)
    post_links = tree.xpath(constants.IMOBILIARE_RO['XPATH_APARTMENT_ANCHORS'])

    apartments = []
    for link in post_links:
        apartment = {'title': link.attrib['title'], 'link': link.attrib['href']}
        apartments.append(apartment)

    return apartments


if __name__ == "__main__":
    crawl()
