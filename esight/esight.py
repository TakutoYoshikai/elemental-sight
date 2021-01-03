from git import Repo
import os
import argparse



def file_write(filename, content):
    file_dir = os.path.dirname(filename)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    with open(filename, "wb") as f:
        f.write(content)

def extract_repo(repo_path, branch, exported_dir="./tmp"):
    repo = Repo(repo_path)
    commits = list(repo.iter_commits(branch))
    i = 1
    for commit in commits:
        print("=" * 30)
        for file_name in commit.stats.files:
            print(file_name)
            contents = None
            try:
                contents = repo.git.show('{}:{}'.format(commit.hexsha, file_name))
            except:
                continue
            d = exported_dir + "/" + str(i)
            os.makedirs(d)
            file_write(d + "/" + file_name, contents.encode("utf-8", "surrogateescape"))
        i = i + 1


def main():
    parser = argparse.ArgumentParser(description="This is an extractor of git repository.")
    parser.add_argument("repo")
    parser.add_argument("branch")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    if args.output == None:
        extract_repo(args.repo, args.branch)
    else:
        extract_repo(args.repo, args.branch, args.output)


if __name__ == "__main__":
    main()
