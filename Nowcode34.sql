/*
# Problem: 统计复旦用户8月练题情况
# Problem Number: 牛客sql34
# Difficulty: Hard
# Link: https://www.nowcoder.com/practice/53235096538a456b9220fce120c062b3?tpId=199&tqId=1980673&ru=/exam/oj&qru=/ta/sql-quick-study/question-ranking&sourceUrl=%2Fexam%2Foj

描述
题目： 现在运营想要了解复旦大学的每个用户在8月份练习的总题目数和回答正确的题目数情况，请取出相应明细数据，对于在8月份没有练习过的用户，答题数结果返回0.

示例：用户信息表user_profile
id	device_id	gender	age	university	gpa	active_days_within_30
1	2138	male	21	北京大学	3.4	7
2	3214	male		复旦大学	4.0	15
3	6543	female	20	北京大学	3.2	12
4	2315	female	23	浙江大学	3.6	5
5	5432	male	25	山东大学	3.8	20
6	2131	male	28	山东大学	3.3	15
7	4321	female	26	复旦大学	3.6	9示例：question_practice_detail
id	device_id	question_id	result	date
1	2138	111	wrong	2021-05-03
2	3214	112	wrong
2021-05-09
3	3214	113	wrong
2021-06-15
4	6543	111	right	2021-08-13
5	2315	115	right
2021-08-13
6	2315	116	right
2021-08-14
7	2315	117	wrong
2021-08-15





根据示例，你的查询应返回以下结果：
device_id
university	question_cnt	right_question_cnt
3214	复旦大学	3	0
4321	复旦大学	0	0



*/

#solution
SELECT
    up.device_id,
    university,
    count(qpd.question_id) as question_cnt,
    sum(if (qpd.result = 'right', 1, 0)) as right_question_cnt
FROM
    user_profile up
    LEFT JOIN question_practice_detail qpd ON qpd.device_id = up.device_id AND month (qpd.date) = 8
    
WHERE
    up.university = '复旦大学' 
GROUP BY
    up.device_id;