```markdown
# Higher or Lower Game

This is a simple terminal-based "Higher or Lower" game written in Python. The game tests your ability to guess which celebrity or public figure has more followers on social media. You will be presented with two choices, and your task is to pick the one with a higher follower count.

## Features
- Presents two choices (A and B) to the player, displaying the name, description, and country of each celebrity.
- The player guesses which celebrity has more followers by typing "A" or "B."
- The game tracks your score, and it continues until you make a wrong guess.
  
## How to Play
1. Run the game, and you will be shown two public figures to compare.
2. Each choice will display:
   - Name
   - Short description
   - Country
3. Guess which one has the higher follower count by typing either:
   - `"A"` for the first option
   - `"B"` for the second option
4. If you are correct, your score increases by 1, and the game continues with the next comparison.
5. The game ends when you guess wrong, and your final score is displayed.

## How to Run

To play the game, follow these steps:

1. Ensure you have Python installed on your system.
2. Download or clone the repository.
3. Run the `higher_lower.py` script in your terminal:
   ```bash
   python higher_lower.py
   ```

## Dependencies
- The game relies on an ASCII art file (`Art.py`) to display the game logos.
- The dataset for celebrities and their follower counts is stored in `day_14.py`. Ensure both files are included in your project.

## Functions

### `high_low()`
Displays the two choices (A and B) for the player to compare, showing their name, description, and country.

### `compar(a, b)`
Compares the follower counts of the two choices and returns "A" or "B" depending on which has more followers.

## Example Gameplay
```bash
Compare A: Beyoncé, Musician, USA
   vs
Against B: Lionel Messi, Footballer, Argentina

Who has more followers? Type 'A' or 'B': A

You're right! Your score is 1.

Compare A: Lionel Messi, Footballer, Argentina
   vs
Against B: Cristiano Ronaldo, Footballer, Portugal

Who has more followers? Type 'A' or 'B': B

You're right! Your score is 2.
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to adjust it to fit your game. Let me know if you'd like any additional sections or modifications!