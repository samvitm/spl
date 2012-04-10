BUFFER_SIZE = 60
import re
tokens = {
  '\;': "TK_Semicolon",
  '\,': "TK_Comma",
  '\(': "TK_LFBK",
  '\)': "TK_RTBK",
  '\{': "TK_LFBR",
  '\}': "TK_RTBR",
  '\=': "TK_ASSIGN",
  '\+': "TK_PLUS",
  '\*': "TK_STAR",
  '[0-9]+': "TK_INTLIT",
  '[0-9]+\.[0-9]+': "TK_REAL_LIT",
  '(?:"[^"]*\\(?:.[^"]*\\)*.[^"]*")|(?:"[^"]*")': "TK_STRINGLIT",
  'int': "TK_INT ",
  'float': "TK_FLOAT",
  'string': "TK_STRING",
  '[a-zA-Z0-9]?[a-zA-Z0-9]+': "TK_ID",
}
f = open('sample.txt')
tokenlist,st = [],[]
s = f.read(BUFFER_SIZE)
while s!='':  
  for lexeme in re.sub(r'([\+\*\(\)\{\}\;\=\,\"])', ' \g<1> ',s).split():
    for key in tokens.iterkeys():
      match = re.match(key,lexeme)
      if match:
        tokenlist.append(tokens[key])
        st.append((len(tokenlist),lexeme,tokens[key]))
        break
  s = f.read(BUFFER_SIZE)
print tokenlist
print st


  