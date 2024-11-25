import ply.lex as lex
from simbol_table import tabela_de_simbolos

# Lista de tokens
tokens = [
    'IMPRIME',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'LT', 'GT', 'EQ', 'NEQ', 'LE', 'GE',
    'ASSIGN',
    'NUMBER',
    'LOGIC',
    'INT', 'BOOLEAN',
    'ID'
]

# Definições de palavras reservadas
reserved = {
    'imprime': 'IMPRIME',
    'verdadeiro': 'LOGIC',
    'falso': 'LOGIC',
    'inteiro': 'INT',
    'booleano': 'BOOLEAN'
}

# Adiciona palavras reservadas aos tokens
tokens += list(reserved.values())

# Expressões regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LT      = r'<'
t_GT      = r'>'
t_EQ      = r'=='
t_NEQ     = r'!='
t_LE      = r'<='
t_GE      = r'>='
t_ASSIGN  = r'='

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Expressão regular para identificar números (inteiros e decimais)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    if t.type == 'ID':
        tabela_de_simbolos.install_id(t.value)  # Instala o ID na tabela de símbolos
    return t

# Ignorar comentários (comentários de linha única)
def t_COMMENT(t):
    r'\#.*'
    pass

# Definir nova linha
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

# Tratamento de erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Criar o lexer
lexer = lex.lex()

# Função para testar o lexer
def tokenize(code):
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))
    return tokens

