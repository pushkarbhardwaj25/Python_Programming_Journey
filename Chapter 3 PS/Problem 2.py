letter = '''Hello <|Name|>,
            You are selected for the Job Interview !
            <|Date|>'''
print(letter.replace("<|Name|>", "Pushkar").replace("<|Date|>", "28th June, 2030"))
