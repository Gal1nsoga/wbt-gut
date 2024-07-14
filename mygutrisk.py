# 代码目的：基于streamlit包生成网页

# 导入包
import pandas as pd
import streamlit as st
import joblib
import pickle

# main function
# 设置网页名称
st.set_page_config(page_title='胃溃疡风险评估工具')

# 设置网页标题
st.header('中老年人胃溃疡风险评估网页工具')

# 设置副标题
st.subheader('欢迎使用本工具！请您输入以下信息进行预测：')

# 添加说明文本
# 长文本会出现滑动条
# st.text('您可使用本工具预测未来4年内发生2型糖尿病的可能性。')
# st.text('请注意，本预测结果仅供参考，实际结果需以医生检查结果为准。')

# 在侧边栏添加图片
# st.sidebar.image('https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', width=200)

# st.title('请您输入以下信息：')

# 在侧边栏添加说明
st.sidebar.info(
    '您可使用本工具预测现在以及未来3年内发生胃溃疡的可能性。请注意，本预测结果仅供参考，实际结果需以医生检查结果为准。')

# Function for online predictions
# 在侧边栏输入预测因子
# 添加滑动条
# factor1 = st.sidebar.selectbox(
#       'Age',
#        ('<50', '50-64', '>=65')
#    )  # 显示列表选择框

# 填写预测变量
# 社会人口学
factor1 = st.radio('性别', ['男性', '女性'], index=None)
factor2 = st.slider('请填写您的年龄', 45, 120, index=None)
factor3 = st.radio('请填写您的民族', ['汉族', '其他'])
factor4 = st.radio('请选择您的学历',
                   ['小学及以下', '小学学历', '初中学历', '高中学历', '大学及以上', '从未上过学', '不清楚'])
