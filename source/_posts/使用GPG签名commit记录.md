---
title: 使用GPG签名commit记录
date: 2022-01-29 11:16:10
tags: 
  - git
excerpt: 不好好使用 GPG 签名你的 commit 可是有被别人冒用身份的风险哦（不过也没人会专程来冒充我就是了
---

## 前言

以前完全不签名的我，今天看到这个消息  
![asd](fake.png)

看来还是有必要好好学习一下的。

## 下载安装 GPG4win

到[这里](https://gpg4win.org/download.html)下载 GPG4win。

注意安装的时候**一定**要把`Kleopatra`给勾选上，否则需使用 Cli 进行配置。  
![gpg](gpg_install.png)

## 配置密钥

安装完后打开`Kleopatra`, 点击`新建密钥对`。

![kleo_gen_setting](kleo_gen_setting.png)

在弹出的新窗口中,输入名称(可随意, Github 不会管的)和电子邮件地址(电子邮件地址必须与注册 Github 的一致)

> `使用密码句保护生成的密钥` 相当于针对 GPG 签名的最后一把锁 | 按自己情况勾选

填好后, 点击高级设置

![kleo_advanced](kleo_advanced.png)

- 将密钥类型设置为`RSA`
- 将密钥长度设置为`2048` (两个都是)
- 有效期按自己喜好设置

最后点击`下一步`你的密钥就生成完成了

## 向 Github 添加密钥

在 Kleopatra 主界面中, 右键单击你刚刚生成的密钥, 选择`导出...`

![export_key](export_key.png)

将`asc`后缀的公钥保存好, 打开 Github 的`settings`页面, 点击`Add SSH Key`把你的公钥添加进去

## 本地 git 设置

先得去获取你 GPG 密钥的指纹, 再打开 Kleopatra, 右键你的密钥选择`细节`

![kleo_fingerprint](kleo_fingerprint.png)

将`指纹`复制下来即可

之后的操作就相当简单了, 如下

打开`git cli` 输入:

```bash
    git config --global user.signkey {指纹(去掉空格)}
    git config --global user.gpgsign true
    // 这会对所有仓库生效
    git config user.gpgsign true
    // 仅对该仓库生效
```

### 错误处理

`No Secret Key`
![no_secret_key](no_secret_key.png)

这是由于 git 默认使用的 gpg 程序并非我们先前安装的那一个，故采用
`git config --global gpg.program "{安装目录\bin\gpg.exe}"`
来设置 gpg.program。

### 其他

- 设置密钥密码过期时间

  打开 Kleopatra，选择`设置` > `配置Kleopatra` > `GnuPG` > `Private Key` > `Expire cached PINs after N Seconds`

  ![expire_setting](expire_setting.png)

  填入`604800`即可，单位为秒，默认为`0`，即永不过期。

## 参考链接

[1] https://www.liesauer.net/blog/post/sign-git-commit-with-gpg-under-windows.html  
[2] https://blog.sdlsj.net/archives/git/windows-sign-git-commit-with-gpg/
