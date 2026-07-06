def modify_str(x):
    new=x
    new += "I love Python"
    return new

x="Hello"

res=modify_str(x)

print("Original string:", x)
print("Modified string:", res)