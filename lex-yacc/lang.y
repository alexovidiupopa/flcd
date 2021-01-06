%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1 
%}

%token AND
%token ARRAY
%token ELSE
%token FOR
%token GO
%token IF
%token NUMBER
%token OR
%token CIN
%token COUT
%token STRING
%token WHILE
%token XOR

%token ID
%token CONST

%token ATRIB
%token EQ
%token NE
%token LE
%token GE 
%token LT
%token GT
%token NOT 

%token DOT 

%left '+' '-' '*' '/'

%token PLUS 
%token MINUS
%token DIV 
%token MOD 
%token MUL 

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET 
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET 

%token READ_OP
%token WRITE_OP 

%token COMMA 
%token SEMI_COLON
%token COLON
%token SPACE 

%start program 

%%
program : GO cmpdstmt
	;
declaration :  type ID
	    ;
type :  NUMBER | STRING | typeTemp
	   ;
typeTemp : /*Empty*/ | ARRAY OPEN_RIGHT_BRACKET CONST CLOSED_RIGHT_BRACKET 
	 ;
cmpdstmt : OPEN_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET
	 ;
stmtlist :  stmt stmtTemp
	 ;
stmtTemp : /*Empty*/ | stmtlist
	 ;
stmt :  simplstmt SEMI_COLON | structstmt
     ;
simplstmt :  assignstmt | iostmt | declaration
	 ; 
structstmt :  cmpdstmt | ifstmt | whilestmt | forstmt
	   ;
ifstmt :  IF OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET cmpdstmt tempIf
       ;
tempIf : /*Empty*/ | ELSE cmpdstmt
       ;
forstmt :  FOR forheader cmpdstmt
       ;	
forheader :  OPEN_ROUND_BRACKET NUMBER assignstmt SEMI_COLON OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET SEMI_COLON assignstmt CLOSED_ROUND_BRACKET
	  ;
whilestmt :  WHILE OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET cmpdstmt
	  ;
assignstmt :  ID ATRIB expression
	   ;
expression : arithmetic2 arithmetic1
	   ;
arithmetic1 : PLUS arithmetic2 arithmetic1 | MINUS arithmetic2 arithmetic1 | /*Empty*/
	    ;
arithmetic2 : multiply2 multiply1
	    ;
multiply1 : MUL multiply2 multiply1 | DIV multiply2 multiply1 | /*Empty*/ 
	  ;
multiply2 : OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | CONST | ID | IndexedIdentifier
	  ;
IndexedIdentifier :  ID OPEN_RIGHT_BRACKET CONST CLOSED_RIGHT_BRACKET
		  ;
iostmt :  CIN READ_OP ID | COUT WRITE_OP ID | COUT WRITE_OP CONST
      ; 
condition : expression GT expression |
	 expression GE expression | 
	 expression LT expression |
	 expression LE expression | 
	 expression EQ expression |
	 expression NE expression
	  ;
boolean_condition : condition boolean_cond_temp
		  ;
boolean_cond_temp : /*Empty*/ | AND boolean_condition | OR boolean_condition | XOR boolean_condition
		 ; 
%%
yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}

