import yaml
import shutil
import os


def main():
    with open("scores.yml") as f:
        res = yaml.load(f, Loader=yaml.BaseLoader)

    for score, files in res.items():
        dirpath = f"scored/{score}/"
        print(dirpath)

        if not os.path.isdir(dirpath):
            os.makedirs(dirpath)

        for filename in files:
            shutil.copy(f"img/{filename}", f"scored/{score}/{filename}")

    return res


if __name__ == "__main__":
    main()
