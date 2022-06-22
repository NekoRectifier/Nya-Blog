---
title: jQuery笔记
date: 2021-10-26 22:08:07
tags: 
  - Web
  - jQuery
---

## 基础语法

`$(selector).action()` 

- `$`  美元符号, jQuery定义开始

- `selector`  用于确定操作的HTML元素  
  [CSS选择器 见此](https://www.runoob.com/cssref/css-selectors.html)  

  常用选择器:
    - `.<Class-Name>` 选择所有`class=<>`的元素
    - `#<id>` 选择所有`id`为指定值的元素
    - `<元素类型>` 选择所有该类型的元素 (支持`,`分隔)
    - `[<attribute>]` 选择所有带有指定属性的元素  
    
      如	`[target=-blank]`  和  
          `[title~=flower]`  (包含关系)


- `action()`  就是指代操作

## 常用事件方法

### "文档就绪事件"  

  如下代码: 
  ``` jQuery
  $(document).ready(function(){
 
   // 开始写 jQuery 代码...
 
  });
  ```

  这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码，即在 DOM 加载完成后才可以对 [DOM](https://developer.mozilla.org/zh-CN/docs/Web/API/Document_Object_Model/Introduction) 进行操作。

### [剩余见此](https://www.runoob.com/jquery/jquery-events.html)