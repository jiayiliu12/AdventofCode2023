import re

path = 'C:/Users/jiayi/OneDrive/ETH/Rest/AdventofCode2023/1st/input.txt'
print(path)

def reverse(x):
  return x[::-1]

firstnums = []
lastnums = []
finalnumlist = []
with open(path, 'r') as f:
   for count, line in enumerate(f):
      print("##################################", "count: ", count, "line: ", line)
      # get first number in line
      matchfirst = re.search(r'\d', line)
      firstnums.append(matchfirst.group())
      print("firstnums[count]: ", firstnums[count]) 
      # reverse the line to use search command for last num
      reversedLine = reverse(line)
      print("reversedLine: ", reversedLine)  
      # get last number
      matchlast = re.search(r'\d', reversedLine)
      lastnums.append(matchlast.group())
      print("lastnums[count]: ", lastnums[count]) 
      # put first and last digit together into finalnumlist
      finalnumlist.append(int(str(matchfirst.group()) + str(matchlast.group())))
      print("finalnumlist[count]", finalnumlist[count])


totalsum = 0
totalsum = sum(finalnumlist)
print(totalsum)
