from pygments.lexer import RegexLexer, bygroups, include

from pygments.token import *

class MarkdownLexer(RegexLexer):

	tokens = {
		"root": [

			# Quote codes
			(r"\`\`\`(.|\n)+\`\`\`", Generic.Md.MultilineCode),
			(r"((\`\`)|\`).+((\`\`)|\`)", Generic.Md.Code),

			# Bold and Italics
			(r"\*\*\*.+\*\*\*", Generic.Md.StrongandItalics),
			(r"((\*\*)|(__)).+((\*\*)|(__))", Generic.Md.Strong),
			(r"((\*)|(_)).+((\*)|(_))", Generic.Md.Italics),

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
