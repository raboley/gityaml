import os
import subprocess


class GitCommit():
    def get_hash(self):
        repo = os.listdir('.')[0]
        sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo).decode('ascii').strip()
        return sha

    def get_url(self):
        repo = os.listdir('.')[0]
        url = subprocess.check_output(['git', 'remote', 'get-url','origin'], cwd=repo).decode('ascii').strip()
        return url

    def get_project_name(self):
        header_url = self.get_url()
        project_name = os.path.split(header_url)[1]
        return project_name

    def get_ssh_address(self, ssh_header="hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/"):
        project_name = self.get_project_name()
        ssh_address = ssh_header + project_name
        return ssh_address

    def new_commit_ref(self):
        project_name = self.get_project_name()
        ref = self.get_hash()
        ssh_address = self.get_ssh_address()
        data = { project_name: { 'ref': ref, 'git': ssh_address}}
        return data
