'''
pyecharts绘制柱状图
'''
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 第一幅图，数据固定
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(['服饰', '箱包', '鞋帽', '电子', '数码', '户外'])
    .add_yaxis('京东', [5, 23, 32, 12, 54, 90])
    .add_yaxis('天猫', [15, 6, 32, 74, 54, 90])
    .set_global_opts(title_opts=opts.TitleOpts(title='电商销售对比'))
)
bar.render(path='./res/电商销售对比.html')
# 第二幅图，数据分离
items = ['Java', 'C', 'Python', 'C++', 'JavaScript', 'C#', 'PHP', 'SQL']
data_list1 = [188, 166, 110, 108, 90, 80, 55, 45]
data_list2 = [190, 160, 140, 100, 80, 70, 50, 40]
bar1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(items)
    .add_yaxis('2020年', data_list1)
    .add_yaxis('2019年', data_list2)
    .set_global_opts(title_opts=opts.TitleOpts(title='编程语言排行', subtitle='2019-2020'))
)
bar1.render(path='./res/编程语言排行.html')

# 第三幅，疫情分析
items = ['美国', '西班牙', '意大利', '德国', '中国', '法国', '伊朗', '英国', '土耳其', '比利时']
data_list1 = [432438, 152446, 139887, 108202,
              83264, 82048, 67286, 60733, 38226, 24983]
data_list2 = [14808, 15238, 17669, 2107, 3344, 10328, 4110, 7097, 812, 2523]
bar2 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(items)
    .add_yaxis('累计确诊', data_list1)
    .add_yaxis('累计死亡', data_list2)
    .set_global_opts(title_opts=opts.TitleOpts(title='全球疫情分析', subtitle='2020-4-9 20：41'))
)
bar2.render(path='./res/全球疫情图49.html')
