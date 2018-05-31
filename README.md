# ohHTML2Markdown

当爬取一些如新闻、简书、知乎之类的面向文档的网站时，通常需要将文章保存下来，最合适的介质莫过于Markdown文档（有些网站本来就是用Markdown渲染出来的）。`ohHTML2Markdown`可以将一部分或整个网页转化为Markdown文档，`ohHTML2Markdown`会尽量处理一些不规范的HTML文档，但是不保证输出文档的质量。

When crawling doc-oriented websites contains news, knowledge market like quora, or even Github, sometimes, you might like to save the article. The best media for storage would be .md file, some articles are even generated from .md files.  `ohHTML2Markdown` is able to convert HTML fragment or a complete html file to a human-friendly .md file. Although there would be some irresponsible use in HTML tags, `ohHTML2Markdown` will do its best to ensure the output stays in its best quality.

目前支持的HTML标签有：`h1~h6`, `p`, `a`, `img`, `del`, `b`, `strong`, `i`, `em`, `hr`, `br`, `ul`, `ol`, `table`, `blockquote`, `code`, `pre`, `span`, `title`, `time`, `iframe`, `section`, `div`, `html`, `body`, `head`。

Currently, supported HTML tags include: `h1~h6`, `p`, `a`, `img`, `del`, `b`, `strong`, `i`, `em`, `hr`, `br`, `ul`, `ol`, `table`, `blockquote`, `code`, `pre`, `span`, `title`, `time`, `iframe`, `section`, `div`, `html`, `body`, `head`。

处理主要靠的是`BeautifulSoup`库的`html.parser`解析器和`.descendants`对象。前者可以把html文档解析成一个树状模型，访问`.contents`可以访问到当前层级的所有子树的根节点；后者可以返回一个生成器，它包含了当前子树的所有节点（包含本身）。

`ohHTML2Markdown` is mainly built on `BeautifulSoup` Library, to be more specific, its `html.parser` parser and the `.descendants` object. The parser is able to convert a html file to a tree structure, the using `.content` we can access all sub-trees on the same level; `.descendants` returns an generator which contains all nodes in the current (sub)tree (including itself).

通过判断`descendants`的长度可以知道该子树有没有子节点，然后 根据当前tag的类型，可以选择继续进行深度遍历还是将它转换为Markdown的语义。

By checking the length of `descendants` generator, we can know whether this tree has descendants or not(not that this tree could also be one of descendants of another tree on its topper level). Then based the type of tags included, we make the decision to go further, or convert it to markdown semantics.

其他关于本库的一些细节：[发布自己的Python包 - ohHTML2Markdown](https://journal.ethanshub.com/post/category/gong-cheng-shi/-python-ohhtme2mardown)。

More about this library, [发布自己的Python包 - ohHTML2Markdown](https://journal.ethanshub.com/post/category/gong-cheng-shi/-python-ohhtme2mardown). This post is Chinese.



## 安装 Installation

```
pip install ohHTML2Markdown
```



## 使用 Usage

```
import ohHtml2Markdown as h2m

# 从字符串读取 Read from string
result = h2m.Parser("<h1>h1</h1>", h2m.Parser.STRING).convert()

# 或从文件读取 Read from file
result = h2m.Parser("test/test.html", h2m.Parser.FILE).convert()

with open("test/out.md", 'w', encoding='utf-8') as file:
        file.write(result)
```