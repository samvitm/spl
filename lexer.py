# Samvit Majumdar 2009C6ps814, Namandeep Singh Chugh 2009C6PS569 , Aayush Shrivastava 2009C6PS708P
import re
t = re.compile(r'''(?P<TK_Semicolon>;)|(?P<TK_Comma>,)|(?P<TK_LFBK>\()|(?P<TK_RTBK>\))|(?P<TK_LFBR>\{)|(?P<TK_RTBR>\})|(?P<TK_ASSIGN>\=)|(?P<TK_PLUS>\+)|(?P<TK_STAR>\*)|(?P<TK_REAL_LIT>\d+\.{1}\d+)|(?P<TK_INTLIT>\d+)|(?P<TK_INT>int)|(?P<TK_STRING>string)|(?P<TK_FLOAT>float)|(?P<TK_ID>[a-zA-Z][a-zA-Z0-9]*)|(?P<TK_STRLIT>"(.*?(\\")*.*?)+")''')
s,ln,tt = open("sample.txt").read().rstrip(),0,[]
symbol_table = {}

print '+'*20,'Lexer Begin','+'*20,'\n\n'

def ParseError(s):
  print "%"*50,'\n'
  print s,'\n'
  print "%"*50
  exit()


def getnextToken():
  global s,ln,tt,symbol_table
  if not len(s) : return 0
  while s[0] in ['\n','\r','\r\n',' ','\t']:
    if s[0] not in[' ','\t']: ln+=1
    s = s[1:]
  match = t.match(s)
  if match:
    s = s[len(match.group()):]
    tt = tt+[(len(tt)+1,str(match.group()),match.lastgroup,ln+1,)]
    return match.lastgroup
  else:
    raise ParseError('Unknown symbol %r at line %r' %(s[0],ln+1))



def getType(prevToken,nextToken):
  global symbol_table
  if nextToken == 'TK_LFBK':
    return 'function'
  elif prevToken in ['TK_INT','TK_FLOAT','TK_STRING']:
    return prevToken
  else:
    print prevToken
    raise ParseError("Undeclared variable %r at line number %r" % (tt[-2][1],tt[-2][-1]))
    return 0
  
def print_symbol_table():
  print 'Symbol table \n',"="*70
  for s in symbol_table:
    print s,':',symbol_table[s]
  print '='*70


def build_tokens():
  l = []
  f = 0
  scope =[]
  currToken,prevToken,nextToken = '','',''
  while len(s):
    token = getnextToken()
    l.append(token)
    #print tt[-1]
    if token in ["TK_LFBR","TK_LFBK"]:
      scope.append((token,tt[-1][-1]))  #adding '{' to scope stack along with line number
    if token == 'TK_RTBR':
      for symbol in symbol_table:
        if 'scope_end' not in symbol_table[symbol]:
          symbol_table[symbol]['scope_end'] = tt[-1][-1]
      scope = []
    if prevToken:
      nextToken = token
      #print prevToken,currToken,nextToken
      if tt[-2][1] not in symbol_table and len(scope)!=0:
        print 'Adding',currToken,':',tt[-2][1],'to symbol table'
        symbol_table[tt[-2][1]] = {"line":tt[-2][-1],"type":getType(prevToken,nextToken),"declaration":tt[-2][-1],"scope_start":scope[-1][1]}
      else:
        print 'Symbol :',tt[-2][1],'already present in symbol table -- Ignore - Symbol table unchanged'
      currToken,nextToken,prevToken = '','',''
      #print 'End of addition'
      print_symbol_table()
    elif token == 'TK_ID':
      print 'Identifier found' ,
      prevToken = tt[-2][2]
      currToken = token
      print currToken,',Previous token : ',prevToken
      #print '----------------'


  return l

tokens = build_tokens()

def check_tt():
  print 'Checking token table ... '
  for e in tt:
    print e

#check_tt()

