# import requests
# from bs4 import BeautifulSoup
#
#
# def extract_articles_from_page(url):
#     # Send a GET request to the URL
#     response = requests.get(url)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content of the webpage
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # Find all elements with class="f9uzM"
#         elements = soup.find_all(class_='f9uzM')
#
#         articles = []
#         # Iterate through each found element
#         for element in elements:
#             # Find all articles within the current element
#             article_elements = element.find_all('article', class_='UwIKyb')
#             for article_element in article_elements:
#                 # Extract relevant information from the article element
#                 article = {}
#                 article['source'] = article_element.find(class_='vr1PYe').text.strip()
#                 article['title'] = article_element.find('a', class_='gPFEn').text.strip()
#                 article['url'] = article_element.find('a', class_='gPFEn')['href']
#                 article['timestamp'] = article_element.find('time')['datetime']
#
#                 possible_author = article_element.find(class_='PJK1m')
#
#                 if possible_author is not None:
#                     article['author'] = possible_author.text.strip()
#
#                 articles.append(article)
#
#         return articles
#     else:
#         # If the request was not successful, print an error message
#         print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
#         return []
#
#
# # Example usage:
# url = 'https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en'  # Replace this with the URL you want to search
# articles = extract_articles_from_page(url)
# for article in articles:
#     print(article)

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


def clean_text(text):
    # Remove escape sequences and unnecessary whitespace
    text = re.sub(r"\\'", "'", text) # Remove backslash followed by any character
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()


def truncate_text(text, max_words):
    words = text.split()
    if len(words) <= max_words:
        return text
    truncated = ' '.join(words[:max_words])
    # Ensure the truncated text ends with a period
    if not truncated.endswith('.'):
        truncated = truncated.rsplit('.', 1)[0] + '.'
    return truncated


def extract_text_from_website1(article_soup):
    """
    Extract article text from the first news website.

    Parameters:
    article_soup (BeautifulSoup): The BeautifulSoup object of the article.

    Returns:
    str: The extracted article text.
    """
    # Find the <p> element with the specified classes
    article_text_element = article_soup.find('p', class_='sdc-article-header__sub-title sdc-site-component-header--h2')

    if article_text_element:
        raw_text = article_text_element.get_text(separator='\n')
        return clean_text(raw_text)

    return "Article text not found."

def extract_text_from_website2(article_soup):
    """
    Extract the text of the second paragraph from the article.

    Parameters:
    article_soup (BeautifulSoup): The BeautifulSoup object of the article.

    Returns:
    str: The extracted text of the second paragraph, or None if not found.
    """
    # Find the div with the specified class
    article_content_div = article_soup.find('div', class_='article__content')

    if article_content_div:
        paragraphs = article_content_div.find_all('p')
        if len(paragraphs) >= 2:
            raw_text = paragraphs[1].get_text()
            return clean_text(raw_text)

    return None

def extract_text_from_website3(article_soup):
    """
    Extract the text of the specific paragraph from the article.

    Parameters:
    article_soup (BeautifulSoup): The BeautifulSoup object of the article.

    Returns:
    str: The extracted text of the specific paragraph, or None if not found.
    """
    # Find the <p> element with the specified class
    specific_paragraph_element = article_soup.find('p', class_='ssrcss-1q0x1qg-Paragraph e1jhz7w10')

    if specific_paragraph_element:
        raw_text = specific_paragraph_element.get_text(separator='\n')
        return clean_text(raw_text)

    return None
def extract_text_from_website4(article_soup):
    """
       Extract the text from the first two paragraphs with the specified class from the article.

       Parameters:
       article_soup (BeautifulSoup): The BeautifulSoup object of the article.

       Returns:
       str: The extracted text from the first two paragraphs, or None if not found.
       """
    # Find all <p> elements with the specified class
    paragraph_elements = article_soup.find_all('p', class_='mol-para-with-font')

    if paragraph_elements:
        # Extract text from the first two paragraphs
        first_two_paragraphs_text = ""
        for paragraph in paragraph_elements[:2]:
            first_two_paragraphs_text += paragraph.get_text(separator='\n') + '\n'
        raw_text = first_two_paragraphs_text.strip()
        return clean_text(raw_text)

    return None

