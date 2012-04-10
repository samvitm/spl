#New approach
import re
t = re.compile(r'(?P<TK_Semicolon>;)|(?P<TK_Comma>,)|(?P<TK_LFBK>\()|(?P<TK_RFBK>\))|(?P<TK_LFBR>\{)|(?P<TK_RFBR>\})|(?P<TK_ASSIGN>\=)|(?P<TK_PLUS>\+)|(?P<TK_STAR>\*)|(?P<TK_FLOAT>\d+\.{1}\d+)|(?P<TK_INTLIT>\d+)|(?P<TK_INT>int)|(?P<TK_STRING>string)|(?P<TK_ID>[a-zA-Z][a-zA-Z0-9]*)|(?P<TK_STRLIT>".*")')
s =  open("sample.txt").read()
ln = 0
while len(s):
  match = t.match(s)
  if match:
    print match.group(),match.lastgroup
    s = s[len(match.group()):]
  else:
    if s[0] not in ['\n','\r','\r\n',' ','\t']:
      print 'Unidentified token : "',s[0],'" at line number ',ln+1
      #break
    elif s[0]!=' ':
      ln+=1
    s = s[1:]