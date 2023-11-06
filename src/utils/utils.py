import time
import platform
import os


class Utils:

    def __init__(self):
        pass

    def generate_file_name_with_timestamp(self,extension):
        timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
        file_name = "screenshot-".join(timestamp).join(extension)
        return file_name
    
    def generate_env_props(self,env_info,path,file_name,env):
        environment_data = {
            "environment": env,
            "os_platform": platform.platform(),
            "os_release": platform.release(),
            "os_version": platform.version(),
            "python_version": platform.python_version(),
            "browser": env_info.get("browser"),
            "url": env_info.get("base_url"),
            "creation_time": time.strftime("%Y-%m-%dT%H-%M", time.localtime())
        }
        
        props_content = self.__json_to_props(environment_data)
        file_path = str(path).__add__(file_name)

        # save the file with environment information
        self.__write_content_to_file(file_path, props_content)
    

    def __json_to_props(self,data):
        props_content = []
        for key, value in data.items(): 
            props_content.append(f'{key}={value}\n')
        
        return "".join(props_content)
    
    def __create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    
    def __write_content_to_file(self, file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.seek(0)
                file.truncate()
                file.write(content)
                file.close()
            print(f'File successfully saved at {file_path}')
        except Exception as ex:
            print(f'An error ocurred while saving file {str(ex)}')
