# Frida Kahlo

# initial data
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
dates = [1939, 1933, 1946, 1940]

# add more paintings to the list
paintings.append('The Broken Column')
paintings.append('The Wounded Deer')
paintings.append('Me and My Doll')

# include dates for the appended paintings above
dates.append(1944)
dates.append(1946)
dates.append(1937)

# find the number of paintings on our list
number_of_paintings = len(paintings)

# generate audio tour numbers
audio_tour_numbers = []
for num in range(number_of_paintings):
  audio_tour_numbers.append(num + 1)

# combine audio tour numbers, painting titles and dates into a single list
master_list = list(zip(audio_tour_numbers, paintings, dates))

# output
print('Featured Paintings by Frida Kahlo:')
print(master_list)