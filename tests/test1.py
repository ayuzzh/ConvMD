"""
This is for testing the lexer.

"""

from convmd import lexer

if __name__ == "__main__":
	l = lexer.MarkdownLexer()
	text = (open("tests/test1.md", "r")).read()
	for i in l.get_tokens(text):
		print(i)
