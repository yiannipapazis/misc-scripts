import os
import zipfile
# import github_release
# import github

# g = github.Github()

#github.ApplicationOAuth.ApplicationOAuth.get_login_url()
"""
auth = github
g.ApplicationOAuth.ApplicationOAuth.get_login_url()

repo = g.get_repo("yiannipapazis/image_menus")
"""
#user = g.get_user()
#print(user)
#user.login()
#print(user.name)
#Github.get_repo("yiannipapazis/image_menus")
name = 'Test2.zip'
ignore_dir = ['.git', '__pycache__']
ignore_file = [name, '.gitignore']

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignore_dir]
        print(dirs)
        for file in files:
            if file in ignore_file:
                pass
            else:
                ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
zipf = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED)

zipdir(os.getcwd(), zipf)
zipf.close()

"""
print(repo.get_releases())
tag = repo.get_latest_release().tag_name
latest_commit = repo.get_commits()[0]
user = g.get_user()
user.create_authorization()
user.get_authorization(user.id)
print(user.name)
#release = repo.create_git_release("tag", "#002", "test message", True, True, latest_commit)
"""
