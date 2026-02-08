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

