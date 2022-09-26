"""
4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
"Python", "Django"}

"""

thisset = {"Java","Python","Django"}
set = {"Python",}
# 1 Way 
if "Python" in thisset:
  print("Yes")
else:
  print("No")

# 2 Way
"""
thisset = {"Java","Python","Django"}
set = {"Pyton"}
ans = set.issubset(thisset)
print(ans) #True
"""
# 3 Way
"""
thisset = {"Java","Python","Django"}
set = {"Python",}
ans = thisset.issuperset(set)
print(ans) #True
"""