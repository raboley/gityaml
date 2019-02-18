from gityaml.git_to_yaml import GitYaml
from gityaml.gitcommit import GitCommit

import os
import unittest
from testfixtures import TempDirectory

# Test stub so tests aren't dependent on having a specific commmit
class GitCommit_Test(GitCommit):
    def get_hash(self):
        return '525b2550eb10dcbab2643ebf0417c90a2afe38dc'
    def get_url(self):
        return 'https://hurontfs.visualstudio.com/products/_git/GitYaml'

class git_to_yaml_integration(unittest.TestCase):
    
    def setUp(self):
        # Before every test create a Puppetfile.yaml file with the initial_yaml content
        self.d = TempDirectory()
        
        self.initial_yaml = b"""modules:
  nagiosmonitor_checkldap:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap
    ref: 59bf2d9045688a75cd22f02b9fe5493d276ab5d7
"""
        self.inital_path = 'Puppetfile.yaml'
        self.d.write(self.inital_path, self.initial_yaml)

        self.two_items_yaml = b"""modules:
  nagiosmonitor_checkldap:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap
    ref: 59bf2d9045688a75cd22f02b9fe5493d276ab5d7
  vscode:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode
    ref: lasij34256lawengffasd89ewal3259034qjnlk
"""
        self.two_items_path = 'two_items_Puppetfile.yaml'
        self.d.write(self.two_items_path, self.two_items_yaml)

        self.empty_file_path = 'empty_Puppetfile.yaml'
        self.d.write(self.empty_file_path, b'')

    
    def tearDown(self):
        # After every test delete everything in the temp directory
        self.d.cleanup()


    def test_read_yaml_file_to_data(self):
        path = os.path.join(self.d.path, self.inital_path)
        git_yaml = GitYaml(path)
        result_data = git_yaml.get_yaml_data()
        
        expected_data = { 'modules': 
                { 'nagiosmonitor_checkldap': 
                    { 'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                    'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
                }
            }
        }
        self.assertEqual(result_data, expected_data)

    
    def test_write_data_to_yaml_file(self):
        path = os.path.join(self.d.path, self.inital_path)
        git_yaml = GitYaml(path)

        yaml_to_write = """modules:
  nagiosmonitor_checkldap:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap
    ref: 59bf2d9045688a75cd22f02b9fe5493d276ab5d7
  vscode:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode
    ref: lasij34256lawengffasd89ewal3259034qjnlk
"""
        expected_data = { 'modules': 
                    { 'nagiosmonitor_checkldap': 
                        { 
                            'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                            'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
                        },
                    'vscode':
                        {
                            'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                            'ref': 'lasij34256lawengffasd89ewal3259034qjnlk'
                        }
                    }
                } 

        git_yaml.write_yaml_file(path, yaml_to_write)
        result_data = GitYaml(path).get_yaml_data()
        self.assertEqual(result_data, expected_data)
    
    def test_add_new_commit_to_file(self):
        path = os.path.join(self.d.path, self.inital_path)
        git_yaml = GitYaml(path)
        new_commit = { 'vscode': 
                { 
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'New_Ref_commit'
                }
            }

        expected_data = { 'modules': 
            { 'nagiosmonitor_checkldap': 
                { 
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                    'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
                },
            'vscode':
                {
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'New_Ref_commit'
                }
            }
        } 

        git_yaml.add_commit_to_file(new_commit)
        result_data = GitYaml(path).get_yaml_data()
        self.assertEqual(result_data, expected_data)
        
    def test_add_commit_to_file_updates_commit_ref(self):
        path = os.path.join(self.d.path, self.two_items_path)
        git_yaml = GitYaml(path)
        new_commit = { 'vscode': 
                { 
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'Updated_ref_Commit'
                }
            }

        expected_data = { 'modules': 
            { 'nagiosmonitor_checkldap': 
                { 
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                    'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
                },
            'vscode':
                {
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'Updated_ref_Commit'
                }
            }
        } 

        git_yaml.add_commit_to_file(new_commit)
        result_data = GitYaml(path).get_yaml_data()
        self.assertEqual(result_data, expected_data)

    def test_add_commit_to_file_creates_if_blank(self):
        path = os.path.join(self.d.path, self.empty_file_path)
        git_yaml = GitYaml(path)
        new_commit = { 'vscode': 
                { 
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'Updated_ref_Commit'
                }
            }
        expected_data = { 'modules': 
            {'vscode':
                {
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'Updated_ref_Commit'
                }
            }
        } 


        git_yaml.add_commit_to_file(new_commit)
        result_data = GitYaml(path).get_yaml_data()
        self.assertEqual(result_data, expected_data)

    def test_add_commit_to_file_creates_file_if_doesnt_exist(self):
        path = os.path.join(self.d.path, 'New_Puppetfile.yaml')
        git_yaml = GitYaml(path)
        new_commit = { 'vscode': 
                { 
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'Updated_ref_Commit'
                }
            }
        expected_data = { 'modules': 
            {'vscode':
                {
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                    'ref': 'Updated_ref_Commit'
                }
            }
        } 


        git_yaml.add_commit_to_file(new_commit)
        result_data = GitYaml(path).get_yaml_data()
        self.assertEqual(result_data, expected_data)

    def test_commit_and_file_get_created(self):
        path = os.path.join(self.d.path, 'integration_Puppetfile.yaml')
        git_yaml = GitYaml(path)
        git_commit = GitCommit_Test()
        new_commit = git_commit.new_commit_ref()

        expected_data = { 'modules': 
            {'GitYaml':
                {
                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/GitYaml',
                    'ref': '525b2550eb10dcbab2643ebf0417c90a2afe38dc'
                }
            }
        } 


        git_yaml.add_commit_to_file(new_commit)
        result_data = GitYaml(path).get_yaml_data()
        self.assertEqual(result_data, expected_data)

if __name__ == '__main__':
    unittest.main()