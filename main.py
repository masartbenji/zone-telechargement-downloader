from anticaptchaofficial.turnstileproxyless import *
import requests
from bs4 import BeautifulSoup, ResultSet
import os


def anti_captcha(url, cookie, site_key):
    solver = turnstileProxyless()
    solver.set_verbose(0)
    solver.set_key(get_anticaptcha_api_key())
    solver.set_website_url(url)
    solver.set_cookies("PHPSESSID=" + cookie)
    solver.set_website_key(site_key)

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
    json_object = {'subform': 'unlock', 'cf-turnstile-response': token}
    response = requests.post(url, data=json_object)
    html = get_html(response.text)
    urls = html.find(class_="urls")
    return urls.find("a").attrs.get("href")


def get_cookie(first_page_response):
    return first_page_response.cookies.get("PHPSESSID")


def get_first_page_response(url):
    return requests.get(url)


def get_dl_protect_link(url):
    response = get_first_page_response(url)
    html = get_html(response.text)
    sitekey = html.find(class_="cf-turnstile").attrs.get("data-sitekey")
    cookie = get_cookie(response)
    token = anti_captcha(url, cookie, sitekey)
    return get_protected_link(url, token)


def get_one_fichier_links(post_info_children: ResultSet):
    already_set = False
    links = []

    for tag in post_info_children:
        if tag.findNext().name == 'div':
            if tag.text.__contains__("1fichier"):
                already_set = True
            elif already_set:
                break
        elif tag.findNext().name == 'a' and already_set:
            links.append(tag.findNext().attrs.get("href"))
    return links


def get_dl_protect_links(url):
    response = requests.get(url)
    html_response = get_html(response.text)
    post_info = html_response.find(class_="postinfo")
    return get_one_fichier_links(post_info.findAll('b'))


def get_html(html_text):
    return BeautifulSoup(html_text, "html.parser")


def find_links(url):
    dl_protect_links = get_dl_protect_links(url)
    protected_links = []
    for link in dl_protect_links:
        protected_link = get_dl_protect_link(link)
        print(protected_link)
        protected_links.append(protected_link)
    return "\n".join(protected_links)


if __name__ == '__main__':
    print(find_links("https://www.zone-telechargement.day/?p=serie&id=15501-power-saison5"))
