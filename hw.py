from typing import Union, List


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
            return {'error': f"Max increase for person {self} is {self.max_increase}"}
        self.salary += increase_amount
        self.max_increase = self.calculate_max_increase()
        return {'msg': f"Increase {increase_amount} for person {self} done"}


class Junior(Developer):
    def __init__(self, name, age, profile, salary, mentor=None, plan=None):
        super().__init__(name, age, profile, salary)
        self.mentor = mentor
        self.plan = plan

    def is_mentor_exist(self, new_mentor):
        if getattr(self, "_Junior__mentor", None):
            if new_mentor == self.__mentor:
                return True
        return False

    def only_add_mentor(self, new_mentor: "Senior"):
        self.check_object_class(new_mentor, Senior)
        self.__mentor = new_mentor

    @staticmethod
    def check_object_class(obj, class_to_check):
        if obj and not isinstance(obj, class_to_check):
            raise ValueError(
                f"padavan must be instance of {Senior} not {type(obj)}"
            )

    @property  # if mentor is GETTER => @mentor.setter, @mentor.deleter
    def mentor(self):
        print(f"My mentor is {self.__mentor}")
        return self.__mentor

    @mentor.setter
    def mentor(self, new_mentor: "Senior"):
        self.only_add_mentor(new_mentor)
        if new_mentor and not self.is_mentor_exist(new_mentor):
            new_mentor.padavans = self

    # @mentor.setter
    # def mentor(self, new_mentor: "Senior"):
    #     self.check_object_class(new_mentor, Senior)
    #
    #     if new_mentor and not self.is_mentor_exist(new_mentor):
    #         new_mentor.padavans = self
    #
    #     self.__mentor = new_mentor

    @mentor.deleter
    def mentor(self):
        print(f"{self} delete mentor: {self.__mentor}")
        try:
            self.__mentor.padavans.remove(self) # Senior.padavans.remove(self)
        except ValueError:
            print(f"No such: {self} Padavan in mentor: {self.__mentor}")
        self.__mentor = None



        # Todo: Implement process of deleting this Junior from Senior padavans


class Padavans(list):

    """
    Override list
    """
    def __init__(self, *args, ** kwargs):
        super(Padavans, self).__init__(*args, **kwargs)

    def remove(self, value: Junior) -> None:
        print(f"Removing Padavan {value} from list")
        super(Padavans, self).remove(value)
        print(f"removing Mentor {self} from Padavan Instance")
        del value.mentor

class Senior(Developer):
    def __init__(self, name, age, profile, salary, padavans=None, max_count_padavans=3):
        super().__init__(name, age, profile, salary)
        self.__padavans = Padavans()
        self.padavans = padavans
        self.max_count_padavans = max_count_padavans

    @property
    def padavans(self):
        print(f"{self} has padavans {self.__padavans}")
        return self.__padavans

    @padavans.setter
    def padavans(self, padavan: Union[Junior, List[Junior]]):
        padavans = []
        if isinstance(padavan, list):
            padavans.extend(padavan) # list
        elif padavan:
            padavans.append(padavan)

        if not all([isinstance(obj, Junior) for obj in padavans]):
            raise ValueError(f"padavan must be instance of {Junior} not {padavan}")

        for padavan in padavans:
            # if len(self.__padavans) >= self.max_count_padavans:
            #     raise ValueError(f"{self} has the maximum allowed number of padavans")

            if padavan and padavan not in self.__padavans:
                self.__padavans.append(padavan)
                padavan.only_add_mentor(self)
            else:
                print(f"{padavan} already a padavan and can't be added to {self}")


# s = Senior("Bob", 18, "Python", 2800.0)
# j1 = Junior("Fill", 19, "Python", 900)
# j2 = Junior("Mary", 22, "Python", 900)


