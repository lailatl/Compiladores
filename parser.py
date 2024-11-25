import ply.lex as lex
import ply.yacc as yacc
from symbol_table import tabela_de_simbolos


# 1. Definir os Tokens (Lexer)
tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LT', 'GT', 'EQ', 'NEQ', 'LE', 'GE',
    'ASSIGN', 'NUMBER', 'ID', 'NEWLINE'
]

# Palavras reservadas
reserved = {
    'imprime': 'IMPRIME',
    'verdadeiro': 'LOGIC',
    'falso': 'LOGIC',
    'inteiro': 'INT',
    'booleano': 'BOOLEAN'
}

tokens = list(tokens) + list(reserved.values())

# Expressões Regulares para Tokens Simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NEQ = r'!='
t_LE = r'<='
t_GE = r'>='
t_ASSIGN = r'='

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Definir Tokens Complexos
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'ID':
        tabela_de_simbolos.install_id(t.value)
    return t

# Ignorar comentários
def t_COMMENT(t):
    r'\#.*'
    pass

# Definir Nova Linha
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Tratamento de Erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Criar Lexer
lexer = lex.lex()

# 2. Definir as Regras Gramaticais (Parser)
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'ASSIGN'),
)

def p_programa(p):
    '''programa : declaracao_list statement_list
                | empty'''
    pass

def p_declaracao_list(p):
    '''declaracao_list : declaracao NEWLINE declaracao_list
                       | empty'''
    pass

def p_declaracao(p):
    '''declaracao : INT ID declaracao_prime
                  | BOOLEAN ID declaracao_prime'''
    pass

def p_declaracao_prime(p):
    '''declaracao_prime : ASSIGN expr
                        | empty'''
    pass

def p_statement_list(p):
    '''statement_list : statement NEWLINE statement_list
                      | empty'''
    pass

def p_statement(p):
    '''statement : ID ASSIGN expr
                 | IMPRIME LPAREN expr RPAREN'''
    pass

def p_expr(p):
    '''expr : operator comparison'''
    pass

def p_operator(p):
    '''operator : term expr_prime'''
    pass

def p_expr_prime(p):
    '''expr_prime : PLUS term expr_prime
                  | MINUS term expr_prime
                  | empty'''
    pass

def p_term(p):
    '''term : factor term_prime'''
    pass

def p_term_prime(p):
    '''term_prime : TIMES factor term_prime
                  | DIVIDE factor term_prime
                  | empty'''
    pass

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expr RPAREN
              | LOGIC'''
    pass

def p_comparison(p):
    '''comparison : comparison_op operator comparison
                  | empty'''
    pass

def p_comparison_op(p):
    '''comparison_op : EQ
                     | NEQ
                     | LT
                     | GT
                     | LE
                     | GE'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Tratamento de Erros de Sintaxe
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Criar Parser
parser = yacc.yacc()

# Função para Testar o Parser
def test_parser(input_code):
    lexer.input(input_code)
    result = parser.parse(input_code)
    if result is not None:
        print("Parsing concluído com sucesso")
    else:
        print("Erro durante o parsing")


# Exemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")    # espera um arquivo de entrada
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as file: # lê o arquivo de entrada
        input_lines = file.read()
    test_parser(input_lines)
