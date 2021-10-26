---
title: jQuery笔记
date: 2021-10-26 22:08:07
tags: Web, 
---

## 基础语法

`$(selector).action()` 

- `$`  美元符号, jQuery定义开始

- `selector`  用于确定操作的HTML元素  
  [CSS选择器 见此](https://www.runoob.com/cssref/css-selectors.html)

- `action()`  就是指代操作

## 常用事件方法

### "文档就绪事件"  

  如下代码: 
  ```jQuery
  $(document).ready(function(){
 
   // 开始写 jQuery 代码...
 
  });
  ```

  这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码，即在 DOM 加载完成后才可以对 [DOM](https://developer.mozilla.org/zh-CN/docs/Web/API/Document_Object_Model/Introduction) 进行操作。

### [剩余见此](https://www.runoob.com/jquery/jquery-events.html)