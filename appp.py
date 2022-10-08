import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as plt
# matplotlib.use('Agg')
# import seaborn as sns
# import altair as alt
# from vega_datasets import data
import plotly.express as px



# df = pd.read_csv("C:/data_015.csv", sep=",", encoding='cp949')

df2 = pd.read_csv('C:/sinbig/sinbig/user_fin.csv')
st.dataframe(df2.head())

fig1 = px.bar(df2, x='P2', y="P2_count", color="P1", title="연령대별 신한 계열사 이용 남녀 비율")
# st.plotly_chart(fig1)
# fig1.show()
# fig1.write_image("fig1.png") #아니 kaleido 사용하면 저장된다며



fig2 = px.pie(df2, values='consumer_count', names="consumer_type", title='신한라이프 활동 고객 비율')      #plotly pie차트
st.plotly_chart(fig2)



fig3 = px.pie(df2, values='age_total', names="age", title='신한라이프 활동 고객 연령대 비율')      #plotly pie차트
st.plotly_chart(fig3)

fig33 = px.histogram(df2, y='숫자', x="나이2개", color="연령별 고객유형", barmode='group', title='연령대별 고객, 비고객 그래프')
# fig33.show()

fig4 = px.histogram(df2, y='P3_count', x="P2", color="P1", barmode='group', title='신한은행 활동 고객 비율')
# st.plotly_chart(fig4)
# fig4.show()
#
fig5 = px.histogram(df2, y='P4_count', x="P2",color="P1", barmode='group', title='신한카드 우수 고객 비율')
# st.plotly_chart(fig5)
# fig5.show()
#
fig6 = px.histogram(df2, y='P5_count', x="P2", color="P1", barmode='group', title='신한금투 활동 고객 비율')
# st.plotly_chart(fig6)
# fig6.show()

fig7 = px.bar(df2, x="종류", y="고객수", color="나이", title="결제은행")
# st.plotly_chart(fig7)
# fig7.show()
#
fig8 = px.bar(df2, x="종류1", y="고객수1", color="나이1", title="결제증권사")
# st.plotly_chart(fig8)
# fig8.show()

#---20대
# ---

df = pd.read_csv('C:/sinbig/sinbig/graph_data.csv')
st.dataframe(df.head())

fig9 = px.pie(df, values='20대_총사용금액', names="소비유형", title='20대 소비유형 대분류')      #plotly pie차트
st.plotly_chart(fig9)
# fig9.show()

fig14 = px.bar(df, x="2세부소비유형1순위", y="20대_사용금액1", title="20대 세부소비유형 1순위")
st.plotly_chart(fig14)

fig15 = px.bar(df, x="2세부소비유형2순위", y="20대_사용금액2", title="20대 세부소비유형 2순위")
st.plotly_chart(fig15)

fig16 = px.bar(df, x="2세부소비유형3순위", y="20대_사용금액3", title="20대 세부소비유형 3순위")
st.plotly_chart(fig16)

#---30대
# ---

fig10 = px.pie(df, values='30대_총사용금액', names="소비유형", title='30대 소비유형 대분류')      #plotly pie차트
st.plotly_chart(fig10)

fig17 = px.bar(df, x="3세부소비유형1순위", y="30대_사용금액1", title="30대 세부소비유형 1순위")
st.plotly_chart(fig17)

fig18 = px.bar(df, x="3세부소비유형2순위", y="30대_사용금액2", title="30대 세부소비유형 2순위")
st.plotly_chart(fig18)

fig19 = px.bar(df, x="3세부소비유형3순위", y="30대_사용금액3", title="30대 세부소비유형 3순위")
# st.plotly_chart(fig19)

#---40대
# ---

fig11 = px.pie(df, values='40대_총사용금액', names="소비유형", title='40대 소비유형 대분류')      #plotly pie차트
st.plotly_chart(fig11)

fig20 = px.bar(df, x="4세부소비유형1순위", y="40대_사용금액1", title="40대 세부소비유형 1순위")
st.plotly_chart(fig20)

fig21 = px.bar(df, x="4세부소비유형2순위", y="40대_사용금액2", title="40대 세부소비유형 2순위")
st.plotly_chart(fig21)

fig22 = px.bar(df, x="4세부소비유형3순위", y="40대_사용금액3", title="40대 세부소비유형 3순위")
# st.plotly_chart(fig22)

#---50대
# ---

fig12 = px.pie(df, values='50대_총사용금액', names="소비유형", title='50대 소비유형 대분류')      #plotly pie차트
st.plotly_chart(fig12)

fig23 = px.bar(df, x="5세부소비유형1순위", y="50대_사용금액1", title="50대 세부소비유형 1순위")
st.plotly_chart(fig23)

fig24 = px.bar(df, x="5세부소비유형2순위", y="50대_사용금액2", title="50대 세부소비유형 2순위")
st.plotly_chart(fig24)

fig25 = px.bar(df, x="5세부소비유형3순위", y="50대_사용금액3", title="50대 세부소비유형 3순위")
# st.plotly_chart(fig25)

#---60대
# ---

fig13 = px.pie(df, values='60대_총사용금액', names="소비유형", title='60대 소비유형 대분류')      #plotly pie차트
st.plotly_chart(fig13)

fig26 = px.bar(df, x="6세부소비유형1순위", y="60대_사용금액1", title="60대 세부소비유형 1순위")
st.plotly_chart(fig26)

fig27 = px.bar(df, x="6세부소비유형2순위", y="60대_사용금액2", title="60대 세부소비유형 2순위")
st.plotly_chart(fig27)

fig28 = px.bar(df, x="6세부소비유형1순위", y="60대_사용금액3", title="60대 세부소비유형 3순위")
st.plotly_chart(fig28)

#---

fig29 = px.pie(df, values='total_사용금액', names="소비유형", title='전체 고객 소비유형 비율')      #plotly pie차트
st.plotly_chart(fig29)


#---혼합차트1
# <바차트>
# fig30 = px.bar(df2, x="나이", y="가격", color="소비유형", barmode="group")
# # st.plotly_chart(fig30)
# fig30.update_layout(title_font_size=24)
# fig30.update_xaxes(showgrid=True)

# <scatter차트>
fig30 = px.scatter(df2, x="가격", y="나이분류", size="나이대별 비고객수", color="소비유형", hover_name="소비유형_세부", size_max=60,title="연령대별 신한라이프 비고객 소비패턴 파악(X축 : 지출액 log그래프)")
st.plotly_chart(fig30)
# fig30.show()


#---혼합차트2

df3 = pd.read_csv('C:/sinbig/sinbig/totalgraph2.csv')
fig31 = px.scatter(df3, x="세부소비 유형", y="지출액" , color="나이", size="사이즈", hover_name="소비유형", title = "연령대별 소비유형 분포도(Y축 : 지출액 log그래프)")
st.plotly_chart(fig31)
# fig31.show()


#---혼합차트3
df4 = pd.read_csv("C:/sinbig/sinbig/totalgraph3.csv")
fig32 = px.scatter(df4, x="나이분류", y="가격", size="컬럼갯수", color="소비유형", hover_name="소비유형_세부", size_max=60,title="세부소비 유형별 지출액 소비패턴 파악(Y축 : 지출액 log그래프)")
st.plotly_chart(fig32)
# fig32.show()

    #
    # for i in range(0,32):
    #     i += 1
    #     print(i)
    # return f"fig{i}.show()"






