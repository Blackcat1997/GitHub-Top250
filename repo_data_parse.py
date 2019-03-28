from bs4 import BeautifulSoup as BS
import requests
import re
import json

repo_names = []
repo_description = []
repo_links = []
repo_date = []
star = []
repositories = []

url = "https://github.com/search?o=desc&q=stars%3A%3E1&s=stars&type=Repositories"
# def fetch_repo(url):
html = requests.get(url) # Get HTML code
soup_first_page = BS(html.content, 'html.parser') #Parse html
# print(soup_first_page.prettify)
def get_name(content):
    return content.string
def get_link(content):
    return "https://github.com" + content.get('href')
def get_date(content):
    return content.get('datetime')
def get_description(content):
    return content.get_text().strip()
def get_star(content):
    content = re.sub("[^0-9.k$]", "", content.text)
    if ("k" in content):
        return content

def fetch_repo_every_page(data_type, tag, attr, process):
    for data in soup_first_page.find_all(tag, attr):
        final = process(data)
        data_type.append(final)
    
fetch_repo_every_page(repo_names, 'a', {'class': "v-align-middle"}, get_name)
fetch_repo_every_page(repo_links, 'a', {'class': "v-align-middle"}, get_link)
fetch_repo_every_page(repo_description, 'p', {'class': "col-12 col-md-9 d-inline-block text-gray mb-2 pr-4"}, get_description)
fetch_repo_every_page(repo_date, 'relative-time', '', get_date)
fetch_repo_every_page(star, 'a', {'class': "muted-link"}, get_star)

# for link in soup_first_page.find_all('a', {'class': "v-align-middle"}):
#     repo_names.append(link.string)
#     repo_links.append("https://github.com" + link.get('href'))

# for description in soup_first_page.find_all('p', {'class': "col-12 col-md-9 d-inline-block text-gray mb-2 pr-4"}):
#     repo_description.append(description.get_text().strip())

# for date in soup_first_page.find_all('relative-time', ''):
#     repo_date.append(date.get('datetime'))

# for star in soup_first_page.find_all('a', {'class': "muted-link"}):
#     star = re.sub("[^0-9.k$]", "", star.text)
#     if ("k" in star):
#         stars.append(star)
# url_one = 'https://github.com/search?o=desc&q=stars%3A%3E1&s=stars&type=Repositories'
# url_two = 'https://github.com/search?o=desc&p=2&q=stars%3A%3E1&s=stars&type=Repositories'
# fetch_repo(url_one)
# fetch_repo(url_two)
for index in range(len(repo_names)):
    repositories.append({"name": repo_names[index], 
                            "description": repo_description[index],
                            "star": star[index],
                            "date": repo_date[index]
                        })

for repository in repositories:
    print(repository["name"], repository["star"])
# json_data = json.dumps(repositories)
# print(repositories)