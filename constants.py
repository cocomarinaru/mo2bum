class ImobiliareRo:
    SEARCH_RESULTS_URL = "https://www.imobiliare.ro/vanzare-apartamente/timisoara?pagina={}"
    XPATH_APARTMENT_ANCHORS = "//h2[@class='titlu-anunt']/a"

    class HousePage:
        PAGE_HEADER = "//div[@class='title-head-container']"
        PAGE_TITLE = PAGE_HEADER + "//div[@class='titlu']/h1"
        HOUSE_AREA = PAGE_HEADER + "//div[@class='header_info']/div/div[1]"
        ENTRY_ADDED_DATE = PAGE_HEADER + "//div[@class='header_info']//span[@class='data-actualizare']"
        PRICE = PAGE_HEADER + "//div[@class='preturi clearfix']/div[@class='pret first blue']"
        # House details
        HOUSE_DETAILS = "//div[@id='b_detalii_text']"
        # House caracteristics
        HOUSE_CARACTERISTICS = "//div[@id='b_detalii_caracteristici']"
        NUMBER_OF_ROOMS = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Nr. camere:')]/span"
        HOUSE_MP = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Suprafaţă utilă:')]/span"
        BUILD_MP = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Suprafaţă construită:')]/span"
        HOUSE_DIVISION = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Compartimentare:')]/span"
        HOUSE_COMFORT = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Confort:')]/span"
        HOUSE_FLOOR = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Etaj:')]/span"
        NUMBER_OF_KITCHENS = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Nr. bucătării:')]/span"
        NUMBER_OF_BATHROOMS = HOUSE_CARACTERISTICS +  "//ul/li[contains(text(),'Nr. băi:')]/span"
        BUILDING_YEAR = HOUSE_CARACTERISTICS +  "//ul/li[contains(text(),'An construcţie:')]/span"
        BUILDING_STRUCTURE = HOUSE_CARACTERISTICS +  "//ul/li[contains(text(),'Structură rezistenţă:')]/span"
        BUILDING_TYPE = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Tip imobil:')]/span"
        BUILDING_FLOORS = HOUSE_CARACTERISTICS + "//ul/li[contains(text(),'Regim înălţime:')]/span"
        # House specifications
        # TODO: change specs xpaths with more reliable xpaths
        SPECS = "//*[@id='b_detalii_specificatii']"
        SPECS_UTILITIES = SPECS + "/ul[1]"
        SPECS_FINISHING = SPECS + "/ul[2]"
        SPECS_FEATURES = SPECS + "/ul[3]"
        SPECS_OTHER_DETAILS_AREA = SPECS + "/ul[4]"
        SPECS_NEIGHBOURHOOD = SPECS + "/ul[5]"
        SPECS_OTHER_DETAILS_PRICE = SPECS + "/ul[6]"



