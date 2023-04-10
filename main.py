from anticaptchaofficial.turnstileproxyless import *
import requests
from bs4 import BeautifulSoup, ResultSet
import os


def anti_captcha(url, cookie, siteKey):
    solver = turnstileProxyless()
    solver.set_verbose(0)
    solver.set_key(get_anticaptcha_api_key())
    solver.set_website_url(url)
    solver.set_cookies("PHPSESSID=" + cookie)
    solver.set_website_key(siteKey)

    solver.set_soft_id(0)

    token = solver.solve_and_return_solution()
    if token != 0:
        return token
    else:
        print("task finished with error " + solver.error_code)
        return


def get_anticaptcha_api_key():
    return os.environ['ANTICAPTCHA_API_KEY']


def get_protected_link(url, token):
    jsonObject = {'subform': 'unlock', 'cf-turnstile-response': token}
    response = requests.post(url, data=jsonObject)
    htmlSoup = BeautifulSoup(response.text, "html.parser")
    urls = htmlSoup.find(class_="urls")
    return urls.find("a").attrs.get("href")


def get_cookie(firstPageResponse):
    return firstPageResponse.cookies.get("PHPSESSID")


def get_first_page_response(url):
    return requests.get(url)


def get_dl_protect_link(url):
    response = get_first_page_response(url)
    html = get_html(response.text)
    sitekey = html.find(class_="cf-turnstile").attrs.get("data-sitekey")
    cookie = get_cookie(response)
    token = anti_captcha(url, cookie, sitekey)
    return get_protected_link(url, token)


def get_one_fichier_links(postInfoChildren: ResultSet):
    alreadySet = False
    links = []

    for tag in postInfoChildren:
        if (tag.findNext().name == 'div'):
            if (tag.text.__contains__("1fichier")):
                alreadySet = True
            elif alreadySet:
                break
        elif tag.findNext().name == 'a' and alreadySet:
            links.append(tag.findNext().attrs.get("href"))
    return links


def get_dl_protect_links(url):
    response = requests.get(url)
    htmlResponse = get_html(response.text)
    postInfo = htmlResponse.find(class_="postinfo")
    return get_one_fichier_links(postInfo.findAll('b'))


def get_html(htmlText):
    return BeautifulSoup(htmlText, "html.parser")


def find_links(url):
    dlProtectLinks = get_dl_protect_links(url)
    protectedLinks = []
    for link in dlProtectLinks:
        protectedLink = get_dl_protect_link(link)
        print(protectedLink)
        protectedLinks.append(protectedLink)
    return "\n".join(protectedLinks)


if __name__ == '__main__':
    print(find_links("https://www.zone-telechargement.day/?p=serie&id=15501-power-saison5"))
