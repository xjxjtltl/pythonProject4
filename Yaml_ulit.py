import yaml


# 读写Yaml文件

class Yaml_Ulit:
    def __init__(self, path):
        self.path = path

    # 读取yaml文件
    def yaml_read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            file = yaml.safe_load(f)
        return file

    # 写入yaml文件
    def yaml_write(self, data):
        with open(self.path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, allow_unicode=True)
