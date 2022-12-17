"""
The 3n+1 problem

print a sequence of numbers
"""

import file_reader as fr
import file_writer as fw



class Problem1:

    def __init__(self):
        self.modulo = 0
        self.count = 0
        self.longest_cycle = 0
        self.cycle_iter = 0


    def find_cycle(self, n):
        self.count = 1

        while n > 1:
            self.modulo = n % 2
            if self.modulo == 0:
                n = n/2
            else:
                n = ((3*n)+1)
            self.count += 1
        return self.count

    def solve(self):
        input_file = fr.FileReader("Problem1-6-1Input.txt")
        problem_set = input_file.file_as_int_line_list()
        return_string = ""
        
        for i in range(0, len(problem_set), 1):
            self.longest_cycle = 0
            self.cycle_iter = 0
            for j in range(problem_set[i][0], problem_set[i][1], 1):
                self.cycle_iter = self.find_cycle(j)
                if self.cycle_iter > self.longest_cycle:
                    self.longest_cycle = self.cycle_iter
            print(self.longest_cycle)
            return_string += str(problem_set[i][0]) + " " + str(problem_set[i][1]) + " " + str(self.longest_cycle) + "\n"
        print(return_string)
        return return_string

def execute_main():
    exe_problem1 = Problem1()
    answer = exe_problem1.solve()
    output_file = fw.FileWriter("PyProblem1-Output.txt")
    output_file._file_write_all_str(answer)
    

if __name__ == "__main__":
    execute_main()
