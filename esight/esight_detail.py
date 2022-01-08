import json
import argparse

def get_commit_detail(index):
    with open("./git.json", "r") as f:
        json_data = json.load(f)
        print("name: " + json_data[index]["name"])
        print("email: " + json_data[index]["email"])
        print("message: " + json_data[index]["message"])

def main():
    parser = argparse.ArgumentParser(description="edetail can get commit detail.")
    parser.add_argument("index")
    args = parser.parse_args()
    get_commit_detail(args.index)


if __name__ == "__main__":
    main()
