a = {
    "Donald Trump" : "USA",
    "Narendra Modi" : "India",
    "Vladimir Putin" : "Russia",
    "Benjamin Netanyahu" : "Israel"
}

print(a.items()) # Will give all the items of dict as item
print(a.keys()) # Will give all the items on the left of colon as output
print(a.values()) # Will give all the items on the right of colon as output
a.update({"Donald Trump" : "Iran", "Xi Jinping" : "China"})
# The above method will update the original dict by adding one and updating other
print(a)
print(a.get("Narendra Modi")) # Will give the value if its present
print(a.get("Emmanuel Macron")) # Will give "None" as its not present in the dictionary
'''Difference between a.get() & a.[], well a.get() gives none when the specific key not present in dict,
where as a.[] gives error'''

b = len(a)
print(b)

