
class Developer:
    def __init__(self, name, age, profile, salary):
        self.name = name
        self.age = age
        self.profile = profile
        self.salary = salary
        self.max_increase = self.calculate_max_increase()

    def calculate_max_increase(self):
        return self.salary * 0.1


    def salary_increase(self, increase_amount):
        if increase_amount > self.max_increase:
            return {"error": f"Max increase for person {self} is {self.max_increase}"}
        self.salary += increase_amount
        self.max_increase = self.calculate_max_increase()
        return {"msg": f"Increase {increase_amount} for person {self} done"}


class Junior(Developer):
    def __init__(self, name, age, department, salary, mentor=None, plan=None):
        super().__init__(name, age, department, salary)
        self.plan = plan
        self.mentor = mentor
        if mentor is not None:
            senior = [var_value for var_key, var_value in globals().items() if
                      isinstance(var_value, Senior) and var_value.name == mentor]
            if senior:
                if not senior[0].add_padavans(self.name):
                    print(senior[0])
                    self.mentor = None
            else:
                self.mentor = None


    def change_mentor(self, mentor):
        senior = [var_value for var_key, var_value in globals().items() if
                  isinstance(var_value, Senior) and var_value.name == mentor]
        if senior[0].add_padavans(self.name):
            self.mentor = mentor




class Senior(Developer):

    def __init__(self, name, age, department, salary, padavans=None):
        super().__init__(name, age, department, salary)
        self.padavans = list()
        if padavans is not None:
            self.padavans.extend(padavans)
            for var_name, var_value in globals().items():
                if isinstance(var_value, Junior) and var_value.name in padavans:
                    if self.add_padavans(self.name):
                        var_value.mentor = self.name


    def add_padavans(self, padavans):
        # print(self.padavans)
        if len(self.padavans) >= 2:
            print(f"Too many padavans for {self.name}")
            return False
        self.padavans.append(padavans)
        return True




# j = Junior('Nick', 22, 'dev', 1000)
# j2 = Junior('Nick2', 22, 'dev', 1000)
# j3 = Junior('Nick3', 22, 'dev', 1000)
# s2 = Senior('Cris', 30, 'super_dev', 5000)
# j4 = Junior('Nick4', 22, 'dev', 1000, 'Cris')
# s = Senior('Mike', 30, 'super_dev', 5000, ['Nick4'])
# j.change_mentor('Cris')
# j2.change_mentor('Cris')
# j3.change_mentor('Cris')
# j4.change_mentor('Cris')
# s2.add_padavans('Nick3')
# print(j.mentor)
# print(s.padavans)

