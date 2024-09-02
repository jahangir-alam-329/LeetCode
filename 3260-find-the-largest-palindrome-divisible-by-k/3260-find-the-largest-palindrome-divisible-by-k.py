class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1 or k == 3 or k == 9:
            a = "9" * n
            return a
        elif k == 2:
            if n <= 2:
                a = "8" * n
                return a
            else:
                a = "8" + "9" * (n - 2) + "8"
                return a
        elif k == 4:
            if n <= 4:
                a = "8" * n
                return a
            else:
                a = "88" + "9" * (n - 4) + "88"
                return a
        elif k == 5:
            if n <= 2:
                a = "5" * n
                return a
            else:
                a = "5" + "9" * (n - 2) + "5"
                return a
        elif k == 8:
            if n <= 6:
                a = "8" * n
                return a
            else:
                a = "888" + "9" * (n - 6) + "888"
                return a

        elif k == 6:
            if n == 1 or n == 2:
                a = "6" * n
                return a
            elif n == 3:
                a = "888"
                return a
            elif n >= 4:
                if n % 2 == 0:
                    a = "8" + "9" * ((n - 4) // 2) + "77" + "9" * ((n - 4) // 2) + "8"
                    return a
                else:
                    a = "89" + "9" * ((n - 5) // 2) + "8" + "9" * ((n - 5) // 2) + "98"
                    return a

        elif k == 7:
            dic = {
                0: "",
                1: "7",
                2: "77",
                3: "959",
                4: "9779",
                5: "99799",
                6: "999999",
                7: "9994999",
                8: "99944999",
                9: "999969999",
                10: "9999449999",
                11: "99999499999",
            }
            quetient, remainder = divmod(n, 12)
            return '999999' * quetient + dic[remainder] + '999999' * quetient

        #     return largest[li]

        # elif(n==3):
        #     for i in range(100,1000):
        #         if (i%k==0):
        #             l=str(i)
        #             b=l[::-1]
        #             if (b==l):
        #                 largest.append(l)
        #     li=len(largest)-1
        #     return largest[li]

        # elif(n==4):
        #     for i in range(1000,10000):
        #         if (i%k==0):
        #             l=str(i)
        #             b=l[::-1]
        #             if (b==l):
        #                 largest.append(l)
        #     li=len(largest)-1
        #     return largest[li]

        # elif(n==5):
        #     for i in range(10000,100000):
        #         if (i%k==0):
        #             l=str(i)
        #             b=l[::-1]
        #             if (b==l):
        #                 largest.append(l)
        #     li=len(largest)-1
        #     return largest[li]

        # elif(n==6):
        #     for i in range(100000,1000000):
        #         if (i%k==0):
        #             l=str(i)
        #             b=l[::-1]
        #             if (b==l):
        #                 largest.append(l)
        #     li=len(largest)-1
        #     return largest[li]

        # elif(n==7):
        #     for i in range(1000000,10000000):
        #         if (i%k==0):
        #             l=str(i)
        #             b=l[::-1]
        #             if (b==l):
        #                 largest.append(l)
        #     li=len(largest)-1
        #     return largest[li]

        # elif(n==8):
        #     if(k==1 or k==3 or k==9):
        #         a1="99999999"
        #         return a1
        #     elif(k==2):
        #         a1="89999998"
        #         return a1
        #     elif(k==4):
        #         a1="88999988"
        #         return a1
        #     elif(k==5):
        #         a1="59999995"
        #         return a1
        #     elif(k==6):
        #         a1="89977998"
        #         return a1
        #     elif(k==7):
        #         a1="99944999"
        #         return a1
        #     elif(k==8):
        #         a1="88899888"
        #         return a1

        # elif(n==9):
        #     if(k==1 or k==3 or k==9):
        #         a1="999999999"
        #         return a1
        #     elif(k==2):
        #         a1="899999998"
        #         return a1
        #     elif(k==4):
        #         a1="889999988"
        #         return a1
        #     elif(k==5):
        #         a1="599999995"
        #         return a1
        #     elif(k==6):
        #         a1="899989998"
        #         return a1
        #     elif(k==7):
        #         a1="999969999"
        #         return a1
        #     elif(k==8):
        #         a1="888999888"
        #         return a1
        # elif(n==10):
        #         a1="9999999999"
        #         return a1


#  in this approach time exceeds


#         largest=0
#         sum=0
#         second_largest=0
#         if(n==1):
#             for i in range(1,10):
#                 if (i%k==0):
#                     q=i
#                     l=len(str(i))
#                     for j in range(0,l):
#                         r=q%10
#                         sum=(sum*10)+r
#                         q=q//10
#                     if (sum==i):
#                         largest=sum
#                         sum=0
#                     else:
#                         sum=0
#             return str(largest)

#         elif(n==2):
#             for i in range(10,100):
#                 if (i%k==0):
#                     q=i
#                     l=len(str(i))
#                     for j in range(0,l):
#                         r=q%10
#                         sum=(sum*10)+r
#                         q=q//10
#                     if (sum==i):
#                         largest=sum
#                         sum=0
#                     else:
#                         sum=0
#             return str(largest)

#         elif(n==3):
#             for i in range(100,1000):
#                 if (i%k==0):
#                     q=i
#                     l=len(str(i))
#                     for j in range(0,l):
#                         r=q%10
#                         sum=(sum*10)+r
#                         q=q//10
#                     if (sum==i):
#                         largest=sum
#                         sum=0
#                     else:
#                         sum=0
#             return str(largest)

#         elif(n==4):
#             for i in range(1000,10000):
#                 if (i%k==0):
#                     q=i
#                     l=len(str(i))
#                     for j in range(0,l):
#                         r=q%10
#                         sum=(sum*10)+r
#                         q=q//10
#                     if (sum==i):
#                         largest=sum
#                         sum=0
#                     else:
#                         sum=0
#             return str(largest)

#         elif(n==5):
#             for i in range(10000,100000):
#                 if (i%k==0):
#                     q=i
#                     l=len(str(i))
#                     for j in range(0,l):
#                         r=q%10
#                         sum=(sum*10)+r
#                         q=q//10
#                     if (sum==i):
#                         largest=sum
#                         sum=0
#                     else:
#                         sum=0
#             return str(largest)

#         elif(n==6):
#             for i in range(100000,1000000):
#                 if (i%k==0):
#                     q=i
#                     l=len(str(i))
#                     for j in range(0,l):
#                         r=q%10
#                         sum=(sum*10)+r
#                         q=q//10
#                     if (sum==i):
#                         largest=sum
#                         sum=0
#                     else:
#                         sum=0
#             return str(largest)

#         else:
#             for i in range(1000000,10000000):
#                 if (i%k==0):
#                     q=i
#                     l=len(str(i))
#                     for j in range(0,l):
#                         r=q%10
#                         sum=(sum*10)+r
#                         q=q//10
#                     if (sum==i):
#                         largest=sum
#                         sum=0
#                     else:
#                         sum=0
#             return str(largest)
