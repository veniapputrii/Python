#🐾 What is yield?
#Think of 'yield' like a bookmark in a book. When u use 'yield' in a function,
#it's like saying, "Pause here, remember this spot, and when you come back, pick up right where you left off"

#the example with a loop:
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(3):
   # First loop: It prints 3 and pauses.
   # Second loop: It continues, prints 2, and pauses again.
   # Third loop: It continues, prints 1, and then stops.
    print(number)
#it's like having a TV remote where you can pause and play whenever you want!

# 🐾 Why is yield useful?
# ✌️ Memory Efficient: If you have a huge amount of data, 
# like a million episodes (imagine if a show never ended!), 
# yield lets you handle them one at a time without using too much memory.

# ✌️ Lazy Evaluation: It only produces values when you need them. 
# So, if you only want the first 5 episodes, you don’t have to wait for all million episodes to load.