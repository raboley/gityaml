from gitcommit import GitCommit
from git_to_yaml import GitYaml

from sys import argv
module_name, repo_name, commit_ref, yaml_path = argv

class scripted_GitCommit(GitCommit):
    def __init__(self, repo_name, commit_ref):
        self._repo_name = repo_name
        self._commit_ref = commit_ref

    def get_project_name(self):
        return self._repo_name

    def new_commit_ref(self):
        ssh_address = self.get_ssh_address()
        data = { self._repo_name: { 'ref': self._commit_ref, 'git': ssh_address}}
        return data

# create a commit tag from current repo
#git_commit = GitCommit('C:\\Users\\rboley\\Desktop\\git\\azure_devops\\git_to_yaml')
git_commit = scripted_GitCommit(repo_name=repo_name, commit_ref=commit_ref)
commit = git_commit.new_commit_ref()
# add commit to other repo's puppetfile
#puppetfile_path = 'C:\\Users\\rboley\\Desktop\\Puppet-Control\puppet_File.yaml'

git_yaml = GitYaml(yaml_path)
git_yaml.add_commit_to_file(commit)

# python3 C:\Users\rboley\Desktop\git\azure_devops\git_to_yaml\src\gityaml 'test' '1235456789' 'C:\Users\rboley\Desktop\git\azure_devops\git_to_yaml\src\gityaml\test.yaml'