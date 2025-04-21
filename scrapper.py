import requests
from bs4 import BeautifulSoup, Tag

# Define the URL for the Dutch verb (replace 'spreken' with any verb you want)
BASE_URL = "https://en.wiktionary.org/wiki/"

def get_relevant_elements(url):
    # Send a GET request
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find(class_="inflection-table vsSwitcher").find("tbody").find_all("tr")


def get_conjugation_from_wiki_to_list(elements):
    result = []
    result.append(elements[7].findAll()[3].findAll()[0].findAll()[0].text)
    result.append(elements[8].findAll()[5].findAll()[0].findAll()[0].text)
    result.append(elements[9].findAll()[5].findAll()[0].findAll()[0].text)
    result.append(elements[10].findAll()[5].findAll()[0].findAll()[0].text)
    result.append(elements[11].findAll()[3].findAll()[0].findAll()[0].text)
    result.append(elements[12].findAll()[3].findAll()[0].text)
    return result


def list_to_person_conjugation(conj_list):
    return {
        "ik" : conj_list[0],
        "je/jij/u" : conj_list[1],
        "hij/zij/het" : conj_list[4],
        "we/wij" : conj_list[5],
        "jullie" : conj_list[5],
        "ze/zij" : conj_list[5]
    }


def dict_to_html(conj_dict : dict):
    result = ""
    for person in conj_dict:
        result = result + """
            <div class="conj-item">
                <div class="conj-person">{}</div>
                <div class="conj-result">{}</div>
            </div>""".format(person, conj_dict[person])
    return result

    
def get_conjugation(verb):
    try:
        html = get_relevant_elements(BASE_URL + verb)
        list_v = get_conjugation_from_wiki_to_list(html)
        conj_dict = list_to_person_conjugation(list_v)
        return dict_to_html(conj_dict)
    except Exception as e:
        print(e)
        raise Exception("Problem scrapping verb {}".format(verb))
