#!/usr/bin/python3
"""Module for fetching and saving posts"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints posts"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetches and saves posts"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["userId", "id", "title", "body"])
            for post in posts:
                writer.writerow([post["userId"], post["id"],
                                post["title"], post["body"]])
