import yaml
import os
class GitYaml():
    
    def add_commit_to_file(self, commit):
        if self._yaml_data == None:
            self.set_yaml_from_string('modules: {}') # {'modules': None}
        self._yaml_data = self.append_dict_to_dicts(self._yaml_data, commit)
        self._yaml_string = self.data_to_yaml(self._yaml_data)
        self.write_yaml_file(self._yaml_path, self._yaml_string)

    def __init__(self, yaml_path):
        self._yaml_path = yaml_path
        self._yaml_data = self.read_yaml_file(path=self._yaml_path)
        self._yaml_string = self.data_to_yaml(self._yaml_data)

    def read_yaml_file(self, path):
        if os.path.lexists(path):
            with open(path, 'r') as stream:
                try:
                    return yaml.load(stream)
                except yaml.YAMLError as exc:
                    return exc
        else:
            print(path + 'does not exist')
    
    def get_yaml_string(self):
        return self._yaml_string
    
    def get_yaml_data(self):
        return self._yaml_data
    
    def set_yaml_from_string(self, yaml_string):
        self._yaml_string = yaml.dump(yaml_string)
        self._yaml_data = self.yaml_to_data(yaml_string)
    
    def write_yaml_file(self, path, yaml):
        with open(path, 'w') as outfile:
            outfile.write(yaml)
    

    def append_dict_to_dicts(self, data, new_dict):
        data['modules'].update(new_dict)
        return data

    def yaml_to_data(self, yaml_string):
        result_data = yaml.load(yaml_string)
        return result_data

            
    def data_to_yaml(self, data):
        """convert a dictionary of dictionaies to yaml string
        
        Arguments:
            data {dict} -- a dictionary datatype that can be n layers deep ex. 
                {'modules': 
                    { 'module1': { 'ref': 'abcd',
                                'git': hurontfs@vs-ssh.com/module1'}
                                }, 
                    'module2': { 'ref': 'efgh',
                                'git': hurontfs@vs-ssh.com/module2'} 
                                }
                    }
                }
        
        Returns:
            [string] -- a converted yaml string format ex.
            modules:
            module1:
                ref: abcd
                git: hurontfs@vs-ssh.com/module1
            module2:
                ref: efgh
                git: hurontfs@vs-ssh.com/module2
        """
        result_yaml = yaml.dump(data, default_flow_style=False)
        return result_yaml







# def output_yaml_string():
#     return ''

# def convert_git_checkin_to_yaml(ref, module, uri):
#     return ref + module + uri

if __name__ == '__main__':
    data = { 'modules': 
            { 'nagiosmonitor_checkldap': 
                { 'git': 'hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nagiosmonitor_checkldap',
                'ref': '59bf2d9045688a75cd22f02b9fe5493d276ab5d7' 
            }
            }
        }
    dict_to_yaml(data)