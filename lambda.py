# %%
# Q1
lst = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
lst.sort(key=lambda x:x[1])
print(lst)

# %%
# Q2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(map(lambda x:x*x,numbers))
print(numbers)

# %%
# Q3
lst_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_strs = tuple(map(str,lst_ints))
print(lst_strs)

# %%
# Q4
import functools

lst = [i for i in range(1,26)]
functools.reduce(lambda a,b:a*b,lst)

# %%
# Q5

lst = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
filtered_lst = list(filter(lambda x:x%2==0 or x%3==0,lst))
print(filtered_lst)

# %%
# Q6
def isPalindrome(s):
    '''
        Check whether s is a palindrome or not.
        param  : s <- str
        return : bool
    '''
    for i in range(len(s)//2):
        if(s[i]!=s[len(s)-1-i]):
            return False
    return True


lst = ['python', 'php', 'aba', 'radar', 'level']
palindromes = list(filter(lambda x:isPalindrome(x),lst))
print(palindromes)

# %%
f = lambda x,y:x**y
f(4,5)

# %%



