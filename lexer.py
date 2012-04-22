import re
t = re.compile(r'''(?P<TK_Semicolon>;)|(?P<TK_Comma>,)|(?P<TK_LFBK>\()|(?P<TK_RTBK>\))|(?P<TK_LFBR>\{)|(?P<TK_RTBR>\})|(?P<TK_ASSIGN>\=)|(?P<TK_PLUS>\+)|(?P<TK_STAR>\*)|(?P<TK_REAL_LIT>\d+\.{1}\d+)|(?P<TK_INTLIT>\d+)|(?P<TK_INT>int)|(?P<TK_STRING>string)|(?P<TK_FLOAT>float)|(?P<TK_ID>[a-zA-Z][a-zA-Z0-9]*)|(?P<TK_STRLIT>"(.*?(\\")*.*?)+")''')
s,ln,st = open("sample.txt").read().rstrip(),0,[]
def getnextToken():
  global s,ln,st
  if not len(s) : return 0
  while s[0] in ['\n','\r','\r\n',' ','\t']:
    if s[0] not in[' ','\t']: ln+=1
    s = s[1:]
  match = t.match(s)
  if match:
    s,st = s[len(match.group()):],st+[(len(st)+1,str(match.group()),match.lastgroup,ln+1,)]
    return match.lastgroup
  else:
    raise SyntaxError('Unknown symbol %r at line %r' %(s[0],ln+1))


#testing
def build_tokens():
  l = []
  while len(s):
    l.append(getnextToken())
  return l

tokens = build_tokens()

print 'Checking token table ... '
for e in st:
  print e
