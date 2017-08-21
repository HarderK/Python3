import urllib.request
import urllib.error
import re
import urlparse

def download(url, num_retries=2, user_agent='wswp'):
    print('Downloading: ', url)
    headers = {'User_agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('Download error:', e.reason)
        html = None
        if hasattr(e, 'reason'):
            print('fail to reach a server')
            print('Reason: ', e.reason)
        elif num_retries > 0 and hasattr(e, 'error'):
            # 服务器端错误则继续请求
            if 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


# 网站地图爬虫
def crawl_sitemap(url):
    sitemap = download(url)     # download the sitemap file
    links = re.findall('<loc>(.*?)</loc>', sitemap)     # extract sitemap links
    for link in links:
        html = download(link)
        if html is None:
            break
        else:
            pass


def link_crawler(seed_url, link_regex):
    # crawl from the given seed URL following links matched by link_regex
    crawler_queue = [seed_url]
    seen = set(crawler_queue)

    while crawler_queue:
        url = crawler_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)

                if link not in seen:
                    crawler_queue.append(link)
                    seend.add(link)

def get_links(html):
    # return a list of links from html
    # regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=(["\'])(.*?)\\1', re.IGNORECASE)
    return webpage_regex.findall(html)