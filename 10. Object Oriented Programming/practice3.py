# 小型練習題: 寵物管理系統(基礎版)
# 建立一個Pet類別，讓使用者可以建立不同的寵物(例如狗、貓、兔子)，並能夠:
# 1. 儲存寵物的基本資訊(名字、種類、年齡)。
# 2. 透過 __str__()把寵物的資訊轉成好看的文字，方便印出。

import textwrap

class Pet:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return textwrap.dedent(f"""\
        名字:{self.name}
        種類:{self.breed}
        年齡:{self.age}
        """)

# 進階題目1:
# 新增「寵物清單」類別
#   --> 建立一個PetManager類別，裡面有一pets清單。
#   --> 該清單會存放很多Pet物件。
class PetManager:
    def __init__(self):
        self.pets = []

# 進階題目2: 
# 增加「新增寵物」功能
    def add_pet(self, name, breed, age):
        new_pet = Pet(name, breed, age)
        self.pets.append(new_pet)

# 進階題目3:
# 增加「查詢所有寵物」功能
    def list_pets(self):
        print(f"印出寵物清單:\n{"-" * 30}")
        for pet in self.pets:
            print(pet)

# 進階題目4:
# 增加「依名字搜尋寵物」功能
    def find_pet(self, name):
        for pet in self.pets:
            if pet.name == name:
                print("找到寵物:")
                return pet
        print("沒找到寵物!")
        return None
    
# 進階題目5:
# 增加「計算總共有幾隻寵物」功能
    def count_pets(self):
        return len(self.pets)

# 進階額外挑戰1:
# 增加「刪除寵物」功能，輸入名字，刪掉該寵物
    def remove_pet(self, name):
        for pet in self.pets:
            if pet.name == name:
                self.pets.remove(pet)
                print(f"移除{pet.name}")
                return True
        return False

# 進階額外挑戰2:
# 增加「只印出某種類的寵物」，例如只列出所有貓咪
    def list_pets_by_breed(self, breed):
        print(f"列出breed為{breed}的寵物:")
        for pet in self.pets:
            if pet.breed == breed:
                print(pet)
        return None

# test
my_pet_manager = PetManager()

p1 = my_pet_manager.add_pet("小黑", "狗", 5)
p2 = my_pet_manager.add_pet("咪咪", "貓", 3)
p3 = my_pet_manager.add_pet("小白", "兔", 1)

my_pet_manager.list_pets()

p4 = my_pet_manager.add_pet("小S", "蛇", 2)
p5 = my_pet_manager.add_pet("喵喵", "貓", 10)
p6 = my_pet_manager.add_pet("姆姆", "貓", 7)
p7 = my_pet_manager.add_pet("來福", "狗", 2)

my_pet_manager.list_pets()

print(my_pet_manager.find_pet("咪咪"))

print(f"目前總共有{my_pet_manager.count_pets()}隻寵物")

my_pet_manager.remove_pet("小黑")

my_pet_manager.list_pets()

print(f"目前總共有{my_pet_manager.count_pets()}隻寵物")

my_pet_manager.list_pets_by_breed("貓")