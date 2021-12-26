# mdpy


## TODO

[ ] 单换行修改。如果是<!-- -->不要在末尾添加空格了

[ ] 文件id和link函数。


## 规则

1. 命令，image。插入图片。
2. 命令，file。插入文件链接。
3. 支持单换行。参见 formatter.py。
4. 自动添加h1标题。参见 insert_h1() formatter.py。
5. 遇到行首和行尾的 {}，自动添加代码范围


## 命令行参数

```
parser.add_argument('--note-directiony', '-d', required=True, help='note directiony')
parser.add_argument('--file', '-f', default=None, required=False, help='file')
parser.add_argument('--assets-repository-path', default=None, required=False, help='assets repository path')
parser.add_argument('--assets-folder-path', default=None, required=False, help='assets folder path')
```

命令行使用举例
```
py ../mdpy/main.py -d . -f ./trade/20200915_茅台进取.md
```

## 命令，file

```
(file_path, description) -> html
{
    hmtl, <a href='file_path'>description</a>
    过程
    {
        1. 文件复制和重命名。类似image。
        2. 生成html文本。
    }
}
```

## sublime插件

参见，sublime_text_fans 项目。  
open_github_html.py -- 打开文件对应在github上的网页  
compile_mdpy_then_sync.py -- 同步内容到 github  
