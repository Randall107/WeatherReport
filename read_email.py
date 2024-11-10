class reader:
    def read(self, path):
        with open (path, "r") as f:
            lines = f.readlines()
            list = []
            for line in lines:
                try:
                    list.append(line[:-1])
                except Exception as e:
                    print(e)
        return list