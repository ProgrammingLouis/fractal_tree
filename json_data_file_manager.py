import json

class manager:
    def __init__(self, path, default_datas):
        self.datas = None
        self.path = path
        self.default_datas = default_datas

        self.read_file()

    def read_file(self):
        try:
            print("laoding", self.path)
            file_read = open(self.path, "r")
            self.datas = json.load(file_read)
            file_read.close()

            # check and reset if keys are mising ; WILL NORMALY NEVER APPEND
            for key in self.default_datas.keys():
                if key not in self.datas:
                    print("key \"" + key + "\" not found. key will be created")
                    self.datas[key] = self.default_datas[key]
                    self.write_datas()

            print(self.path, "file loaded")
            print("datas : ")
            print(self.datas)

        # if we were not able to find the file
        except FileNotFoundError:
            print(self.path, "not found. File will be created")
            self.datas = self.default_datas
            self.write_datas()

        # if there is an error when converting the file
        except json.decoder.JSONDecodeError:
            print(self.path, "error while converting. File will be reset to default")
            self.datas = self.default_datas
            self.write_datas()

    def write_datas(self):
        file_write = open(self.path, "w")
        json.dump(self.datas, file_write, indent=4)
        file_write.close()
        print(self.path, "file created or updated")
        print("datas : ")
        print(self.datas)