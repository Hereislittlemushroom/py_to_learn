'''
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc" 

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
'''

keyin = '"abab" p: "ab"'

t_arr,s_arr,p_arr,out_arr = [],[],[],[]

for i in range(len(keyin)):
    if keyin[i]=='"':
         t_arr.append(i)
s = keyin[(t_arr[0]+1):t_arr[1]]
p = keyin[(t_arr[2]+1):t_arr[3]]

s_len,p_len,keyin_len = len(s),len(p),len(keyin)

if(s_len <= 20100 and p_len <=20100 and p_len > 0):
    for i in s:
        s_arr.append(i)

    is_inside = 0
    for i in range(s_len-p_len+1):
        for j in range(p_len):
            # is_inside = 1 if p_arr[j] in s_arr[i:(i+p_len)] else 0 
            if p[j] not in s_arr[i:(i+p_len)]:
                is_inside = 0
                break
            else:
                is_inside = 1
        if is_inside == 1:
            out_arr.append(i)
print(out_arr)
