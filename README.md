# pokemonbattlesim
A text based simulator game based on Nintendo's Game Franchise Pokemon and Linux text-based games such as "Trek"

Instructions:

1. When you first boot up the game, press "Enter" to proceed to next lines of dialogue
2. Once you reach the main menu, choose which sub-menu you want to enter using different integer inputs (1, 2, 3, 4)
3. From the sub-menu, proceed to use different integer inputs to perform an action
4. Your opponent will commence with their move after you finished with your action
5. The cycle will continue looping until every pokemon on one team all have 0 HP

When menu menu pops up, only input from these options given:
- Main Menu: 1, 2, 3, 4
- Move Menu: 1, 2, 0
  (Move Menu allows you to use your pokemon's moves such as Scratch or Tail Whip)
- Pokemon Menu: 1, 2, 0
  (Allows you to swap out you pokemon)
(The "0" input for both the Move Menu and Pokemon Menu returns you to the main menu)


Pokemon:
- Red (User):
  - Charmander -> Moves: Scratch, Growl
  - Bulbasaur -> Moves: Tackle, Growl
- Blue (Opponent):
  - Squirtle -> Moves: Tackle, Tail Whip

Moves:
- Scratch -> Lowers opponents HP based on calculations
- Tackle -> Lowers opponents HP based on calculations
- Growl -> Lowers opponents defense stat
- Tail Whip -> Lowers opponents attack stat

Things to take note:
- Please do not enter any input except the ones stated above, the data validation for the program has not been finished yet and it will definetly break if you enter something you're not supposed to >.<

WIP Information:
- I'm want to work on a new "combat update" that should make it easier to create and edit moves as compared to the current state of the program, hopefully I'll be able to finish it soon
- Super Effective is currently inactive in the program's current state, I will add it alongside the combat update above

Thank you and I hope you enjoy this game of mine! :D
