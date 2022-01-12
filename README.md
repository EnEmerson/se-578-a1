# se-578-a1
Assignment 1 for SE-578

"There should be one file named README.txt explaining which file contains what part of the
assignment and explaining the procedure to build your code. It should only be a .txt format. No
other format is acceptable."

This is that file.

---

### Instructions:

1. `Q1.py` is the tool I used to solve this cipher. 
   1. It approximates the letters in the substitution cipher based on letter frequency analysis, as mentioned in section 2.3.2 in Information Security by Mark Stamp.
   2. The user can then manually try substitutions based on their visual analysis and intuition of the partially decoded message.
2. To try the solver yourself, open the python file into IntelliJ, VS Code, or any other IDE and right click -> run, or simply run the file from your command line with the usual `python Q1.py` command
3. To make it fun - try to guess the cipher in the fewest swaps possible!

---

### Key:
This is what I think the key is after much trial and error:

| Alphabet      | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
|---------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Substitutions | K   | F   | A   | Z   | S   | R   | O   | B   | C   | W   | D   | I   | N   | U   | E   | L   | T   | H   | Q   | G   | X   | V   | P   | ?   | M   | ?   |

#### J and Y were not used in the encoded message, so it's a 50/50 whether they're assigned to X or Z.

### Solution:
Therefore, this is what the plaintext of the cipher would look like after decoding (with some adjustments):

```
	the united states was at peace with that nation and at the solicitation of japan was still in 
	conversation with its government and its emperor looking toward the maintenance of peace in 
	the pacific indeed one hour after japanese air squadrons had commenced bombing in oahu the japanese 
	ambassador to the united states and his colleague delivered to the secretary of state a formal 
	reply to a recent american message while this reply stated that it seemed useless to continue 
	the existing diplomatic negotiations it contained no threat or hint of war or armed attack
```
