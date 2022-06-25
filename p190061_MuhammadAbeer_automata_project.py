#!/usr/bin/env python
# coding: utf-8

# # TURING MACHINE 

# ### Language
# 
# {a^n b^m c^k|n>=1,m=n+1,k=m+1}

# ### Descriptive Definition:
# 
# Any number of a’s followed by  number of b’s and then followed by  number of c’s where number of a’s is less than number of b’s which is less less than number of c's
# 
# Words:
# {abbccc,aabbbcccc,aaabbbbccccc,aaaabbbbbcccccc,aaaaabbbbbbccccccc,aaaaaabbbbbbbcccccccc,aaaaaaabbbbbbbbccccccccc,aaaaaaaabbbbbbbbbcccccccccc, aaaaaaaaabbbbbbbbbbccccccccccc,aaaaaaaaaabbbbbbbbbbbcccccccccccc,…..}
# 

# In[26]:


string = input("Enter word: ")
length = len(string) + 2
tape = ['*']*length
i = 1
tapehead = 1
#loop to place characters of word in machine's tape
for s in string: 
    tape[i] = s
    i += 1

state = 0

X, Y, Z, S, B, R, L = 'X', 'Y', 'Z', 'S', '*', 'R', 'L' 
oldtapehead = -1
accept = False

def action(input_char, replace_with, move, new_state):
    global tapehead, state
    if tape[tapehead] == input_char:
        tape[tapehead] = replace_with
        state = new_state
        if move == 'L':
            tapehead -= 1
            return True
        elif move == 'R':
            tapehead += 1
            return True
    return False
#if tapehead is static then terminate Turing machine
while(oldtapehead != tapehead): 
    oldtapehead = tapehead
    print(tape , "with tapehead at index", tapehead, "on state" , state)
    
    if state == 0:
        if action('a', X, R, 1) or action(Y, Y, R, 4) or action(X, X, R, 1):
            pass
        
    elif state == 1:
        if action('b', Y, R, 2) or action(X, X, R, 1) or action(Y, Y, R, 1) or action('a', 'a', R, 1):
            pass
        
    elif state == 2:
        if action('c', Z, L, 3) or action('b', 'b', R, 2) or action(Z, Z, R, 2):
            pass
            
    elif state == 3:
        if action('a', 'a', L, 3) or action('b', 'b', L, 3) or action(Y, Y, L, 3) or action(Z, Z, L, 3) or action(X, X, R, 0):
            pass
    
    elif state == 4:
        if action(X, X, R, 4) or action(Z, Z, R, 5) or action(Y, Y, R, 4) or action('b', Y, R, 2):
            pass
        
    elif state == 5:
        if action('c', Z, L, 3) or action(Z, Z, R, 5) or action(B, B, R, 6):
            pass
            
    elif state == 6:
       
        accept = True

    else:
        accept = True
        
print("\nAfter Computation of Turing Machine we conclude that \n")            
if accept:
    print("Word is accepted on state = ", state)
else:
    print("Word is not accepted on state = ", state)


# In[ ]:





# In[ ]:




