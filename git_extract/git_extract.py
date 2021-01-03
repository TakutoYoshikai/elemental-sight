from git import Repo
from io import BytesIO
import os

repo = Repo("/home/lucky/obin")
commits = list(repo.iter_commits("master"))
exported_dir = "./tmp"

i = 1

def file_write(filename, content):
    file_dir = os.path.dirname(filename)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    with open(filename, "wb") as f:
        f.write(content)
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

