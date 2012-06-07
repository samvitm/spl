# Samvit Majumdar 2009C6ps814, Namandeep Singh Chugh 2009C6PS569 , Aayush Shrivastava 2009C6PS708P
from lexer import tokens,tt,symbol_table, print_symbol_table,ParseError

count = -1
def nextToken():
  global count
  count+=1
  try:
    token = tokens[count]
  except :
    return '$'
  return token

parse_table = {
    "<program>" : {"TK_INT" : 1 , "TK_FLOAT" :1 , "TK_STRING" : 1 ,"TK_Comma" : 1},
    "<functionbody>" : { "TK_LFBR" : 2 },
    "<functions>" : {"TK_INT" : 3 , "TK_FLOAT" : 3, "TK_STRING" : 3 , "TK_Comma" : 4},
    "<function>" : {"TK_INT" : 5,"TK_FLOAT" : 5 , "TK_STRING" : 5},
    "<functionsignature>" : {"TK_INT" : 6,"TK_FLOAT" : 6,"TK_STRING" :6},
    "<type>" : {"TK_INT":7,"TK_FLOAT" : 8,"TK_STRING" : 9},
    "<params>" : { "TK_INT" : 10,"TK_FLOAT" : 10,"TK_STRING":10,"TK_RTBK":11},
    "<declarations>" : {"TK_INT" : 12 , "TK_FLOAT" : 12 ,"TK_STRING" : 12,"TK_ID" : 13,"TK_Comma" : 13},
    "T" : {"TK_ID" : 14 ,"TK_INTLIT" : 14,"TK_REAL_LIT" : 14,"TK_STRLIT" : 14},
    "T!" : {"TK_STAR" : 15,"TK_PLUS" : 16,"TK_Semicolon" : 16},
    "<args>" : {"TK_ID" : 17 ,"TK_INTLIT" : 17,"TK_REAL_LIT" : 17,"TK_STRLIT" : 17,"TK_RTBK" :18},
    "<statements>" : {"TK_ID" : 19,"TK_STAR":20},
    "<statements!>" : {"TK_ID":21,"TK_INTLIT":22,"TK_REAL_LIT":23,"TK_STRLIT":24},
    "<more>" : {"TK_LFBK":25,"TK_PLUS":26,"TK_Semicolon":26,"TK_STAR":27},
    "<expr>" : {"TK_ID" : 28 ,"TK_INTLIT" : 28,"TK_REAL_LIT" : 28,"TK_STRLIT" : 28},
    "<expr!>" : {"TK_PLUS" : 29,"TK_Semicolon":30},
    "F" : {"TK_ID" : 31 ,"TK_INTLIT" : 32,"TK_REAL_LIT" : 33,"TK_STRLIT" : 34},
}

stack = ['$',"<program>"]

def get_grammar():
  f = open('grammar.txt')
  g = [' ',] #compensate for the 0'th grammar rule
  for line in f:
    g.append(line.strip())
  return g

def get_terminals():
  f = open('terminals.txt')
  t = []
  for line in f:
    t.append(str(line.strip()))
  return t

terminals = get_terminals()
grammar = get_grammar()

def get_rhs(s):
  m = s.split('->')[-1]
  return m.split()


def parse():
  global stack
  a = nextToken()
  x = stack[-1]
  while x != '$':
    print stack,x,a
    if x == a:
      stack.pop()
      print stack
      a = nextToken()
      print 'Next token to parse : ',a
    elif x in terminals:
      error = 'Expected Token : %r got Token : %r - %r at line number %d' %(x,tt[count][2],tt[count][1],tt[count][-1])
      raise ParseError(error)
    elif  a not in parse_table[x] :
      print a,x,tt[count]
      error = 'Invalid token %r, expected tokens : %r at line number %r' % (a,[ key for key in parse_table[x]],tt[count][-1])
      raise ParseError(error)
    else:
      rule = str(grammar[parse_table[x][a]])
      print 'Match found!'
      print a,x,tt[count]
      print 'Applying grammar rule  : ',rule
      #print stack
      stack.pop()
      #print stack
      stack = stack + get_rhs(rule)[::-1]
      print stack
      print '-----END----'
    x = stack[-1]
    print 'Stack top now :',x,'\n','='*40

    #print a,'||-- x :',x,'||--stack :',stack

print '\n\n'
print '#'*20,'Starting to parse','#'*80
print '\n\n'
parse()
print '\n\n','*'*20,'Parsing Completed!','*'*20,'\n'
print_symbol_table()
print '\n\n','*'*20,'Parsing was successful!','*'*20,'\n'