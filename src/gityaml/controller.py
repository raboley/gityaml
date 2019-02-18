from gitcommit import GitCommit
from git_to_yaml import GitYaml

# create a commit tag from current repo
git_commit = GitCommit()
commit = git_commit.new_commit_ref()
# add commit to other repo's puppetfile
puppetfile_path = ''
git_yaml = GitYaml(puppetfile_path)
git_yaml.add_commit_to_file(commit)


