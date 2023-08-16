from bs4 import BeautifulSoup
import requests
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
idElements=soup.find(id="ResultsContainer")
job_elements=idElements.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip(),company_element.text.strip(),location_element.text.strip())