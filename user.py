

class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
            print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member)

    def enroll(self):
        self.gold_card_points = 200
        if self.is_rewards_member == False:
                self.is_rewards_member = True
        else:
            print("User already a member")
            return self.is_rewards_member == False
        print(self.is_rewards_member, self.gold_card_points)

    def spend_points(self, amount):
        self.gold_card_points = 200
        self.gold_card_points = self.gold_card_points - (amount)
        if amount > self.gold_card_points:
            print("Not enough points")
        else:
            print(self.gold_card_points)



allen = user("Allen", "Wyatt", "wyattallen@dojo.com", "27")
brandon = user("Brandon", "James", "jamesb@dojo.com", "28")

# allen.display_info()
# brandon.display_info()

# allen.enroll()
# brandon.enroll()

allen.spend_points(50)
brandon.enroll()
brandon.spend_points(80)
allen.display_info()
brandon.display_info()