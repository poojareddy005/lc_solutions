class Solution:
    def generate(self,ind,curr,res,open,close,n):
        if(open==close and ind==n*2):
            res.append(curr)
            return
        if(open>n):
            return
        self.generate(ind+1,curr+"(",res,open+1,close,n)
        if(open>close):
            self.generate(ind+1,curr+")",res,open,close+1,n)
    def generateParenthesis(self, n: int) -> List[str]:
        ind=0
        curr=""
        res=[]
        open=0
        close=0
        self.generate(ind,curr,res,open,close,n)
        return res
        