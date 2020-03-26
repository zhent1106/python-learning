"""
百分制成绩转换等级制成绩
"""
score = float(input('请输入成绩'))
if score >= 90:
    grade = '优秀'
elif score >= 80:
    grade = '良好'
elif score >= 70:
    grade = '中等'
elif score >= 60:
    grade = '及格'
else:
    grade = '不及格'
print('对应的成绩等级：', grade)
