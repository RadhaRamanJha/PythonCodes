class coustom_list():
    """Class to calculate maximum, minimum, sum, average"""
    def __init__(self,number_list):
        self.number_list = number_list
    def list_sum (self):
        return(sum(self.number_list))

    def list_avg (self):
        sum_of_list = sum(self.number_list)
        count = len(self.number_list)
        return(sum_of_list/count)

    def min_of_list(self):
        return(min(self.number_list))

    def max_of_list(self):
        return(max(self.number_list))

natural_numbers = [natural_number in range(1,10000,2)]
cl = coustom_list(natural_number)
print(cl.max_of_list())
print(cl.min_of_list())
print(cl.list_sum())
print(cl.list_avg())