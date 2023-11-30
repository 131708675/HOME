import pandas as pd
from pyreadstat import pyreadstat
import
plt.rcparams["font.sans-serif"]=["SimHei"]#设置字体
def 有序类别变量描述统计函数(表名,变量名):
    result=表名[变量名].value_counts(sort=False)
    描述统计表= pd.DataFrame(result)
    描述统计表['比例'] = 描述统计表['count']/ 描述统计表['count'].sum()
    描述统计表['累计比例'] = 描述统计表['比例'] .cumsum ()
    return 描述统计表
def 绘制单类别柱状图(数据表,变量):
    绘制单个类别变量柱状
    x=数据表[变量].value_counts().index
    y=数据表[变量].
def 数据变量描述统计(数据表,变量名):
    result=数据表[变量名].describe()
    中位数=result['median']
    平均值=result['mean']
    标准值=result['std']
    return  中位数,平均值,标准值
def 制作交叉表(数据表,自变量,因变量):
    return pd.crosstab(数据表[自变量],数据表[因变量],normalize='columns')
    margins=True
import pandas as pd
from scipy import stats

def 单变量参数估计(file_path, confidence_level): 
 file_path = R"movie_data_cleaned.csv"
df_movies = pd.read_csv(file_path)
#计算均值和标准误差
mean = df_movies['average'].mean()
std_error = stats.sem(df_movies['average'])
# 设定置信水平
confidence_level = 0.95
# 设定自由度
自由度 = len(df_movies['average']) - 1
# 计算置信区间
confidence_interval = stats.t.interval(confidence_level, 自由度, loc=mean, scale=std_error)
# 输出结果
print(F"均值：{mean: .2f}")
print(F"均值在置信水平{confidence_level}下的置信区间为：", confidence_interval)