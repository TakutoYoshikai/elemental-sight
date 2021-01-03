from git import Repo
from io import BytesIO
import os

repo = Repo("/home/lucky/obin")
commits = list(repo.iter_commits("master"))
exported_dir = "./tmp"

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
        f = open(d + "/" + file_name, "wb")
        f.write(contents.encode("utf-8", "surrogateescape"))
        f.close()
        i = i + 1

