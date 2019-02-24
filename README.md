# CSDN-Blog-Saver
CSDN博客保存到本地(markdown源码) 技术栈：python  selenium





### 运行环境

目前只支持**windows**            已测试：win10.0.17134   Python3.6.2

第三方包见requirements.txt

代码中浏览器使用的是Chrome     如使用其他浏览器，自行改动相应代码部分即可





### 使用方法

**stage0:**

`pip install -r requirements.txt`



**stage1: 获取目标博客id列表**

![img](https://s2.ax1x.com/2019/02/24/k4vxNq.png)

`python  get_article_list.py`   注意修改用户名



**stage2: 根据获得的id获取markdown源码**

![img](https://s2.ax1x.com/2019/02/24/k4xKgO.png)

`python  get_article_markdown `     注意修改用户名和密码





### 结果示例

https://blog.csdn.net/Feynman1999/article/details/82874491



![img](https://s2.ax1x.com/2019/02/24/k4xgP0.png)





### 待改进（从上至下优先级降低）

* 多线程
* 兼容linux系统(ubantu)

* 如何保持每一次测试时不用再次登录?

* 重构代码，面向对象抽象





### 可能的运行错误

由于网络环境和硬件性能的差异，代码time.sleep的时间自行调节，我测试时是没问题的
