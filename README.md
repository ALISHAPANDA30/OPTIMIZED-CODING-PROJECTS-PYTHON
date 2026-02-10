#STRING METHODS
#HERE WE WILL LEARN STRINGS FROM BASIC TO ADVANCE
s = "hello python"
#OPERATORS THAT CAN BE USED DIRECTLY ON STRINGS
print("------1.CONCATENATION-------")
print("hello" + "world")
print("-----2.MEMBERSHIP OPERATOR-----")
print("li" in "alisha")
print("li" not in "alisha")
print("------3.REPETITION----------")
print("hello"*3)
print("-------4.indexing---------")
print("alisha"[2])
print("-------5.slicing--------".upper())
print("alisha"[0:2])
print("-------6.length---------".upper())
print(len("alisha"))

#CASE CHANGING
print("-------case changing-----------".upper())
s = "PyThOn Is FuN"
print(s.upper())       # "PYTHON IS FUN"
print(s.lower())       # "python is fun"
print(s.title())       # "Python Is Fun"
print(s.capitalize())  # "Python is fun"
print(s.swapcase())    # "pYtHoN iS fUn"

print("-------HANDLING WHITESPACES--------")
text = "   hello world   \n"
print(text.strip())    # "hello world"          (removes left + right whitespace)
print(text.lstrip())   # "hello world   \n"
print(text.rstrip())   # "   hello world"

print("-------FINDING AND COUNTING---------")
p = "hey i am alisha"
print(p.find("alisha"))
print(p.count("a"))
print(p.index("a"))
print(p.startswith("hey"))

print("------SPLITTING AND JOINING--------")
print("split converts into list")
print("i love python".split())
print("-".join("i love python"))

print("-----REPLACE--------")
msg = "I like Java. Java is good."
print(msg.replace("Java", "Python"))   # I like Python. Python is good.

print("------CHECKING TYPE OF CONTENT--------")
print("123".isdigit())      # True
print("abc".isalpha())      # True
print("abc123".isalnum()) # True
print("  ".isspace())       # True
print("Alisha".istitle())   # True
print("hello".islower())    # True


print("ADVANCED LIST COMPREHENSION METHOD")
result = [char.upper() for char in "hello"]
# → ['H', 'E', 'L', 'L', 'O']

Placement,What methods?,When to use? / Examples,Why?
Before 'for' (prepares the loop input),"split(), strip() (on whole string), replace() (on whole if global change first), list() (to turn string into char list)","- When you need to break/clean the string first to loop properly.
- E.g., [word.upper() for word in sentence.split()] → split() before 'for' to loop over words.
- E.g., [c for c in sentence.strip()] → strip() removes outer spaces before looping chars.","Creates the sequence (e.g., words/chars) — without this, 'for' has nothing good to loop on. Use when input needs global prep (e.g., dirty sentence)."
After 'for' (in the expression – acts on each item),"upper()/lower()/title()/capitalize(), replace() (on each), strip() (on each word), startswith()/endswith(), isdigit()/isalpha() (for checks)","- When you transform/filter per item (word/char).
- E.g., [word.upper() for word in words] → upper() after 'for' on each word.
- E.g., [word.strip("","") for word in csv_data.split("","")] → strip() cleans each piece.","Applies to one item at a time — efficient for per-word/char changes. Use when loop is set, but items need individual tweaks."

