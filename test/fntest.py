import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import ohHtml2Markdown as h2m

class TestStringMethods(unittest.TestCase):
    def test_h(self):
        ret1 = h2m.Parser("<h1>h1</h1>", 2).convert()
        ret2 = h2m.Parser("<h2>h2</h2>", 2).convert()
        ret3 = h2m.Parser("<h3>h3</h3>", 2).convert()
        ret4 = h2m.Parser("<h4>h4</h4>", 2).convert()
        ret5 = h2m.Parser("<h5>h5</h5>", 2).convert()
        ret6 = h2m.Parser("<h6>h6</h6>", 2).convert()

        self.assertEqual(ret1.strip(), '# h1')
        self.assertEqual(ret2.strip(), '## h2')
        self.assertEqual(ret3.strip(), '### h3')
        self.assertEqual(ret4.strip(), '#### h4')
        self.assertEqual(ret5.strip(), '##### h5')
        self.assertEqual(ret6.strip(), '###### h6')

    def test_p(self):
        ret = h2m.Parser("<p>paragraph</p>", 2).convert()
        self.assertEqual(ret.strip(), 'paragraph')

        ret = h2m.Parser("<p><b>paragraph</b></p>", 2).convert()
        self.assertEqual(ret.strip(), '**paragraph**')

        ret = h2m.Parser("<p>a<b>paragraph</b></p>", 2).convert()
        self.assertEqual(ret.strip(), 'a**paragraph**')

        ret = h2m.Parser("<p><b>paragraph</b>a</p>", 2).convert()
        self.assertEqual(ret.strip(), '**paragraph** a')

        ret = h2m.Parser("<p>a<b>paragraph</b>a</p>", 2).convert()
        self.assertEqual(ret.strip(), 'a**paragraph** a')

    def test_a(self):
        ret = h2m.Parser("<a href='https://www.google.com'>Google</a>", 2).convert()
        self.assertEqual(ret.strip(), '[Google](https://www.google.com)')

    def test_img(self):
        ret = h2m.Parser("<img src='https://www.google.com'>", 2).convert()
        self.assertEqual(ret.strip(), '![image_without_label](https://www.google.com)')

    def test_del(self):
        ret = h2m.Parser("<del>del</del>", 2).convert()
        self.assertEqual(ret.strip(), '~~del~~')

    def test_bold(self):
        ret = h2m.Parser("<b>bold</b>", 2).convert()
        self.assertEqual(ret.strip(), '**bold**')

        ret = h2m.Parser("<strong>bold</strong>", 2).convert()
        self.assertEqual(ret.strip(), '**bold**')

        ret = h2m.Parser("<b><i>bolditalic</i></b>", 2).convert()
        self.assertEqual(ret.strip(), '***bolditalic***')

    def test_italic(self):
        ret = h2m.Parser("<i>italic</i>", 2).convert()
        self.assertEqual(ret.strip(), '*italic*')

        ret = h2m.Parser("<em>italic</em>", 2).convert()
        self.assertEqual(ret.strip(), '*italic*')

    def test_hr(self):
        ret = h2m.Parser("<hr/>", 2).convert()
        self.assertEqual(ret.strip(), '------')

    def test_br(self):
        ret = h2m.Parser("<br>", 2).convert()
        self.assertEqual(ret, '\n')

    def test_ul(self):
        ret = h2m.Parser("<ul><li>1</li><li>2</li><li>3</li></ul>", 2).convert()
        self.assertEqual(ret.strip().replace('\n',''), '- 1- 2- 3')

    def test_ul(self):
        ret = h2m.Parser("<ol><li>1</li><li>2</li><li>3</li></ol>", 2).convert()
        self.assertEqual(ret.strip().replace('\n',''), '1. 12. 23. 3')

    def test_table(self):
        ret = h2m.Parser('<table>'
                            '<thead>'
                                '<tr class="1">'
                                    '<th>thead1</th>'
                                    '<th>thead2</th>'
                                '</tr>'
                            '</thead>'
                            '<tbody>'
                                '<tr>'
                                    '<td>td11</td>'
                                    '<td>td12</td>'
                                '</tr>'
                                '<tr>'
                                    '<td>td21</td>'
                                    '<td>td22</td>'
                                '</tr>'
                            '</tbody>'
                        '</table>', 2).convert()

        self.assertEqual(ret, '\n| thead1 | thead2 |\n| -- | -- |\n| td11 | td12 |\n| td21 | td22 |\n\n')


    def test_blockquote(self):
        ret = h2m.Parser("<blockquote>blockquote</blockquote>", 2).convert()
        self.assertEqual(ret.strip().replace('\n',''), '> blockquote')

    def test_code(self):
        ret = h2m.Parser("<code>inline code</code>", 2).convert()
        self.assertEqual(ret.strip().replace('\n',''), '```inline code```')

    def test_pre(self):
        ret = h2m.Parser("<pre><code>block code</code></pre>", 2).convert()
        self.assertEqual(ret, '\n```\nblock code\n```\n')

    def test_span_title_time(self):
        ret = h2m.Parser("<span>span</span>", 2).convert()
        self.assertEqual(ret, 'span\n')

        ret = h2m.Parser("<title>title</title>", 2).convert()
        self.assertEqual(ret, 'title\n')

        ret = h2m.Parser("<time>time</time>", 2).convert()
        self.assertEqual(ret, 'time\n')

    def test_time(self):
        ret = h2m.Parser("<span>span</span>", 2).convert()
        self.assertEqual(ret, 'span\n')

    def test_iframe(self):
        ret = h2m.Parser("<iframe src='http://www.google.com'>iframe</iframe>", 2).convert()
        self.assertEqual(ret, '[iframe](http://www.google.com)')

    def test_block(self):
        html = ''
        for x in h2m.BLOCK_ELEMENTS__PARSED:
           html += '<' + x + '>'

        html += 'block'

        for x in h2m.BLOCK_ELEMENTS__PARSED[-1::-1]:
           html += '<' + x + '>'

        ret = h2m.Parser(html, 2).convert()
        self.assertEqual(ret, 'block')
        
    def test_discard_elements(self):
        ret = h2m.Parser("<acxa src='http://www.google.com'>acxa</acxa>", 2).convert()
        self.assertEqual(ret, '')

if __name__ == '__main__':
    unittest.main()