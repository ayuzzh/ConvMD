
"""

TODO:
1. Support for custom tags
2. Support for Mathematical equations
3. Support for table
4. Support for Images
5. Support for order

It contains lexer which uses pygments for generating tokens. Previously
I tried using ply for lexing but was quite complicated to implement and
also tried implementing a lexer from scratch but it didn't go well.

"""


from pygments.lexer import RegexLexer, bygroups, include

from pygments.token import *

class MarkdownLexer(RegexLexer):

	tokens = {
		"root": [

			# Headings
			(r"(\n|)######.+", Generic.Md.Heading6),
			(r"(\n|)#####.+", Generic.Md.Heading5),
			(r"(\n|)####.+", Generic.Md.Heading4),
			(r"(\n|)###.+", Generic.Md.Heading3),
			(r"(\n|)##.+", Generic.Md.Heading2),
			(r"(\n|)#.+", Generic.Md.Heading1),


			# Quote codes
			(r"\`\`\`(.|\n)+\`\`\`", Generic.Md.MultilineCode),
			(r"((\`\`)|\`).+((\`\`)|\`)", Generic.Md.Code),

			# Bold and Italics
			(r"\*\*\*.+\*\*\*", Generic.Md.StrongandItalics),
			(r"((\*\*)|(__)).+((\*\*)|(__))", Generic.Md.Strong),
			(r"((\*)|(_)).+((\*)|(_))", Generic.Md.Italics),

			# Striked text
			(r"\~\~.+\~\~", Generic.Md.Striked),

			# Links
			(r"\[.+\]( +|)\(.+\)", Generic.Md.Link),

			# Quote
			(r">.+", Generic.Md.Quote),

			# Html Tags
                        (r"<br>", Generic.Md.HtmlTag.Break),

			(r"<sub>.+</sub>", Generic.Md.HtmlTag.SubScript),
			(r"<sup>.+</sup>", Generic.Md.HtmlTag.SuperScript),

			# General
			(r"\n", Generic.Md.Newline),
			(r".+", Generic.Md.Text),
		]
	}
