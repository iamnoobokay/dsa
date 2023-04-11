from typing import List

def solution(morsecode: str) -> List[str]:
    # write your solution here
    morseCode = morsecode
    morseCodeArr = list(morsecode)
    ans = []
    for i,m in enumerate(morseCodeArr):
        newArr = morseCodeArr
        j = i + 1
        if i == len(morseCodeArr):
            break
        if j == len(morseCodeArr):
            break
        if (morseCodeArr[i] == morseCodeArr[j]):
            if(morseCodeArr[i] == '.'):
                newArr[i] = '-'
                newArr[j] = '-'
                if(''.join(newArr) == morsecode):
                    continue
                ans.append(''.join(newArr))
            if(morseCodeArr[j] == '-'):
                newArr[i] =  '.'
                newArr[j] = '.'
                if(''.join(newArr) == morsecode):
                    continue
                ans.append(''.join(newArr))
    print(ans)


# R E A D M E
# DO NOT CHANGE the code below, we use it to grade your submission. If changed your submission will be failed automatically.
# if __name__ == '__main__':  
#     a = input()
#     output = solution(a)
#     output.sort()
#     if output == []:
#         print('[]')
#     else:
#         print('["%s"]' % '","'.join(map(str, output)))

solution('-..-......')