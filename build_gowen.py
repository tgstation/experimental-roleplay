from git import Repo
import shutil
import os
import distutils

folder_to_copy = "./gowen_repo"
folder_to_target = "./tmp/tgrepo"
if not os.path.exists(folder_to_target):
    print("Cloning /tg/station...")
    repo = Repo.clone_from("https://github.com/tgstation/tgstation.git", to_path=folder_to_target)
else:
    repo = Repo(folder_to_target)
print("Resetting /tg/station to current latest commit...")
repo.git.reset('--hard')
repo.heads.master.checkout()
repo.git.reset('--hard')
repo.git.clean('-xdf')
repo.remotes.origin.pull()
print("Copying over modular_gowen...")
distutils.dir_util.copy_tree(folder_to_copy, folder_to_target)
print("Appending gowen.dme to tgstation.dme...")
dme = open("./tmp/tgrepo/tgstation.dme", "a")
dme.write("#include \"gowen.dme\"")
dme.close()
print("Running the /tg/station build process...")
os.system(".\\tmp\\tgrepo\\build.cmd")
print("Build complete!")
