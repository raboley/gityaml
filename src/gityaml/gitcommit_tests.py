import unittest


from gityaml.gitcommit import GitCommit

# Test stub so tests aren't dependent on having a specific commmit
class GitCommit_Test(GitCommit):
    def get_hash(self):
        return '525b2550eb10dcbab2643ebf0417c90a2afe38dc'
    def get_url(self):
        return 'https://hurontfs.visualstudio.com/products/_git/GitYaml'

class gitcommit(unittest.TestCase):
    
    def setUp(self):
        self.git_commits = GitCommit_Test()

    def test_can_get_commit_hash(self):
        expected_hash = '525b2550eb10dcbab2643ebf0417c90a2afe38dc'
        result_hash = self.git_commits.get_hash()
        self.assertEqual(result_hash, expected_hash)

    def test_can_get_git_uri(self):
        expected_uri = 'https://hurontfs.visualstudio.com/products/_git/GitYaml'
        result_uri = self.git_commits.get_url()
        self.assertEqual(result_uri, expected_uri)

    def test_can_make_full_uri(self):
        result_ssh_address = self.git_commits.get_ssh_address()
        expected_ssh_address = 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/GitYaml'
        self.assertEqual(result_ssh_address, expected_ssh_address)

    def test_get_project_name(self):
        result_project_name = self.git_commits.get_project_name()
        expected_project_name = 'GitYaml'
        self.assertEqual(result_project_name, expected_project_name)

    def test_new_commit_ref(self):
        result_data = self.git_commits.new_commit_ref()
        expected_data = { 
                            'GitYaml': 
                                { 
                                    'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/GitYaml',
                                    'ref': '525b2550eb10dcbab2643ebf0417c90a2afe38dc' 
                                }
                            }
        self.assertEqual(result_data, expected_data)
        

if __name__ == '__main__':
    unittest.main()