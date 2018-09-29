计算MovieLens 100k数据集中男性女性用户评分的标准差并输出。

数据集下载http://files.grouplens.org/datasets/movielens/ml-100k.zip

其中u.data 表示100k条评分记录，每一列的数值含义是：

user id | item id | rating | timestamp

u.user表示用户的信息，每一列的数值含义是：

user id | age | gender | occupation | zip code

u.item文件表示电影的相关信息，每一列的数值含义是：

movie id | movie title | release date | video release date |IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |

可能会用到的相关函数：

pandas.read_table(filepath_or_buffer, sep='\t', names=None)

pandas.pivot_table(data, values=None, columns=None, aggfunc='mean')

pandas.merge(left, right, how='inner')

更详尽的API文档请参考http://pandas.pydata.org/pandas-docs/stable/。

输出结果：

Gender

M *

F	*

结论：标准差高的评分差异大

注意：先分别计算每个人电影评分的平均分再按性别求标准差

请将男女评分（保留2位小数）组合后放到一个txt文件中通过网络提交，例如：如果两者评分的标准差分别是

男：0.32

女：0.35

则提交：

3235