factor5 = st.radio('请选择您的婚姻状态', ['已婚', '离异', '丧偶', '未婚', '不清楚'])
factor6 = st.radio('您的生活水平如何？', ['很好', '好', '一般', '不好', '很差', '不清楚'])
factor7 = st.radio('您觉得您的身体状况如何？', ['很好', '好', '一般', '不好', '很差', '不清楚'])
factor8 = st.radio('您觉得您精力充沛吗？', ['总是', '经常', '有时', '偶尔', '从不', '不清楚'])
# 行为学
factor9 = st.radio('您平常主食以什么为主？', ['大米', '全麦谷物', '面粉', '米面各一半', '其他', '不清楚'])
factor10 = st.radio('您吃新鲜水果的频率如何？', ['几乎每天吃', '经常吃', '有时吃', '很少或从不吃', '不清楚'])
factor11 = st.radio('您吃新鲜蔬菜的频率如何？', ['几乎每天吃', '经常吃', '有时吃', '很少或从不吃', '不清楚'])
factor12 = st.radio('您的口味主要是什么？', ['清淡', '偏咸', '偏甜、辣、生冷', '没有以上习惯'])
factor13 = st.radio('meat您吃肉的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor14 = st.radio('您吃鱼的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor15 = st.radio('您吃蛋的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor16 = st.radio('您吃豆制品的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor17 = st.radio('您吃腌制品的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor18 = st.radio('您吃大蒜(蒜苗/蒜黄/蒜苔/青蒜等)的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor19 = st.radio('您吃奶制品（牛奶/奶粉/酸奶/冰淇淋等）的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor20 = st.radio('您吃坚果（花生/核桃/栗子/瓜子等）的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor21 = st.radio('您吃菌藻类食物（蘑菇/木耳/银耳/海带/紫菜等）的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor22 = st.radio('您吃维生素保健品素(A/C/E/钙片等)的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor23 = st.radio('您吃药用植物（人参/黄芪/枸杞子/当归等）的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor24 = st.radio('您喝茶的频率如何？',
                    ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃',
                     '很少或从不吃', '不清楚'])
factor25 = st.radio('您的饮用水主要是什么？', ['井水', '河水或湖水', '泉水', '塘水', '自来水（含纯净水）', '不清楚'])
factor26 = st.radio('您现在是否吸烟？', ['是', '否', '不清楚'])
factor27 = st.radio('您过去是否吸烟？', ['是', '否', '不清楚'])
factor28 = st.radio('您现在是否经常喝酒？', ['是', '否', '不清楚'])
factor29 = st.radio('您过去是否经常喝酒？', ['是', '否', '不清楚'])
factor30 = st.radio('您做家务的频率？', ['每天', '至少一周一次', '至少一月一次', '偶尔', '从不', '不清楚'])
# 疾病史
factor31 = st.radio('您是否患有关节炎？', ['是', '否', '不清楚'])
factor32 = st.radio('您是否患有前列腺疾病？', ['是', '否', '不清楚'])
factor33 = st.radio('您是否患有胆囊炎或胆石症？', ['是', '否', '不清楚'])
factor34 = st.radio('您是否患有血脂异常？', ['是', '否', '不清楚'])
factor35 = st.radio('您是否患有慢性肾炎？', ['是', '否', '不清楚'])
factor36 = st.radio('您是否患有子宫肌瘤？', ['是', '否', '不清楚'])
factor37 = st.radio('您是否患有白内障？', ['是', '否', '不清楚'])
factor38 = st.radio('您是否患有癌症？', ['是', '否', '不清楚'])
factor39 = st.radio('您是否患有心脏病？', ['是', '否', '不清楚'])
factor40 = st.radio('您是否患有中风及脑血管疾病？', ['是', '否', '不清楚'])
factor41 = st.radio('您是否患有风湿或类风湿？', ['是', '否', '不清楚'])
factor42 = st.radio('您是否患有乳腺增生？', ['是', '否', '不清楚'])
factor43 = st.radio('您童年时期是否经常挨饿？', ['是', '否', '不清楚'])
# 体格检查
factor44 = st.slider('请填写您的体重（kg）', 0, 150)
factor45 = st.slider('请填写您的身高（cm）', 0, 200)
factor46 = st.slider('请填写您的腰围（cm）', 0, 130)

# 创建dataframe，用于预测
input_dict = {'a1': factor1, 'trueage': factor2, 'a2': factor3, 'a53a4': factor4,
              'f41': factor5, 'b11': factor6, 'b12': factor7,
              'b23': factor8, 'd1': factor9, 'd31': factor10, 'd32': factor11,
              'd34': factor12, 'd4meat2': factor13, 'd4fish2': factor14, 'd4egg2': factor15,
              'd4bean2': factor16, 'd4veg2': factor17, 'd4garl2': factor18, 'd4milk1': factor19,
              'd4nut1': factor20, 'd4alga1': factor21, 'd4vit1': factor22, 'd4drug1': factor23,
              'd4tea2': factor24, 'd6a': factor25, 'd71': factor26, 'd72': factor27, 'd81': factor28,
              'd82': factor29, 'd11a': factor30, 'g15n1': factor31, 'g15j1': factor32,
              'g15q1': factor33, 'g15r1': factor34, 'g15t1': factor35, 'g15v1': factor36,
              'g15g1': factor37, 'g15i1': factor38, 'g15c1': factor39, 'g15d1': factor40,
              'g15s1': factor41, 'g15u1': factor42, 'f66': factor43, 'g102': factor44,
              'g1021': factor45, 'g102c': factor46}

input_df = pd.DataFrame([input_dict])


# 对dataframe中传入的数据进行编码
def codeing_fun(input_df):
    # 社会人口学
    input_df['a1'] = input_df['a1'].replace(['男性', '女性'], [1, 2])
    input_df['a2'] = input_df['a2'].replace(['汉族', '其他'], [1, 2])
    input_df['a53a4'] = input_df['a53a4'].replace(
        ['小学及以下', '小学学历', '初中学历', '高中学历', '大学及以上', '从未上过学', '不清楚'],
        [0, 1, 2, 3, 4, 5, -1])
    input_df['f41'] = input_df['f41'].replace(['已婚', '离异', '丧偶', '未婚', '不清楚'], [1, 3, 4, 5, -1])
    input_df['b11'] = input_df['b11'].replace(['很好', '好', '一般', '不好', '很差', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['b12'] = input_df['b12'].replace(['很好', '好', '一般', '不好', '很差', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['b23'] = input_df['b23'].replace(['总是', '经常', '有时', '偶尔', '从不', '不清楚'], [1, 2, 3, 4, 5, -1])
    # 行为学
    input_df['d1'] = input_df['d1'].replace(['大米', '全麦谷物', '面粉', '米面各一半', '其他', '不清楚'],
                                            [1, 2, 3, 4, 5, -1])
    input_df['d31'] = input_df['d31'].replace(['几乎每天吃', '经常吃', '有时吃', '很少或从不吃', '不清楚'],
                                              [1, 2, 3, 4, -1])
    input_df['d32'] = input_df['d32'].replace(['几乎每天吃', '经常吃', '有时吃', '很少或从不吃', '不清楚'],
                                              [1, 2, 3, 4, -1])
    input_df['d34'] = input_df['d34'].replace(['清淡', '偏咸', '偏甜、辣、生冷', '没有以上习惯'], [1, 2, 3, -1])
    input_df['d4meat2'] = input_df['d4meat2'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4fish2'] = input_df['d4fish2'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4egg2'] = input_df['d4egg2'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4bean2'] = input_df['d4bean2'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4veg2'] = input_df['d4veg2'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4garl2'] = input_df['d4garl2'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4milk1'] = input_df['d4milk1'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4nut1'] = input_df['d4nut1'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4alga1'] = input_df['d4alga1'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4vit1'] = input_df['d4vit1'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4drug1'] = input_df['d4drug1'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d4tea2'] = input_df['d4tea2'].replace(
        ['几乎每天吃', '不是每天，但每周至少一次', '不是每周，但每月至少一次', '不是每月，但有时吃', '很少或从不吃',
         '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['d6a'] = input_df['d6a'].replace(['井水', '河水或湖水', '泉水', '塘水', '自来水（含纯净水）', '不清楚'],
                                              [1, 2, 3, 4, 5, -1])
    input_df['d71'] = input_df['d71'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['d72'] = input_df['d72'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['d81'] = input_df['d81'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['d82'] = input_df['d82'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['d11a'] = input_df['d11a'].replace(['每天', '至少一周一次', '至少一月一次', '偶尔', '从不', '不清楚'], [1, 2, 3, 4, 5, -1])
    # 疾病史
    input_df['g15n1'] = input_df['g15n1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15j1'] = input_df['g15j1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15q1'] = input_df['g15q1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15r1'] = input_df['g15r1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15t1'] = input_df['g15t1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15v1'] = input_df['g15v1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15g1'] = input_df['g15g1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15i1'] = input_df['g15i1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15c1'] = input_df['g15c1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15d1'] = input_df['g15d1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15s1'] = input_df['g15s1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['g15u1'] = input_df['g15u1'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['f66'] = input_df['f66'].replace(['是', '否', '不清楚'], [1, 2, -1])
    return input_df


# Define function to call
# 定义一个函数，实现导入模型，预测新数据，给出预测概率

# def make_predict(input_df):
#     # Load the trained model for predictions
#     current_model = joblib.load(
#         "/Users/galinsoga/22023482_Xiao/New Gastric Ulcers/Final Results/2018/Model Parameters/sklearn_RF_best_model.sav")  # 使用joblib导入保存好的模型
#     future3yrs_model = joblib.load(
#         "/Users/galinsoga/22023482_Xiao/New Gastric Ulcers/Final Results/2014-2018/Model Parameters/sklearn_AdaBoost_best_model.sav")  # 使用joblib导入保存好的模型
#     # make prediction
#     predict_result_current = current_model.predict(input_df)  # 对输入的数据进行预测
#     predict_result_future3yrs = future3yrs_model.predict(input_df)  # 对输入的数据进行预测
#     # check probability
#     predict_probability_current = current_model.predict_proba(input_df)  # 给出预测概率
#     predict_probability_future3yrs = future3yrs_model.predict_proba(input_df)
#     return predict_result_current, predict_probability_current, predict_result_future3yrs, predict_probability_future3yrs
#

# # 设置一个按钮用于预测
# if st.button('点击进行预测'):
#     input_df1 = codeing_fun(input_df=input_df)
#
#     # make prediction from the input data
#     current_result, current_probability, future3yrs_result, future3yrs_probability = make_predict(input_df=input_df1)
#
#     # Display results of the current model prediction
#     st.header('对于目前患有胃溃疡：')
#
#
#     if int(current_result) == 1:
#         st.write("您可能属于高危人群",
#                  current_probability[0, 1])
#     else:
#         st.write("您可能属于低危人群",
#                  current_probability[0, 0])
#
#     # Display results of the future 3-year risk model prediction
#     st.header('对于未来三年患有胃溃疡：')
#     if int(future3yrs_result) == 1:
#         st.write("您可能属于高危人群",
#                  future3yrs_probability[0, 1])
#     else:
#         st.write("您可能属于低危人群",
#                  future3yrs_probability[0, 0])
def make_predict(input_df):
    # Load the trained model for predictions
    with open("sklearn_RF_best_model.sav", "rb") as f:
        model = pickle.load(f)
    # model = joblib.load("sklearn_RF_best_model.sav")  # 使用joblib导入保存好的模型

    # make prediction
    predict_result = model.predict(input_df)  # 对输入的数据进行预测

    # check probability
    predict_probability = model.predict_proba(input_df)  # 给出预测概率
    return predict_result, predict_probability


# 设置一个按钮用于预测
if st.button('点击进行预测'):
    input_df1 = codeing_fun(input_df=input_df)

    # make prediction from the input data
    result, probability = make_predict(input_df=input_df1)

    # Display results of the task
    st.header('您的胃溃疡风险：')

    if int(result) == 1:
        st.write("您可能属于高危人群")
                 # probability[:, 1])
    else:
        st.write("您可能属于低危人群")
                 # probability[:, 0])
