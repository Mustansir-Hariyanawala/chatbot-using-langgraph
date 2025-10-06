import re


C_KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef", "union", "unsigned", "void",
    "volatile", "while", "include", "define"
}


C_OPERATORS = {
    "+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=",
    "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "=", "+=", "-=", "*=",
    "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "->", ".", "?", ":"
}

def lexical_analyzer(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

 
    code = re.sub(r'//.*?\n|/\*.*?\*/', '', code, flags=re.S)
    print(code)

    tokens = re.findall(r'[A-Za-z_]\w*|\d+\.\d+|\d+|==|!=|>=|<=|->|\+\+|--|&&|\|\||[+\-*/%=&|^~<>?:;{},()\[\]]', code)

    
    print(tokens)

    keywords = set()
    constants = set()
    variables = set()
    operators = set()

    for token in tokens:
        if token in C_KEYWORDS:
            keywords.add(token)
        elif token in C_OPERATORS:
            operators.add(token)
        elif re.fullmatch(r'\d+(\.\d+)?', token):
            constants.add(token)
        elif re.fullmatch(r'[A-Za-z_]\w*', token):
            variables.add(token)

  
    print("\n=== LEXICAL ANALYSIS RESULT ===")
    print("Keywords:", ", ".join(sorted(keywords)) if keywords else "None")
    print("Constants:", ", ".join(sorted(constants)) if constants else "None")
    print("Variables:", ", ".join(sorted(variables)) if variables else "None")
    print("Operators:", ", ".join(sorted(operators)) if operators else "None")



if __name__ == "__main__":
    file_path = input("Enter path of C code file: ").strip()
    lexical_analyzer(file_path)
 # type: ignore
