from git_to_yaml import GitYaml

import unittest
from unittest.mock import patch

class git_to_yaml(unittest.TestCase):
    

    @patch('git_to_yaml.GitYaml.read_yaml_file')
    def setUp(self, mock_read_yaml_file):
        mock_read_yaml_file.return_value = return_value="""modules:
  nagiosmonitor_checkldap:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap
    ref: 59bf2d9045688a75cd22f02b9fe5493d276ab5d7
"""
        self.git_yaml = GitYaml('fake')

    #def tearDown(self):
        
        

    def test_dict_to_yaml_returns_yaml_string(self):
        # in setUp class an object that contains the return yaml value
        # is stored, and this ensures that the yaml string matches.
        data = { 'modules': 
                    { 'nagiosmonitor_checkldap': 
                        { 'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                        'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
                    }
                  }
                }
        expected_yaml ="""modules:
  nagiosmonitor_checkldap:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap
    ref: 59bf2d9045688a75cd22f02b9fe5493d276ab5d7
"""
        result_yaml = self.git_yaml.data_to_yaml(data)
        self.assertEqual(result_yaml, expected_yaml)
    
    
    def test_yaml_to_dict_returns_same_thing(self):
        yaml_string = """modules:
  nagiosmonitor_checkldap:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap
    ref: 59bf2d9045688a75cd22f02b9fe5493d276ab5d7
"""
        expected_data = { 'modules': 
                    { 'nagiosmonitor_checkldap': 
                        { 'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                        'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
                    }
                  }
                }
        result_data = self.git_yaml.yaml_to_data(yaml_string)
        self.assertEqual(result_data, expected_data)
    

    def test_yaml_to_dict_will_return_multiple_modules(self):
        
        # Indenting and spacing of these strings is very important. tests will fail if the strings here are not properyly indented
        yaml_string = """modules:
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
        result_data = self.git_yaml.yaml_to_data(yaml_string)
        self.assertEqual(result_data, expected_data)


    def test_append_dict_to_dicts_maintains_earlier_dict_and_appends_new(self):
        data = { 'modules': 
                    { 'nagiosmonitor_checkldap': 
                        { 'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                        'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
                    }
                  }
                }
        new_dict = { 'vscode': 
                        { 
                          'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                          'ref': 'lasij34256lawengffasd89ewal3259034qjnlk'
                        }
                    }
        expected_dict = { 'modules': 
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
        result_dict = self.git_yaml.append_dict_to_dicts(data, new_dict)
        self.assertEqual(result_dict, expected_dict)
    
    def test_append_dict_to_dicts_updates_dictionary_when_already_exists(self):
        data = { 'modules': 
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
        updated_data = { 'vscode': 
                        { 
                          'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode',
                          'ref': 'New_Ref_commit'
                        }
                    }
        expected_dict = { 'modules': 
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
        result_dict = self.git_yaml.append_dict_to_dicts(data, updated_data)
        self.assertEqual(result_dict, expected_dict)



    # def test_output_string(self):
    #     ref = '59bf2d9045688a75cd22f02b9fe5493d276ab5d7'
    #     module = 'nagiosmonitor_checkldap'
    #     uri = 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap'

    #     output_string = convert_git_checkin_to_yaml(ref=ref,module=module,uri=uri)
    #     self.assertEqual(output_string,result_string)

if __name__ == '__main__':
    unittest.main()