def extract_text_from_website5(article_soup):
    """
      Extract the text from the first two paragraphs with the specified class from the article.

      Parameters:
      article_soup (BeautifulSoup): The BeautifulSoup object of the article.

      Returns:
      str: The extracted text from the first two paragraphs, or None if not found.
      """
    # Find all <p> elements with the specified class
    paragraph_elements = article_soup.find_all('p', class_='dcr-iy9ec7')

    if paragraph_elements:
        # Extract text from the first two paragraphs
        first_two_paragraphs_text = ""
        for paragraph in paragraph_elements[:2]:
            first_two_paragraphs_text += paragraph.get_text(separator='\n') + '\n'
        raw_text = first_two_paragraphs_text.strip()
        return clean_text(raw_text)

    return None

def extract_text_from_website6(article_soup):
    """
    Extract text from a <p> element within a specific hierarchy of classes.

    Parameters:
    article_soup (BeautifulSoup): The BeautifulSoup object of the article.

    Returns:
    str: The extracted text from the <p> element, or None if not found.
    """
    # Navigate through the specified hierarchy
    container = article_soup.find('div', class_='vsc-initialized meter-ribbon-visible')
    if container:
        container = container.find('div', class_='main-content main-content--desktop-article main-content--universal-header')
    if container:
        container = container.find('div', class_='pay-wall-content content_664cb6592785155cfe42bdf8 current-page ads-loaded')
    if container:
        container = container.find('div', class_='main-content-body')
    if container:
        container = container.find('div', class_='article-wrapper')
    if container:
        container = container.find('div', class_='body-container')
    if container:
        container = container.find('div', class_='article-body-container')
    if container:
        container = container.find('div', class_='article-body fs-article fs-responsive-text current-article article-topline')

    # Find the first <p> element within the final container
    if container:
        paragraph_element = container.find('p')
        if paragraph_element:
            return paragraph_element.get_text(separator='\n').strip()

    return None

def extract_articles_from_page(url, max_words=200):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with class="f9uzM"
        elements = soup.find_all(class_='f9uzM')

        articles = []
        # Iterate through each found element
        for element in elements:
            # Find all articles within the current element
            article_elements = element.find_all('article', class_='UwIKyb')
            for article_element in article_elements:
                # Extract relevant information from the article element
                article = {}
                article['source'] = article_element.find(class_='vr1PYe').text.strip()
                article['title'] = article_element.find('a', class_='gPFEn').text.strip()
                article_url = article_element.find('a', class_='gPFEn')['href']
                article['url'] = urljoin(url, article_url)  # Prepend base URL to form complete URL
                article['timestamp'] = article_element.find('time')['datetime']

                possible_author = article_element.find(class_='PJK1m')
                if possible_author is not None:
                    article['author'] = possible_author.text.strip()

                # Fetch the content of the article URL
                article_response = requests.get(article['url'])
                if article_response.status_code == 200:
                    # Parse the HTML content of the article page
                    article_soup = BeautifulSoup(article_response.content, 'html.parser')

                    article['text'] = None
                    if article['source'] == "Sky News":
                        article['text'] = extract_text_from_website1(article_soup)
                    elif article['source'] == "The Sun":
                        article['text'] = extract_text_from_website2(article_soup)
                    elif article['source'] == "BBC":
                        article['text'] = extract_text_from_website3(article_soup)
                    elif article['source'] == 'Daily Mail':
                        article['text'] = extract_text_from_website4(article_soup)
                    elif article['source'] == 'The Guardian':
                        article['text'] = extract_text_from_website5(article_soup)
                    elif article['source'] == 'Forbes':
                        article['text'] = extract_text_from_website6(article_soup)

                    if article['text'] is None:
                        article['text'] = "Article text not found."

                articles.append(article)

        return articles
    else:
        # If the request was not successful, print an error message
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return []

# Example usage:
url = 'https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en'  # Replace this with the URL you want to search
articles = extract_articles_from_page(url)
for article in articles:
    print(article)
