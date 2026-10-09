# Import
import time

# This function is informing the player they have everything needed to get to the kingdom.
# It displays a visual progression of the character moving.
# It informs the character they have reached their goal.

def goal(way): # The function receives way from the specific path function the player uses to get to the goal.

    print("\nYou now have everything needed! Let's go!")
    time.sleep(1)

    if way == "lake":
        for i in range(5):
            print("\n" + "." * (i * 3) + "⛵" + "." * (12 - i * 3))
            time.sleep(1)

    elif way == "desert":
        for i in range(5):
            print("\n" + "." * (i * 3) + "💧" + "." * (12 - i * 3))
            time.sleep(1)

    elif way == "freezing_mountain":
        for i in range(5):
            print("\n" + "." * (i * 3) + "🧥" + "." * (12 - i * 3))
            time.sleep(1)

    print("\nCongratulations! You got to Molitorreno!")
    time.sleep(1)
    print("\nThe message has been correctly delivered to the kingdom!\n")
    time.sleep(1)