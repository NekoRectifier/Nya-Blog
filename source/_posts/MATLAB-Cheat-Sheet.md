---
title: MATLAB Cheat sheet
date: 2021-12-18 16:15:39
tags: [MATLAB]
---

# Misc (杂项)

*   用 `"` 来标识字符串(String); 用 `'` 来表示字符类型(Char)  

*   优雅的MATLAB脚本是有 `;` 作为休止符的

*   使用 `clear` 来清空变量, `clc` 来情况命令区输出

*   `.*` 通过将对应的元素相乘来将数组 A 和 B 相乘。A 和 B 的大小必须相同或兼容。(<i>即 A和 B都是数组之类的玩意 ?</i> )

    > 作图时貌似是很重要的玩意, 必须要有

*   `meshgrid()` 的使用
    范例: `[X,Y,Z] = meshgrid(x,y,z)`  
    > 当只有 `X` 和 `Y` 参数时, 返回二维坐标点, 反之亦然  
    
    作为参数的 `x` 和 `y` 定义应于此相似: `x = 1:3`  

# 制图相关

## 2D制图

先选择横纵坐标上的元素,如 `x` 和 `y` .  
将 `x` 作为横坐标(狭义),则需要 `x = linspace([起始点,[终止点]])` .  
而令 `y = sin(x)` , 最后使用 `plot(x,y)` 作图

> `linspace` 作用:   
用于产生x1,x2之间的N点行线性的矢量。其中x1、x2、N分别为起始值、终止值、元素个数。若默认N，默认点数为100。

### 添加标识

* `xlabel()` 与 `ylabel()` 分别给 `x` 轴和 `y` 轴添加标识

* `title()` 用于给图标添加标识

### 作图相关

* 改变图线: 通过在 `plot()` 的第三个参数中指定颜色/样式/端点形状.  
稍微具体一点的格式如下:

|颜色|样式|形状|
|----|----|----|
|r|--|o|
|g|:|+|
|b|-.|*|
|c|-|.|
|m|'none'|>|
||还有很多|

* 同时做多个图: 在 `plot()` 完后,执行 `hold on` 再去 `plot()` 下一个.

## 3D制图

先使用 `meshgrid` 生成一组 `(X,Y)` 点, 再声明新的函数因变量, 如 `F = X.*exp(-X.^2-Y.^2);` .  

*   曲面图生成  
    `surf(X,Y,F);`.

    ![`surfc()` 的样子](surfc.png)

*   曲面点图生成  
    `mesh(X,Y,F);`

    > 还有 `meshc()` 和 `meshz()` , `c` 是等高线; 而 `z` 是底部加固体填充. 具体见图片.

![`meshc()`](meshc.png)

![`meshz()`](meshz.png)

![`plot3()`](plot3.png)

>   `surfc()` 相比原来的 `surf()` 是多加了个等高线在 `X-Y` 面上.

- 使用 `colorbar` 来添加颜色栏 

## 子图绘制 `subplot`

```MatlabScript
    subplot(m,n,p);
    subplot(m,n,p,'replace');
    subplot(m,n,p,'align');
```

>   `m` / `n` 指代建立的网格横纵数  
    `p` 指代该图像放在网格的位置 (从左到右数)  

# 编程与脚本

## 创建脚本

使用 `edit [文件名]` 即可.

## 添加注释

在行首添加 `%` .

## 运行脚本

在命令区内输入脚本名称

## 循环语句

```MatlabScript
    for n = 0:MAX
        [Other codes]
    end
```

以上代码展示了自变量 `n` 由0遍历至MAX值的循环语句

> 看起来是使用严格的缩进来进行代码的分层

## 判断语句

```MatlabScript
    if num > 100
        a = 1000
    elseif num < 0
        a = -1
    else
        a = 0
    end
```

(不做过多解释)

