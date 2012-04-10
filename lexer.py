#Author : 'Samvit Majumdar'
tokens = {
	';' 			: "TK_Semicolon",
	',' 			: "TK_Comma",
	'(' 			: "TK_LFBK",
	')' 			: "TK_RTBK",
	'{' 			: "TK_LFBR",
	'}'				: "TK_RTBR",
	'='				: "TK_ASSIGN",
	'+'				: "TK_PLUS",
	'*' 			: "TK_STAR",
	'[0-9]+' 		: "TK_INTLIT",
	'[0-9\.]+' 		: "TK_REAL_LIT",
	'".+?"'			: "TK_STRINGLIT",
	'int'			: "TK_INT ",
	'float'			: "TK_FLOAT",
	'string'		: "TK_STRING",
  '[a-zA-z0-9]+' 	: "TK_ID",
}

# ( index, lexeme, TokenID, type, scope )
BUFFER_SIZE = 60




  