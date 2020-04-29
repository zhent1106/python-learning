"""
使用python实现emoji表情
参考网站：https://www.unicode.org/emoji/charts/emoji-list.html
"""
import emoji

print(emoji.emojize('老班辛苦了\U0001F49E'))
# 默认的表情可以直接通过表情的字符实现
print(emoji.emojize('Python is :thumbs_up:'))
# 特殊的表情需要指定use_aliases=True参数才可以实现
print(emoji.emojize('Slepping is :zzz:', use_aliases=True))
# 单词形式
print(emoji.emojize('我才不是猪呢！:rolling_on_the_floor_laughing:'))
# 用unicode形式
print(emoji.emojize('\U0001F32D'), emoji.emojize(
    '\U0001F35F'), emoji.emojize('\U0001F354'), emoji.emojize('\U0001F355'))
print(emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),)
print(emoji.emojize('\U0001F495'), emoji.emojize('\U0001F496'),
      emoji.emojize('\U0001F495'), emoji.emojize('\U0001F496'))
