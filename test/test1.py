"""
This is for testing the lexer.

"""

from convmd import lexer

if __name__ == "__main__":
	l = lexer.MarkdownLexer()
	text = """

<!-- This
is
actually
a comment-->

`Single line code`

```
Multiline code

code
```

line break<br>

text

> Quote

<sub> subscript </sub>
<sup> superscript </sup>


**Bold**
*Italics*
***Bold and Italics***

[http://example.com]( Link )

![http://example.com/example.png]( This is an Image )

# Heading1
## Heading2
### Heading3
#### Heading4
##### Heading5
###### Heading6

~~Striked Text~~

"""

	for i in l.get_tokens(text):
		print(i)
