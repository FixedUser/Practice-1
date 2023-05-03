import csv
import requests
from pprint import pprint


def analyze_text_file(filepath: str) -> None:
    with open(filepath) as f:
        text = f.read().lower()

    words = [word for word in text.split(' ') if word.isalpha()]
    unique_words = set(words)

    word_counts = {word: words.count(word) for word in unique_words}

    pprint(word_counts)


def download_csv_file(url: str) -> None:
    save_as = 'source_data/file.csv'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        print(f"Під час завантаження файлу сталася помилка: {exc}")
    else:
        rows = [row.split(';') for row in response.text.strip().split('\n')][:-1]

        with open(save_as, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)


if __name__ == '__main__':
    analyze_text_file(input('введіть .txt filepath: '))
    download_csv_file(input('введіть .csv url: '))