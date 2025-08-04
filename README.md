# M.I.A-Tasks

### Code explanation of the first task

Firstly, I import the time library so I can use the delay function in the output
Then, I make the display_gear function which make the empty grid and put spaces between each row
Then, I have simulate the grid as a chars as follows: where a indicates top horizontal segment, b indicates top-right vertical segment, c indicates bottom-right vertical segment, d indicates bottom horizontal segment, bottom-left vertical segment, f indicates top-left vertical segment and g indicates middle horizontal segment
Then, I make a segment to light list which retrieves the list of segments for the given gear_number
Then, I have used the join function so convert each row into a string and can print it where if I don’t do this the output of the rows will be like this: ['#', '#', '#', ' ']
Then, I have made the animate range that takes the start gear and the end with a constant delay of about 0.5, If the user inputs the start gear smaller than the end (within the range) the step will be 1 else the step will be -1.
Then, I created a for loop that print the gear within the display range and apply the delay 0.5
Then, the while true to perform and endless loop until the user input the letter (q) and use the .split function to can read the input of the user that separated by a space


### Code explanation of the Second task
Firstly creating the encode function and I used (|||) as a separator to separate between the each string and change the list to a big string then send this string to decode function and separate between the substrings based on ||| separator
Then, create a function that takes the input from the user and create a terminator that I think that It will not be used, {I have a second approach to use (ctrl+z) as a terminator but I thought that the commander uses radio so no sense to use a command for laptops}.
Then, in the main function I handle that If the commander didn’t send any command if he didn’t send any thing (literally) then I print the outputs as mentioned in the example you gives me

### Code explanation of the Third task
##### Program Features
Object-Oriented Design: The program uses a Racer base class and derived classes (MaxVerstappen, HassanMostafa) to implement core OOP concepts like Inheritance, Encapsulation, and Polymorphism.
Turn-Based Gameplay: The race alternates turns between the two drivers, allowing players to strategically choose their moves.
Dynamic Moves: Offensive and defensive moves are defined with specific fuel costs, damage impacts, and, for some, a limited number of uses.
Input Validation: The program ensures user input is valid (e.g., a number from the list of available moves) to prevent errors.
Race Termination Logic: The simulation ends gracefully when a driver's tire health reaches zero or when both drivers are unable to perform any moves due to fuel depletion.

1. Class Design and OOP Principles
A. The Racer Class (Base Class)
The Racer class serves as the abstract blueprint for any driver in the simulation. It encapsulates all common attributes and methods, which are then inherited by the specific driver classes.
Attributes (Encapsulation):
name: The name of the driver (e.g., "Max Verstappen").
tire_health: An integer representing tire condition, initialized to 100.
fuel: An integer for the car's fuel level, initialized to 500.
offensive_moves: A dictionary to store the driver's offensive moves.
defensive_moves: A dictionary to store the driver's defensive tactics.

Key Methods:
__init__(self, name): The constructor that initializes the racer's name and starting stats.
_print_stats(self): A private helper method to display the racer's current stats.
apply_damage(self, damage): Reduces the tire_health.
use_fuel(self, fuel_cost): Reduces the fuel level.
take_turn(self, opponent): Manages the offensive phase of a turn. It prompts the user for a move, applies fuel costs, and calls the opponent's respond_to_attack method.
respond_to_attack(self, incoming_damage, opponent): Manages the defensive phase. It prompts the user for a defense, calculates the final damage after reduction, and applies it.\

B. Derived Classes (MaxVerstappen and HassanMostafa)
These classes inherit from the Racer base class, specializing it with each driver's unique moves and attributes. This is a clear use of inheritance.
MaxVerstappen(Racer):
Defines specific dictionaries for offensive_moves (DRS Boost, Red Bull Surge, Precision Turn) and defensive_moves (Brake Late, ERS Deployment).
It has a specific attribute, ers_deployment_uses, to track the uses of the "ERS Deployment" tactic.

HassanMostafa(Racer):
Defines its own unique moves, including offensive ones (Turbo Start, Mercedes Charge, Corner Mastery) and defensive ones (Slipstream Cut, Aggressive Block).
It has a specific attribute, agressive_block_uses, to track the single use of the "Aggressive Block" tactic.

2. Method Explanations
take_turn(self, opponent)
This method orchestrates a single offensive turn.
Fuel Check: It first uses a dictionary comprehension to filter self.offensive_moves, creating a new dictionary affordable_moves that only includes moves the racer has enough fuel for.
No Moves Condition: It checks if affordable_moves is empty. If so, it prints a message and returns False, indicating a skipped turn. This is crucial for preventing the infinite loop error.
User Input: It displays the affordable moves with numbers and uses _get_user_choice for validated numeric input.
Execute Move: It applies the fuel cost and passes the tire_impact to the opponent's respond_to_attack method.

respond_to_attack(self, incoming_damage, opponent)
This method handles the defensive response to an attack.
Filter Defenses: It creates a dictionary of available_defenses by filtering out any moves with zero uses or insufficient fuel. This ensures the user only sees valid choices.
No Defenses Condition: If there are no available defenses, it prints a message and applies the full incoming_damage.
Limited Uses: If a limited-use move is chosen, the code dynamically generates the attribute name (e.g., agressive_block_uses) and decrements its value using getattr and setattr.
Calculate Damage: It calculates the final_damage by applying the move's damage reduction percentage and then calls self.apply_damage.

3. The main() Function (Race Orchestration)
This function contains the primary logic for the simulation.
Instantiation: It creates the verstappen and mostafa objects.
Game Loop: The while loop controls the flow of the race. Its condition is:verstappen.tire_health > 0: The race continues as long as Verstappen has tire health.
mostafa.tire_health > 0: The race continues as long as Mostafa has tire health.
no_moves_in_a_row < 2: This is the key update to prevent an infinite loop. It ends the race if two consecutive turns (one for each driver) are skipped due to a lack of affordable moves.
Turn Switching: After each turn, the current_racer and opponent_racer variables are swapped using the Pythonic tuple unpacking syntax.

Winner Determination: Once the loop terminates, the program checks which condition ended the race (tire health or skipped turns) and declares the appropriate winner. If the race ended due to no moves, the winner is the racer with the most remaining tire health.
verstappen.tire_health > 0: The race continues as long as Verstappen has tire health.
mostafa.tire_health > 0: The race continues as long as Mostafa has tire health.
no_moves_in_a_row < 2: This is the key update to prevent an infinite loop. It ends the race if two consecutive turns (one for each driver) are skipped due to a lack of affordable moves.
Turn Switching: After each turn, the current_racer and opponent_racer variables are swapped using the Pythonic tuple unpacking syntax.

### The bouns of task 1.3: 
adding a voice command feature so now both Verstappen and Mostafa can play using their voices instead of just typing. I used the speech_recognition library with google’s free speech‑to‑text so it listens through the mic and then tries to match the spoken words with the available moves. if it doesn’t understand what the player said, it asks again or lets them type the move number as a fallback.
the function get_voice_command is the part that records from the mic, adjusts for background noise, sends it for transcription, and checks if the words match any move name. then in _get_user_choice, I made it so the game first tries listening for a move, and if that fails, the player can still type.
basically you just say something like “turbo start” or “drs boost” when it’s your turn, and the system will run that move. if it didn’t catch what you said, you just type the number.
Winner Determination: Once the loop terminates, the program checks which condition ended the race (tire health or skipped turns) and declares the appropriate winner. If the race ended due to no moves, the winner is the racer with the most remaining tire health.
