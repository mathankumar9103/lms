inp = "wellington was a poodle not one of the small poodles that have hairstyles but a big poodle"
new_str = ''
split_text = inp.split(" ")
for itr in split_text:
    new_str = new_str + itr.capitalize() + ' '
print(new_str)