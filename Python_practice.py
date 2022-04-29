print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())

# While loop:
x = 0
while x <= 5:
    print(x)
    x = x + 1

# For loop
for county in counties:
    print(county)

###
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

###
for num in range(5):
    print(num)

### for loop with indexing
for i in range(len(counties)):
    print(counties[i])

# Get the Keys of a Dictionary
for county in counties_dict:
    print(county)

###
for county in counties_dict.keys():
    print(county)

# Get the Values of a Dictionary
for voters in counties_dict.values():
    print(voters)

# Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

## Playing with votes
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

###
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

### Using f-strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

### Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

### Format Floating-Point Decimals
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

###
###
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
message_to_county = (
    f"county has {voters:,} registered voters.")
for county, voters in counties_dict.items():
    # print(county + " county has " + str(voters) + " registered voters.")
    print(county + " " + message_to_county)
