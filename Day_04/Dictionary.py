# creating a dictionary
country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Pakistan": "Islamabad",
}
print(country_capitals)
#Access Dictionary Items
print(country_capitals["USA"])

#Add Items to a Dictionary
country_capitals["Germany"] = "Berlin"
print(country_capitals)

#Remove Dictionary Items
del country_capitals["France"]
print(country_capitals)

#Change Dictionary Items
country_capitals["Japan"] = "Kyoto"
print(country_capitals)

#Iterate Through a Dictionary
for country in country_capitals:
    print(country)

## print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
# get dictionary's length
print(len(country_capitals))

#Dictionary Membership Test
file_test = {
    ".txt": "Text File",
    ".jpg": "JPEG Image",
    ".png": "PNG Image",
    ".pdf": "PDF Document", 
}
print(".txt" in file_test)  # True
print(".doc" in file_test)  # False
print(".pdf" not in file_test)  # False
print(".doc" not in file_test)  # True
print(".jpg" in file_test)  # True