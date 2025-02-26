# Frida Kahlo

# raw data
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
dates = [1939, 1933, 1946, 1940]

# combine painting names and dates into a 2D list
paintings = list(zip(paintings, dates))

# add more paintings to the list
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))

# output
print(paintings)