---
title: 如何在中git回退版本并提交
date: 2022-01-18 21:43:19
tags: git
---

## 前言

git作为版本控制工具，回退是必不可少的操作之一。 可很多时候都只是知道有却不会上手操作，与其每次都去查Google不如自己写一篇记录下好了。

## 操作命令

```bash
    git reset --hard {位置}
```

看起来相当简单的命令, 解析一下:

-   `--hard` 彻底回退, 本地的文件会改变 (相应的还存在着一个`"soft"`)

-   `{位置}` 可以用`HEAD^`之类或者提交的SHA值来代替

## 那我不仅要本地文件回退还要再提交

如果你直接提交 ->

(截图没了) 反正就是不能正常提交的样子, git会贴心的提示你云端库比你本地库要新, 还问你要不要拉取...

### 正解

应该使用

```bash
    git push --force
```

>   如果出现无法拉取的奇怪问题, 则执行:  
    `git fetch --all`  
    `git reset --hard oringin/{分支名}`

## 后记

我想我还是附上这个链接 [Oh Shit, Git?!](https://ohshitgit.com/zh)  
对于来这里查看指南的各位还是相当有用的。

## 参考链接

[1] https://blog.csdn.net/xue251248603/article/details/78964011  
[2] https://www.liaoxuefeng.com/wiki/896043488029600/897013573512192  
[3] https://blog.csdn.net/yangfengjueqi/article/details/61668381
