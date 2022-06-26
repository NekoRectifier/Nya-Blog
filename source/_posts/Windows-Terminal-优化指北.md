---
title: Windows Terminal 优化指北
date: 2022-06-25 22:48:03
tags:
  - Windows
  - 美化
---

# 历史

[Windows Terminal](https://github.com/microsoft/terminal) 在 3 年前的 [Build 2019 大会](<https://zh.wikipedia.org/wiki/Build_(%E5%BC%80%E5%8F%91%E8%80%85%E5%A4%A7%E4%BC%9A)#Build_2019>) 上横空出世。其优秀的 Fluent Design 设计语言、引入的项目栏、高级的字符渲染机制以及崭新的多 Profile 设置使其成为了 Windows 自带 PowerShell 的最佳替代品。

![windows_terminal](Windows_Terminal_v1.0.png)

> Windows Terminal v1.0 --图源 Wikipedia

# 基础优化

尽管上述特性使得 Windows Terminal 具有得天独厚的优势，但其内光秃秃的 PowerShell 依然是日常使用者的痛点。
以下就针对 PowerShell 亟需着手修改的地方进行分享。

## 改变 Windows Terminal 自带字体

字体的修改不仅仅是为了看的舒服，某些字体内置（☞[Nerd Fonts](https://github.com/ryanoasis/nerd-fonts)）的图标与特殊符号会与后期 PowerShell 的主题配合的很好。（如 Git 状态、电池图标、文件夹之类）
所以选定合适的字体是**必要的**。

Terminal 自带的字体是 “Caskaydia Cove”，观感不错。同时它也在 [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) 列表里，所以应该支持各种各样的图标+连字效果。

我个人更加偏好基于 JetBrains Mono 修改的版本，可以在[这里](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)下载。
或者也可以移步至 Nerd Fonts Release [页面](https://github.com/ryanoasis/nerd-fonts/releases)下载你喜欢的字体。

## 升级原有的 PowerShell

在我的 Windows 11 Pro 22H2 上，PowerShell 的版本为：

![ps_ver](ori_ps_ver.png)

> PSVersion 5.1.22621.1

建议还是升级到目前最新的 [PowerShell](https://github.com/PowerShell/PowerShell/releases) （预览版）

![new_ps](new_ps.png)

64 位的选择红色框内的下载，32 位的选择绿色框内的下载即可。

在完成新版 PowerShell 的安装以后，我们就进入到下一步：

## PowerShell 配置文件修改

Windows Terminal 会将安装自带的 PowerShell 设置为“默认配置”，我们需要手动修改其 json 格式的配置文件来解决这一问题。

推荐使用 VSC、Notepad++ 等编辑器，尽量避免使用自带的记事本（不好用

### 步骤

- 在 Windows Terminal 中按下 <kbd>ctrl</kbd> + <kbd>,</kbd>，打开设置界面。

- 在设置界面按左下的“设置”按钮，打开 json 配置文件的编辑页面。
  ![wt_settings](wt_settings.png)

- 在其中找到 `profiles` 项， 并在 `profiles` 项内的 `list` 数组中添加以下内容：
  ```json
  {
    "colorScheme": "One Half Dark", //主题设置
    "commandline": "{ 替换为你自己的 pwsh.exe 路径 } --nologo", //启动命令行设置，填入可执行文件路径即可
    "experimental.retroTerminalEffect": false, // 终端复古风格--关闭
    "experimental.useAtlasEngine": true, // 启用实验性文本渲染引擎--开启
    "font": { // 字体设置
      "face": "JetBrainsMono Nerd Font Mono", // 字体名称
      "size": 12 // 字体大小
    },
    "guid": "{7a9f583e-9bb1-43e2-92f0-86905a28c370}", // 独有的uuid编号
    "hidden": false, // 配置文件是否隐藏--否
    "icon": "D:\\Program Files\\PowerShell\\7-preview\\assets\\Powershell_av_colors.ico", // 配置文件的图标 （可在 pwsh 安装目录找到）
    "name": "PowerShell 7.3.0 Preview", // 配置文件名称
    "opacity": 35, // 终端背景透明度
    "useAcrylic": true // 终端启用亚克力效果--是
  }
  ```
  > **根据配置文件来添加其前后 ","**

- 接着需要将刚刚添加的配置文件设为默认。找到 `defaultProfile` 项并将其设为：

  ```json
  "defaultProfile": "{7a9f583e-9bb1-43e2-92f0-86905a28c370}"
  ```

# 功能增强

基本的 Windows Terminal 配置已经完成，接下来的是对 PowerShell 的处理。

##  Oh-My-Posh

美化当然是必要的，哪个男孩子不会喜欢~~花花绿绿~~的终端主题呢？

### 安装

根据 [Oh-My-Posh官网](https://ohmyposh.dev/docs/installation/windows) 的指南，在 Windows 上推荐使用 [winget](https://www.microsoft.com/p/app-installer/9nblggh4nns1#activetab=pivot:overviewtab) 进行安装。
只需在 PowerShell 输入 `winget install JanDeDobbeleer.OhMyPosh -s winget` 就能完成安装。

如果你的电脑不能安装 winget，则还有以下两种方法可供选择：

- 使用 “scoop”：
  ```powershell
  scoop install https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/oh-my-posh.json
  ```

- 手动下载：
  ```powershell
  Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
  ```

### 设置主题

- 先在 PowerShell 中执行 `Get-PoshThemes`，在给出的主题中选一个记住名字。

  ![posh_theme](posh_theme.png)

- 在 PowerShell 中运行 `New-Item -Path $PROFILE -Type File -Force`

  > **注意：** 这会使得你原有的 PowerShell 启动配置丢失。
  如果你先前配置过，直接跳到下一步即可。

- 运行 `notepad $PROFILE` 进行编辑。
  添加以下内容
  ```powershell
    oh-my-posh init pwsh --config ~/.{ 你想要的主题名称 }.omp.json | Invoke-Expression
  ```

  如有杀毒软件拦截，则使用这个
  ```powershell
  & ([ScriptBlock]::Create((oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\{ 你想要的主题名称 }.omp.json" --print) -join "`n"))
  ```

- 最后再执行 `. $profile`，主题就应用好了。

## 插件

### PSReadline

- 执行 `Install-Module PSReadLine  -Scope CurrentUser`。
  在安装时可能会提示“是否继续”，按 Y/A 同意即可。

- 并在 `$profile` 文件中添加新的一行： `Import-Module PSReadLine`

### Posh-git

- 执行 `Install-Module posh-git -Scope CurrentUser -Force`

- 同样地添加 `Import-Module posh-git` 到 `$profile`

## 历史回溯功能

在 `$profile` 文件中添加：
```powershell
# 设置预测文本来源为历史记录
Set-PSReadLineOption -PredictionSource History

# 每次回溯输入历史，光标定位于输入内容末尾
Set-PSReadLineOption -HistorySearchCursorMovesToEnd
```

## 快捷键设置

同样在 `$profile` 中：
```powershell
# 设置 Tab 为菜单补全和 Intellisense
Set-PSReadLineKeyHandler -Key "Tab" -Function MenuComplete

# 设置 Ctrl+d 为退出 PowerShell
Set-PSReadlineKeyHandler -Key "Ctrl+d" -Function ViExit

# 设置 Ctrl+z 为撤销
Set-PSReadLineKeyHandler -Key "Ctrl+z" -Function Undo

# 设置向上键为后向搜索历史记录
Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward

# 设置向下键为前向搜索历史纪录
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward
```

# 结语

到此 Windows Terminal / PowerShell 的优化就差不多了，基本上终端该有的功能一个都不差。

![ps_finish](ps_finish.png)

# 参考链接

【1】https://zh.wikipedia.org/wiki/Windows_Terminal
【2】https://zhuanlan.zhihu.com/p/137595941
【3】https://ohmyposh.dev/docs/installation/windows
