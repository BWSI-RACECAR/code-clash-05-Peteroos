"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #5 - Frequency of Word (wordfreq.py)


Author: Carter Berlind

Difficulty Level: 2/10

Prompt: Bobby is friendly and looking for things that say hi to him. He even looks for 
it in other words. Create a program that, when given a string as input, then reports 
how many times “hi” appears either on its own or within a word.

Constraints: Hi should be found regardless of case. The letters must be directly next to each other.

Test Cases:
Input: “Look behind you!”;                  Output: 1
Input: “what word are you looking for”;     Output: 0
Input: “This should be fun”;                Output: 1
Input: “his job is to make people laugh”;   Output: 1
Input: “How high can his white dog hike”;   Output: 4
"""

class Solution:
    def hi_finder(self, hi_string):
     
        hi_number = 0
        for i in range(len(hi_string)-1):
            if hi_string[i] == 'h' or hi_string[i] == 'H' :
                if hi_string[i+1] == 'i' or hi_string[i+1] == 'I'：
                    hi_number +=1
                
                else:
                    pass
            else:
                pass
        return hi_number


        # type hi_string: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        pass

def main():
    string1 = input()

    tc1 = Solution()
    ans = tc1.hi_finder(string1)
    print(ans)

if __name__ == "__main__":
    main()
