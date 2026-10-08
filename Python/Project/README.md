# Karo's game project

# Game's idea:

Game genre: Role-playing game (RPG)

Story genre: Fantasy

Once the game is initiated, the player can select from a list of characters which one they want to choose to play the game. Each character has a bag of items, which affects the resources available to the player when beginning the game.

The character is a messenger who delivers information between different kingdoms. At the beginning of the game, the player is in Sustainable Town, which is the closest location to the kingdom Molitorreno, where they need to head to deliver a message.

From this town, there are only three possible paths to get to Molitorreno: the character can get to the kingdom by crossing a lake, a desert or a freezing mountain.

If the first path is chosen, the character will need a boat to cross the lake. This boat must be built by the character. To do so, they need to get wood from a local wooded area. However, Sustainable Town has very strict rules about deforestation. Therefore, for each tree the character cuts, they must plant two seeds.

The character needs to check their bag and see which items they have that can help them to complete this task. If they do have enough seeds, they can simply proceed to cut the trees and plant the seeds. However, in case they do not have enough seeds, they would need to go to the Trade-In Store located in the town to get some seeds by trading some of their belongings.

On the other hand, the character could also cross the desert. For this, they would need to prepare for the harsh weather conditions by stocking some water for the trip. Sustainable Town also has a well, which is taken care by a farmer that ensures that the land where the well is located is protected so that the water is not polluted and is safe to drink. The character can pump water from it. But they would need to pay the eco-fee the farmer charges to be able to fund all the costs related to maintaining the water quality. Again, in case the character does not have enough money, they would need to go to the Trade-In Store to trade some items for money.

Finally, if the character chooses to go through the freezing mountains, they will need to get proper clothing. They can buy these from the Second-Hand Store located in the town. Once again, if they do not have enough money to do so, they can go the Trade-In Store.

After choosing a path and obtaining the necessary items, the character simply needs to head towards the kingdom of Molitorreno using the correct path. Then, they will reach their destination and correctly deliver their message.

# Objective:

- The final goal is to reach the kingdom where the messenger has to deliver a message.
- In order to accomplish this, the character has three possible paths to reach the kingdom. However, each of these paths has an obstruction that the player needs to overcome.
- The character must use the objects they have in their bag to obtain new items that will help them overcome these obstructions and reach their destination.

# Operating principles:

## How to run the game:

1. The machine where you will run the game must have Python 3 installed.
    - Link to download and install it: https://www.python.org/downloads/
2. Download the game from https://github.com/karolynegomesdamota/Software-1.git
    - Download the repository: Code -> Download ZIP, OR
    - Clone the repository using Git.
3. Open the game using your preferred environment, such as VSCode, a terminal, etc.
4. Locate the file game.py and run it.
5. Play the game by following the instructions displayed and entering your commands when prompted.

## How the player interacts with the game:

- The game starts by asking the player's name.
- The player chooses a character.
    - Each character starts with different items in their bag.
- The main menu is then displayed:
    - The player navigates through menus using numbered commands.
    - If the player enters a non-existing command, or something other than a number, an error message is displayed and the player is asked to try again.
    - Different menu options lead the player to other different menus.
        - Each menu displays different options for taking different actions.
        - Different paths can be taken to accomplish the same result.
        - Certain actions require specific resources.
        - Resources can be checked, traded, and used to perform certain actions.
- Every action that changes the inventory is automatically saved. The player can continue a previously saved game from where they left off.

# Functionalities:

- Player name input and saving for future games
- Character selection
- Character class for easily creating additional characters
- Several paths to progress through the game from beginning to end
- Main game loop and menu navigation
- Inventory/item management
- Automatic saving of game progress with JSON
- Input validation
- Error handling
- Reading information from .txt files

# How the sustainable development perspective has been taken into account:

- The game incorporates sustainable development principles directly into the game story. Examples include:
    - If the player cuts down trees, they must plant twice the amount of seeds to replace the tres that were cut down.
    - There's a second-hand store in the game where the character can buy items. This encourages sustainable consumption by giving used items a purpose instead of buying new ones.
     - There's a well in the game that the character can use by paying a fee. Within the game, this fee is justified as a contribution towards the costs of maintaining the water in good condition.

# AI:

Version GPT-5.6 Luna of OpenAI's ChatGPT was used to support in the planning phase of this project. This consisted of me telling my whole story to AI and asking it to build a diagram showing how each of my ideas (steps in the game) connected to the next ones. The goal was to ensure there was no gap in logic.