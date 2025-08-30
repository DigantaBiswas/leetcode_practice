class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            group = 1
            while (group + i) < len(chars) and chars[i] == chars[group+i]:
                group+=1
            chars[insert] = chars[i]
            insert+=1
            if group > 1:
                chars[insert:insert+len(str(group))] = list(str(group))
                insert+=len(str(group))
            i+=group
        return insert
            


            
