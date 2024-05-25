class Solution:
    def decodeString(self, s: str) -> str:
    
      sta = []
      OPEN='[';CLOSE=']'
      to_repeat = ''
      times=''
      for c in s : 
          if c != CLOSE :
            sta.append(c)  
          else:
            while sta and sta[-1] != OPEN:
               to_repeat = sta.pop() + to_repeat
            else: # top of stack is [, # remove the opening bracket [
               sta.pop()  
            while sta and sta[-1].isdigit() :
               times = sta.pop() + times 
            # print ('I will repeat ', to_repeat, ' ',times, 'times')
            sta.append(to_repeat*int(times))
            to_repeat = ''
            times = ''
      return ''.join(sta)