#Gillian Line-Luttrell
team={}
for i in range(5):
    jersey_num=int(input("Enter player %s's jersey number:\n" % str(i+1)))
    rating=int(input("Enter player %s's rating:\n" % str(i+1)))

    if jersey_num not in team:
        team[jersey_num]=rating
    print()

print("ROSTER")
for key,value in sorted(team.items()):
    print("Jersey number: %d, Rating: %d" % (key,value))

while True:
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')

    menu_choice=input('Choose an option:\n')
    menu_choice=menu_choice.lower()

    if menu_choice=='o':
        print("ROSTER")
        for key,value in sorted(team.items()):
            print("Jersey number:%d,Rating:%d" % (key,value))

    elif menu_choice=='a':

        jersey_num=int(input("Enter a new player jersey number:\n"))
        rating=int(input("Enter player's rating:\n"))

        if jersey_num not in team:
            team[jersey_num]=rating
        else:
            print("\nThe Player already in the list")

    elif menu_choice== 'd':

        jersey_num=int(input("\nEnter a jersey number:\n"))

        if jersey_num in team:
            del team[jersey_num]
        else:
            print("\nThe Player is not in the list")

    elif menu_choice== 'u':

        jersey_num=int(input("\nEnter a jersey number:\n"))

        if jersey_num in team:
            rating=int(input("\nEnter a new rating for the player:\n"))
            team[jersey_num]=rating
        else:
            print("\nThe Player is not in the list")

    elif menu_choice== 'r':


        rating=int(input("\nEnter a rating:\n"))

        for key,value in sorted(team.items()):

            if value > rating:
                print("Jersey number:%d,Rating:%d" % (key,value))

    elif menu_choice=='q':
        break

def print_menu():
   menu_option = ' '
   return menu_option

#def main_menu():
while(True):
    c = input()
    if(c=='a'):
        jersey_num=int(input("Enter a new player jersey number:\n"))
        rating=int(input("Enter player''s rating:\n"))

        if jersey_num not in team:
            team[jersey_num]=rating
        else:
            print("\nThe Player already in the list")
    elif(c=='o'):
        print("ROSTER")
        for key,value in sorted(team.items()):
            print("Jersey number:%d,Rating:%d" % (key,value))       
    elif(c=='d'):
        jersey_num=int(input("\nEnter a jersey number:\n"))

        if jersey_num in team:
            del team[jersey_num]
        else:
            print("\nThe Player is not in the list")
    elif(c=='u'):
        jersey_num=int(input("\nEnter a jersey number:\n"))

        if jersey_num in team:
            rating=int(input("\nEnter a new rating for the player:\n"))
            team[jersey_num]=rating
        else:
            print("\nThe Player is not in the list")            
    elif(c=='r'):
        rating=int(input("\nEnter a rating:\n"))

        for key,value in sorted(team.items()):
            if value > rating:
                print("Jersey number:%d,Rating:%d" % (key,value))
    elif(c=='q'):
        print()
        break
print()
print(print_menu())
#main_menu()
