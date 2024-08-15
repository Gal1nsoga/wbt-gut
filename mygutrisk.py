# 代码目的：基于streamlit包生成网页

# 导入包
import pandas as pd
import streamlit as st
import joblib
import pickle

# main function
# 设置网页名称
st.set_page_config(page_title='Gastric Ulcer Risk Prediction Tool')

# 设置网页标题
st.header('Middle-aged and Elderly Gastric Ulcer Risk Assessment Web Tool.\n中老年人胃溃疡风险评估网页工具')

# 设置副标题
st.subheader('Welcome to use this tool! Please enter the following information for prediction:\n欢迎使用本工具！请您输入以下信息进行预测：')

# 添加说明文本
# 长文本会出现滑动条
# st.text('您可使用本工具预测未来4年内发生2型糖尿病的可能性。')
# st.text('请注意，本预测结果仅供参考，实际结果需以医生检查结果为准。')

# 在侧边栏添加图片
# st.sidebar.image('https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', width=200)

# st.title('请您输入以下信息：')

# 在侧边栏添加说明
st.sidebar.info(
    "You can use this tool to predict the likelihood of having a stomach ulcer. Please note that the prediction is for reference only, and the actual results should be confirmed by a doctor's examination.\n您可使用本工具预测现在发生胃溃疡的可能性。请注意，本预测结果仅供参考，实际结果需以医生检查结果为准。")
st.sidebar.info("This machine learning program was developed using the CLHLS database. After using this program, you will understand your current risk level of having gastic ulcer. This program helps in the early detection and treatment of gastric ulcer, thereby reducing the public health burden associated with gastric ulcer.\n这个机器学习程序是使用CLHLS数据库开发的。使用这个程序后，您将了解您目前患胃溃疡的风险水平。这个程序有助于早期检测和治疗胃溃疡，从而减轻与胃溃疡相关的公共卫生负担。")                                  
# Function for online predictions
# 在侧边栏输入预测因子
# 添加滑动条
# factor1 = st.sidebar.selectbox(
#       'Age',
#        ('<50', '50-64', '>=65')
#    )  # 显示列表选择框

# 填写预测变量
# 社会人口学
factor1 = st.radio('Gender (性别)', ['Male (男性)', 'Female (女性)'], index=None)
factor2 = st.slider('Age (请填写您的年龄)', 45, 120)
factor3 = st.radio('Ethnicity (请填写您的民族)', ['Han (汉族)', 'Others (其他)'], index=None)
factor4 = st.radio('Education Level (请选择您的学历)',
                   ['Up to and including primary/elementary school (小学及以下)', 'Completed primary/elementary school (小学学历)', 'Completed junior high/middle school (初中学历)', 'High school/secondary school education (高中学历)', 'College/university education or higher (大学及以上)', 'Never went to school (从未上过学)', 'Unclear (不清楚)'], index=None)
