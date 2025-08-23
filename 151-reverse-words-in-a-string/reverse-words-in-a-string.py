class Solution:
    def reverseWords(self, s: str) -> str:
        wl = []
        temp_list = []
        ns = ""
        for c in s:
            if c == " ":
                if len(temp_list)>0:
                    wl.append(temp_list)
                    temp_list = []
            else:
                temp_list.append(c)
        if len(temp_list)>0:
            wl.append(temp_list)
        started = False
        for i in range(len(wl)-1, -1, -1):
            if started:
                ns = ns + " "
            ns += "".join(wl[i])
            started = True
        return ns




            
            


                    