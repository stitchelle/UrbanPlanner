import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = "Michelle"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
    
    def construct(self):
        self.date_constructed = datetime.datetime.now().strftime("%m/%d/%Y")

    def purchase(self, name):
        self.owner = name

eight_hundred_eighth = Building("800 8th Street", 12)
three_zero_one = Building("301 Plus Park Dr.", 6)
three_three_two_two = Building("3322 Dizzy Dean Drive", 2)
three_one_four = Building("314 Upper Mill Drive", 2)
six_four_eight_zero = Building("6480 Deer Lick Road", 2)


eight_hundred_eighth.construct()
three_zero_one.construct()
three_three_two_two.construct()
three_one_four.construct()
six_four_eight_zero.construct()

eight_hundred_eighth.purchase("Robert")
three_zero_one.purchase("Robert")
three_three_two_two.purchase("Robert")
three_one_four.purchase("Robert")
six_four_eight_zero.purchase("Robert")

building_list = [eight_hundred_eighth, three_zero_one, three_three_two_two, six_four_eight_zero]

for list in building_list:
    print(f'{list.address} was purchased by {list.owner} on {list.date_constructed} and has {list.stories} stories.')