factor5 = st.radio('Your marital status (请选择您的婚姻状态)', ['Married (已婚)', 'Divorced (离异)', 'Widowed (丧偶)', 'Single (未婚)', 'Unclear (不清楚)'], index=None)
factor6 = st.radio('Your standard of living? (您的生活水平如何？)', ['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], index=None)
factor7 = st.radio("How's your physical condition? (您觉得您的身体状况如何？)", ['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], index=None)
factor8 = st.radio('Do you feel energetic? (您觉得您精力充沛吗？)', ['Always (总是)', 'Often (经常)', 'Sometimes (有时)', 'Occasionally (偶尔)', 'Never (从不)', 'Unclear (不清楚)'], index=None)
# 行为学
factor9 = st.radio("What's your staple? (您平常主食以什么为主？)", ['Rice (大米)', 'Whole grains (全麦谷物)', 'Flour (面粉)', 'Half rice and half flour (米面各一半)', 'Others (其他)', 'Unclear (不清楚)'], index=None)
factor10 = st.radio('How often do you eat fresh fruits? (您吃新鲜水果的频率如何？)', ['Almost every day (几乎每天吃)', 'Often (经常吃)', 'Sometimes (有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor11 = st.radio('How often do you eat fresh vegetables? (您吃新鲜蔬菜的频率如何？)', ['Almost every day (几乎每天吃)', 'Often (经常吃)', 'Sometimes (有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor12 = st.radio('What is your primary taste preference? (您的口味主要是什么？)', ['Light (清淡)', 'Salty (偏咸)', 'Sweet, Spicy, Cold (偏甜、辣、生冷)', 'None of the above habits (没有以上习惯)'], index=None)
factor13 = st.radio('How often do you eat meat? (您吃肉的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor14 = st.radio('How often do you eat fish?  (您吃鱼的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor15 = st.radio('How often do you eat eggs? (您吃蛋的频率如何？)',
                   ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor16 = st.radio('How often do you eat soy products? (您吃豆制品的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor17 = st.radio('How often do you eat pickled foods? (您吃腌制品的频率如何？)',
                   ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor18 = st.radio('How often do you eat garlic (garlic sprouts/green garlic/leeks/chives, etc.)? (您吃大蒜(蒜苗/蒜黄/蒜苔/青蒜等)的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor19 = st.radio('How often do you consume dairy products (milk/powdered milk/yogurt/ice cream, etc.)? (您吃奶制品（牛奶/奶粉/酸奶/冰淇淋等）的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor20 = st.radio('How often do you eat nuts (peanuts/walnuts/chestnuts/sunflower seeds, etc.)? (您吃坚果（花生/核桃/栗子/瓜子等）的频率如何？)',
                   ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor21 = st.radio('How often do you eat fungi and algae foods (mushrooms/wood ear fungus/silver ear fungus/seaweed/nori, etc.)? (您吃菌藻类食物（蘑菇/木耳/银耳/海带/紫菜等）的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor22 = st.radio('How often do you take vitamin supplements (A/C/E, calcium tablets, etc.)? (您吃维生素保健品素(A/C/E/钙片等)的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor23 = st.radio('How often do you consume medicinal herbs (ginseng/astragalus/wolfberries/angelica, etc.)? (您吃药用植物（人参/黄芪/枸杞子/当归等）的频率如何？)',
                   ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor24 = st.radio('How often do you drink tea? (您喝茶的频率如何？)',
                    ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], index=None)
factor25 = st.radio('What is your primary source of drinking water?  (您的饮用水主要是什么？)', ['Well water (井水)', 'River or lake water (河水或湖水)', 'Spring water (泉水)', 'Pond water (塘水)', 'Tap water (including purified water) (自来水（含纯净水）)', 'Unclear (不清楚)'], index=None)
factor26 = st.radio('Are you currently smoking? (您现在是否吸烟？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor27 = st.radio('Did you smoke in the past? (您过去是否吸烟？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor28 = st.radio('Do you currently drink alcohol regularly? (您现在是否经常喝酒？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor29 = st.radio('Did you used to drink alcohol regularly in the past? (您过去是否经常喝酒？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor30 = st.radio('How often do you do household chores? (您做家务的频率？)', ['Every day (每天)', 'At least once a week (至少一周一次)', 'At least once a month (至少一月一次)', 'Occasionally (偶尔)', 'Never (从不)', 'Unclear (不清楚)'], index=None)
# 疾病史
factor31 = st.radio('Do you suffer from arthritis? (您是否患有关节炎？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor32 = st.radio('Do you suffer from prostate disease? (您是否患有前列腺疾病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor33 = st.radio('Do you suffer from cholecystitis or cholelithiasis? (您是否患有胆囊炎或胆石症？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor34 = st.radio('Do you have abnormal blood lipids? (您是否患有血脂异常？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor35 = st.radio('Do you have chronic nephritis? (您是否患有慢性肾炎？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor36 = st.radio('Do you have uterine fibroids? (您是否患有子宫肌瘤？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor37 = st.radio('Do you have cataracts? (您是否患有白内障？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor38 = st.radio('Do you have cancer? (您是否患有癌症？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor39 = st.radio('Do you have heart disease? (您是否患有心脏病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor40 = st.radio('Do you have a history of stroke or cerebrovascular disease? (您是否患有中风及脑血管疾病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor41 = st.radio('Do you have rheumatism or rheumatoid arthritis? (您是否患有风湿或类风湿？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor42 = st.radio('Do you have breast hyperplasia? (您是否患有乳腺增生？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
factor43 = st.radio('Did you often starve during your childhood? (您童年时期是否经常挨饿？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index=None)
# 体格检查
factor44 = st.slider('Please fill in your weight(kg) (请填写您的体重（kg）)', 0, 150)
factor45 = st.slider('Please fill in your height(cm) (请填写您的身高（cm）)', 0, 200)
factor46 = st.slider('Please fill in your waist circumference(cm) (请填写您的腰围（cm）)', 0, 130)

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
    input_df['a1'] = input_df['a1'].replace(['Male (男性)', 'Female (女性)'], [1, 2])
    input_df['a2'] = input_df['a2'].replace(['Han (汉族)', 'Others (其他)'], [1, 2])
    input_df['a53a4'] = input_df['a53a4'].replace(
        ['Up to and including primary/elementary school (小学及以下)', 'Completed primary/elementary school (小学学历)', 'Completed junior high/middle school (初中学历)', 'High school/secondary school education (高中学历)', 'College/university education or higher (大学及以上)', 'Never went to school (从未上过学)', 'Unclear (不清楚)'],
        [0, 1, 2, 3, 4, 5, -1])
    input_df['f41'] = input_df['f41'].replace(['Married (已婚)', 'Divorced (离异)', 'Widowed (丧偶)', 'Single (未婚)', 'Unclear (不清楚)'], [1, 3, 4, 5, -1])
    input_df['b11'] = input_df['b11'].replace(['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['b12'] = input_df['b12'].replace(['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['b23'] = input_df['b23'].replace(['Always (总是)', 'Often (经常)', 'Sometimes (有时)', 'Occasionally (偶尔)', 'Never (从不)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    # 行为学
    input_df['d1'] = input_df['d1'].replace(['Rice (大米)', 'Whole grains (全麦谷物)', 'Flour (面粉)', 'Half rice and half flour (米面各一半)', 'Others (其他)', 'Unclear (不清楚)'],
                                            [1, 2, 3, 4, 5, -1])
    input_df['d31'] = input_df['d31'].replace(['Almost every day (几乎每天吃)', 'Often (经常吃)', 'Sometimes (有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'],
                                              [1, 2, 3, 4, -1])
    input_df['d32'] = input_df['d32'].replace(['Almost every day (几乎每天吃)', 'Often (经常吃)', 'Sometimes (有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'],
                                              [1, 2, 3, 4, -1])
    input_df['d34'] = input_df['d34'].replace(['Light (清淡)', 'Salty (偏咸)', 'Sweet, Spicy, Cold (偏甜、辣、生冷)', 'None of the above habits (没有以上习惯)'], [1, 2, 3, -1])
    input_df['d4meat2'] = input_df['d4meat2'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4fish2'] = input_df['d4fish2'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4egg2'] = input_df['d4egg2'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4bean2'] = input_df['d4bean2'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4veg2'] = input_df['d4veg2'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4garl2'] = input_df['d4garl2'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4milk1'] = input_df['d4milk1'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4nut1'] = input_df['d4nut1'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4alga1'] = input_df['d4alga1'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4vit1'] = input_df['d4vit1'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4drug1'] = input_df['d4drug1'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d4tea2'] = input_df['d4tea2'].replace(
        ['Almost every day (几乎每天吃)', 'Not every day, but at least once a week (不是每天，但每周至少一次)', 'Not every week, but at least once a month (不是每周，但每月至少一次)', 'Not every month, but sometimes (不是每月，但有时吃)', 'Rarely or never (很少或从不吃)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['d6a'] = input_df['d6a'].replace(['Well water (井水)', 'River or lake water (河水或湖水)', 'Spring water (泉水)', 'Pond water (塘水)', 'Tap water (including purified water) (自来水（含纯净水）)', 'Unclear (不清楚)'],
                                              [1, 2, 3, 4, 5, -1])
    input_df['d71'] = input_df['d71'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['d72'] = input_df['d72'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['d81'] = input_df['d81'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['d82'] = input_df['d82'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['d11a'] = input_df['d11a'].replace(['Every day (每天)', 'At least once a week (至少一周一次)', 'At least once a month (至少一月一次)', 'Occasionally (偶尔)', 'Never (从不)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    # 疾病史
    input_df['g15n1'] = input_df['g15n1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15j1'] = input_df['g15j1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15q1'] = input_df['g15q1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15r1'] = input_df['g15r1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15t1'] = input_df['g15t1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15v1'] = input_df['g15v1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15g1'] = input_df['g15g1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15i1'] = input_df['g15i1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15c1'] = input_df['g15c1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15d1'] = input_df['g15d1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15s1'] = input_df['g15s1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['g15u1'] = input_df['g15u1'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['f66'] = input_df['f66'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
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


# 设置一个按钮用于进行预测
if st.button('Please click the button to predict (请点击进行预测)'):
    # 检查是否完成了所有选项
    if input_df.isnull().values.any():
        st.warning("You have unfinished questions, please make sure you have completed all of them！\n您有问题未完成，请确保完成了所有选项！")
    else:
        # 在这里执行预测相关的代码
        input_df1 = codeing_fun(input_df=input_df)
        result, probability = make_predict(input_df=input_df1)
        
        # 显示结果
        st.header('Your gastric ulcer risk level:\n您的胃溃疡风险等级：')
        if int(result) == 1:
            st.write("You may belong to a high-risk group.\n您可能属于高危人群")
            # 这里可以选择是否显示概率
            # st.write(f"概率：{probability}")
        else:
            st.write("You may belong to a low-risk group.\n您可能属于低危人群")
            # st.write(f"概率：{1 - probability}")
