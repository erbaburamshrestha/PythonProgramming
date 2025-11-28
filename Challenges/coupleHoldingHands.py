class CoupleHodingHand:
    def minSwapsCouple(self, row):
        lengthRow=len(row)
        index={row[i]:i for i in range(lengthRow)}
        ans=0
        for i in range(0,lengthRow,2):
            a=row[i]
            b=row[i+1]
            if (a%2==0 and b==a+1) or (b%2==0 and a==b+1):
                continue
            target=a+1 if a%2==0 else a-1
            target_idx=index[target]
            b_idx=i+1
            row[i+1],row[target_idx]=row[target_idx],row[i+1]
            index[target]=i+1
            index[b]=target_idx
            ans+=1
        return ans
row = [0,2,1,3]

_CoupleHodingHand = CoupleHodingHand()
print(_CoupleHodingHand.minSwapsCouple(row))