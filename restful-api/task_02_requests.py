#!/usr/bin/usr

import requests
import csv
r = requests.get('https://jsonplaceholder.typicode.com/posts')


def fetch_and_print_posts():
    print(f'Status Code: {r.status_code}')
    if r.status_code == 200:
        json_obj = r.json()
        for i in json_obj:
            print(i['title'])


def fetch_and_save_posts():
    if r.status_code == 200:
        posts = []
        for i in r.json():
            new_post = {
                'id': i['id'],
                'title': i['title'],
                'body': i['body']
            }
            posts.append(new_post)
        with open('posts.csv', 'w', newline="", encoding='utf-8') as post:
            write = csv.DictWriter(post, fieldnames=['id','title', 'body'])
            write.writeheader()
            write.writerows(posts)

