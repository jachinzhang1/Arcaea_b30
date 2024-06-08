# Arcaea b40计算器

该文件为Arcaea b40计算器。用于查看ptt最高的前40首曲目。数据来源：[定数详表 - Arcaea中文维基 (mcd.blue)](https://arcwiki.mcd.blue/定数详表)

可直接运行 `calculate_ptt.py`，生成的 `b40.png`即为查询结果。

程序调用的本地曲目信息记录于 `Arcaea_songs.xlsx`，可在此修改相关曲目游玩的最高记录。表中曲目信息为从上述网站爬取所得，可以更新。但需要注意的是直接对表刷新之后，如果游戏曲目数量发生改变，表的格式将会混乱。因此建议对 `web_data.xlsx`中的表格刷新，然后将 `Arcaea_songs.xlsx`中的数据对照 `web_data.xlsx`更新后的数据修改。（多少有点麻烦但暂时解决不了这个问题）

所用Python解释器版本为3.11，用到的库包括：pandas, dataframe_image, numpy。

之后可能会开发包含图形化界面的查分器（可能吧）

---

2024-05-12更新：

生成的图片命名增加当前日期。

---

2024-03-31更新：

增加了检查 `web_data.xlsx`中的更新曲目功能。对 `web_data.xlsx`中的数据进行刷新之后，可以运行 `check.py`用以检查是否有新增曲目或定数发生变化的曲目。结果会打印输出于控制台。对照该结果对 `Arcaea_songs.xlsx`进行手动曲目修改时就更方便了！
