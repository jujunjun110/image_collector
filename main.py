import time
import datetime
import urllib.request


def main():
    fetch_count = 100
    prefix = datetime.datetime.now().strftime("%H%m%S")
    url = "https://source.unsplash.com/1024x1024/"

    for i in range(fetch_count):
        filename = f"{prefix}_{i:04}.jpg"
        print(filename)
        urllib.request.urlretrieve(url, f"img/{filename}")
        time.sleep(3)


if __name__ == "__main__":
    main()
