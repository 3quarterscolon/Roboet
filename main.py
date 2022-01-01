from random import choice

####
d = 2 # do not change
n = 500
start = "According to all known"
####

with open("script.txt") as f:
  poems = f.readlines()
  for i, item in enumerate(poems): poems[i] = item.split()

patterns = {}
for poem in poems:
  #print(poem)
  for i, _ in enumerate(poem):
    try:
      key = ' '.join([poem[i + item] for item in range(d)])
      if not key in patterns.keys():
        patterns[key] = [poem[i + d]]
      else:
        patterns[key].append(poem[i + d])
    except: break
#print(patterns)

generated = start.split()
try:
	for i in range(n):
		generated.append(choice(patterns[" ".join(generated[-d:])])) # temporary solution while I figure out how to make this work for variable values of d
except: pass
print(" ".join(generated))
