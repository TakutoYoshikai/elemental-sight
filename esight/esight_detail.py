import json
import argparse

def get_commit_detail(index):
    with open("./git.json", "r") as f:
        json_data = json.load(f)
        print(json_data[index])

def main():
    parser = argparse.ArgumentParser(description="This is an extractor of git repository.")
    parser.add_argument("index")
    args = parser.parse_args()
    get_commit_detail(args.index)


if __name__ == "__main__":
    main()
