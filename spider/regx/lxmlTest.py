# coding:utf-8

from lxml import etree

text = '''
<div>
<ul>
>
i>
/a></li>
i>
<li class="item-0"><a href="link1.html">first item</a></li
<li class="item-1"><a href="link2.html">second item</a></l
<li class="item-inactive"><a href="link3.html">third item<
<li class="item-1"><a href="link4.html">fourth item</a></l
<li class="item-0"><a href="link5.html">fifth item</a> #
注意，此处缺少⼀个 </li> 闭合标签
</ul>
</div>
'''

html=etree.HTML(text)
result=etree.tostring(html)

print(result)