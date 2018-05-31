# ohHTML2Markdown

当爬取一些如新闻、简书、知乎之类的面向文档的网站时，通常需要将文章保存下来，最合适的介质莫过于Markdown文档（有些网站本来就是用Markdown渲染出来的）。```ohHTML2Markdown```可以将一部分或整个网页转化为Markdown文档，```ohHTML2Markdown```会尽量处理一些不规范的HTML文档，但是不保证输出文档的质量。

目前支持的HTML标签有：```h1~h6```,```p```,```a```,```img```,```del```,```b```,```strong```,```i```,```em```,```hr```,```br```,```ul```,```ol```,```table```,```blockquote```,```code```,```pre```,```span```,```title```,```time```,```iframe```,```section```,```div```,```html```,```body```,```head```。

处理主要靠的是```BeautifulSoup```库的```html.parser```解析器和```.descendants```对象。前者可以把html文档解析成一个树状模型，访问```.contents```可以访问到当前层级的所有子树的根节点；后者可以返回一个生成器，它包含了当前子树的所有节点（包含本身）。

通过判断```descendants```的长度可以知道该子树有没有子节点，然后 根据当前tag的类型，可以选择继续进行深度遍历还是将它转换为Markdown的语义。

其他关于本库的一些细节：[发布自己的Python包 - ohHTML2Markdown](https://journal.ethanshub.com/post/category/gong-cheng-shi/-python-ohhtme2mardown)。

## 安装

```
pip install ohHTML2Markdown

```

## 使用

```
import ohHtml2Markdown as h2m

result = h2m.Parser("<h1>h1</h1>", h2m.Parser.STRING).convert()

# 或从文件读取
result = h2m.Parser("test/test.html", h2m.Parser.FILE).convert()

```

# TODO

- 扩展子块用于解析特性网站的特定标签
- Nested列表（当前版本可以识别这种列表，但是无法输出正确格式的markdown，不会计算缩进）
- 其他未涉及的HTML标签
- 命令行工具
- 其他需要修改的问题