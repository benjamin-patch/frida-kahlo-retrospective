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

# find the number of paintings on our list
number_of_paintings = len(paintings)

# generate audio tour numbers
audio_tour_numbers = []
for num in range(number_of_paintings):
  audio_tour_numbers.append(num + 1)

# output
print('Audio Tour Numbers:')
print(audio_tour_numbers)

print('Painting Titles and Dates:')
print(paintings)