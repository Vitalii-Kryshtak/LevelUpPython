import hw
import faker
import random

fake = faker.Faker()
senior_list = []
junior_list = []

def create_object_class(name_class: str, numbers_obj: int):
    pass

def create_senior(numbers_obj: int):
    for i in range(numbers_obj):
        senior_list.append(hw.Senior(fake.name(), 25, 'Python', 2000))


def create_junior(numbers_obj: int):
    for i in range(numbers_obj):
        junior_list.append(hw.Junior(fake.name(), 25, 'Python', 2000))


def add_junior_to_senior(seniors: list, juniors: list,  number_padavans: int):
    start = 0
    end = number_padavans
    for senior in seniors:
        senior.padavans = juniors[start : end]
        start += number_padavans
        end += number_padavans


def duplicate_juniors_to_seniors(seniors: list, juniors: list, attempts: int = 5):
    random.shuffle(seniors)
    for senior in seniors:
        print(f"_________{senior} try duplicate junior: ")
        for i in range(attempts):
            senior.padavans = random.choice(juniors)


if __name__ == "__main__":
    create_senior(4)
    create_junior(12)
    add_junior_to_senior(senior_list, junior_list, 3)
    duplicate_juniors_to_seniors(senior_list, junior_list)
