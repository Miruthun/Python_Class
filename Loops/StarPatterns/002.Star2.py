# Hollow Square Pattern 

# * * * * * 
# *       *
# *       *
# *       * 
# * * * * *


"""
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i ==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        
    print()
"""

# * * * * * *
# *         *
# *         * 
# * * * * * *

"""
rows = 4
columns = 6
for i in range(1,rows+1):
    for j in range(1, columns+1):
        if i==1 or i==rows or j==1 or j==columns:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()
"""

# *
# * *
# *   *
# *     * 
# * * * * *

"""
rows = 5
for i in range(1, rows+1):
    for j in range(1,i+1):
        if j==1 or i==rows or i==j:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    
    print()
"""
#     *
#   * * *
# * * * * * 

"""
rows =5

for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    
    for k in range(1,2*i):
        print("*", end=" ")

    print()
"""

# * * * * * 
#   * * * 
#     *


#     *
#   * * *
# * * * * * 
#   * * * 
#     *

#     *
#   *   *
# *       * 
#   *   * 
#     *

# A A A A A
#   B B B 
#     C



#  *         *
#  * *     * * 
#  * * * * * *
#  * *     * *
#  *         *
