"""
File reading class
"""

class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name
        
    def _file_read_all_str_list(self):
        f = open(self.file_name, "r")
        self.str_list = f.readlines()
        f.close()
        
    def file_as_int_list(self):
        self._file_read_all_str_list()
        int_list = []
        for str_num in self.str_list:
            str_split = str_num.split(" ")
            for str_ele in str_split:
                single_int = int(str_ele)
                int_list.append(single_int)
        return int_list

    def file_as_int_line_list(self):
        self._file_read_all_str_list()    
        int_line_list = []
        
        for str_num in self.str_list:
            int_line = []
            str_split = str_num.split(" ")
            for str_ele in str_split:
                single_int = int(str_ele)
                int_line.append(single_int)
            int_line_list.append(int_line)
        return int_line_list


file_example = FileReader("Problem1-6-1Input.txt")
lenght = file_example.file_as_int_line_list()
