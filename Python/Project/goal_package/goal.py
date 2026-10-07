# Import
import time

def goal(way): # The function receives way from the specific path function the player uses to get to the goal.

    print("\nYou now have everything needed! Let's go!")
    time.sleep(1)

    if way == "lake":
        print("\n⛵............")
        time.sleep(1)
        print("...⛵.........")
        time.sleep(1)
        print("......⛵......")
        time.sleep(1)
        print(".........⛵...")
        time.sleep(1)
        print("............⛵")
        time.sleep(1)

    elif way == "desert":
        print("\n💧............")
        time.sleep(1)
        print("...💧.........")
        time.sleep(1)
        print("......💧......")
        time.sleep(1)
        print(".........💧...")
        time.sleep(1)
        print("............💧")
        time.sleep(1)

    elif way == "freezing_mountain":
        print("\n🧥............")
        time.sleep(1)
        print("...🧥.........")
        time.sleep(1)
        print("......🧥......")
        time.sleep(1)
        print(".........🧥...")
        time.sleep(1)
        print("............🧥")
        time.sleep(1)

    print("\nCongratulations! You got to Molitorreno!")
    print("\nThe message has been correctly delivered to the kingdom!\n")