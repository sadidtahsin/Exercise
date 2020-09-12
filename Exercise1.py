def rec_sum(x):
    if x==5:
        return 5
    
    return x+recursion_sum(x+1)


print(rec_sum(1))

#EXPLAIN
# fuction call      return                              state  
#    rec_sum(1)     1+rec_sum(2)       pause state, wait for rec_sum(2) to calculate
#    rec_sum(2)     2+rec_sum(3)       pause state, wait for rec_sum(3) to calculate
#    rec_sum(3)     3+rec_sum(4)       pause state, wait for rec_sum(4) to calculate
#    rec_sum(4)     4+rec_sum(5)       pause state, wait for rec_sum(5) to calculate
#    rec_sum(5)     5                  Return value to rec_sum(5) wchich valu is 5
#                   4+rec_sun(5)=5     return value to rec_sun(4) wchich value is 9
#                   3+rec_sum(4)=9     return value to rec_sun(3) wchich value is 12
#                   2+rec_sum(3)=12    return value to rec_sun(2) wchich value is 14
#                   1+rec_sum(2)= 14   return value to rec_sun(1) wchich value is 15
#                   15

