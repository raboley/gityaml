from gitcommit import GitCommit
from git_to_yaml import GitYaml

# create a commit tag from current repo
#git_commit = GitCommit('C:\\Users\\rboley\\Desktop\\git\\azure_devops\\git_to_yaml')
git_commit = GitCommit('/git')
commit = git_commit.new_commit_ref()
# add commit to other repo's puppetfile
#puppetfile_path = 'C:\\Users\\rboley\\Desktop\\Puppet-Control\puppet_File.yaml'
puppetfile_path = '/control-repo/Puppetfile.yaml'
git_yaml = GitYaml(puppetfile_path)
git_yaml.add_commit_to_file(commit)


