import os
import re
import requests
import argparse
from contextlib import closing


def __download_img(url, img_path, position):
    # create directory to organize images
    if not os.path.isdir(position):
        os.makedirs(position)
    # close file when the operation is over
    with closing(requests.get(url, stream=True)) as response:
        with open(img_path, 'wb+') as file:
            # print(response.content)
            file.write(response.content)
    return


def __crawler(subject):
    urls = {
        'math': 'https://baodingwangluo.yunzhan365.com/books/movx/files/mobile/1.jpg?x-oss-process=image/resize,h_1328,w_1896/format,jpg&1577416995',
        'english': 'https://baodingwangluo.yunzhan365.com/books/hzdu/files/mobile/1.jpg?x-oss-process=image/resize,h_1328,w_1896/format,jpg&1577417235'
    }
    pages = {
        'math': 26,
        'english': 26,
    }
    positions = {
        'math': '/examPaper/math/',
        'english': '/examPaper/english/'
    }

    # local path to save exam paper
    cur_position = '/Users/eileen/dev/PycharmProjects/examPaperCrawler'

    # specify subject info
    url = urls['math']
    page = pages['math']
    position = cur_position + positions['math']
    if subject == 'english':
        url = urls['english']
        page = pages['english']
        position = cur_position + positions['english']

    # crawl all pages
    pattern = re.compile(r"\d+(.jpg)")
    for i in range(1, page):
        img_path = position + str(i) + '.jpg'
        # print(img_path)
        url = pattern.sub(str(i)+'.jpg', url)
        # print(url)
        __download_img(url, img_path, position)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", help="crawl exam paper of math or english", type=str)
    args = parser.parse_args()
    if args.subject:
        __crawler(args)
    else:
        print("please input the subject which you need, i.e. 'python3 main.py --subject math'")
