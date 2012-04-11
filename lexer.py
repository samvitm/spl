import re
t = re.compile(r'''(?P<TK_Semicolon>;)|(?P<TK_Comma>,)|(?P<TK_LFBK>\()|(?P<TK_RFBK>\))|(?P<TK_LFBR>\{)|(?P<TK_RFBR>\})|(?P<TK_ASSIGN>\=)|(?P<TK_PLUS>\+)|(?P<TK_STAR>\*)|(?P<TK_FLOAT>\d+\.{1}\d+)|(?P<TK_INTLIT>\d+)|(?P<TK_INT>int)|(?P<TK_STRING>string)|(?P<TK_ID>[a-zA-Z][a-zA-Z0-9]*)|(?P<TK_STRLIT>"(.*?(\\")*.*?)+")''')
s,ln,st = open("sample.txt").read().rstrip(),0,[]
def nextToken():
  global s,ln,st
  while s[0] in ['\n','\r','\r\n',' ','\t']:
    if s[0] not in[' ','\t']: ln+=1
    s = s[1:]
  match = t.match(s)
  if match:
    s,st = s[len(match.group()):],st+[(len(st)+1,str(match.group()),match.lastgroup,)]
    return match.lastgroup
  else:
    print 'Unidentified token : "',s[0],'" at line number ',ln+1
    exit()
#testing
while len(s):
  print nextToken()
print 'Checking symbol table ... '
for e in st:
  print e