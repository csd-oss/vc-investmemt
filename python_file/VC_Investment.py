# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# + [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/csd-oss/vc-investmemt/blob/master/VC_Investment.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + [markdown] id="e0EkCRLhB8XL" colab_type="text"
# # General preparation and GDrive conection

# + id="I0OTz1Y-V09P" colab_type="code" colab={}
import pandas as pd 
import matplotlib.pyplot as plt

# + [markdown] id="pc_kqSO1CKX3" colab_type="text"
# # Uploiding info from [OECD](https://stats.oecd.org/Index.aspx?DataSetCode=VC_INVEST#)

# + id="l8R-BCD8YRB0" colab_type="code" colab={}
vc_path = "https://raw.githubusercontent.com/csd-oss/vc-investmemt/master/VC_INVEST_06042020205501847.csv"
df = pd.read_csv(vc_path)
df

# + [markdown] id="mAzK8NNGCvkH" colab_type="text"
# ## Droping all not needed info

# + id="8V7ELJS_bSPw" colab_type="code" colab={}
df = df.drop(columns=["Reference Period Code","Reference Period","Flag Codes","Flags","SUBJECT","Measure","Unit","Year","Subject","SUBJECT","Development stages"])
df

# + [markdown] id="EJqEB8hSC1x-" colab_type="text"
# ## Deviding data into 2 dataframes

# + id="uczeMMp4BSCh" colab_type="code" colab={}
df_usd = df.query('MEASURE == "USD_V"')
df_gdp = df.query('MEASURE == "SH_GDP"')

# + [markdown] id="fFL61sLwDFVi" colab_type="text"
# # Playing with USD data

# + [markdown] id="wdUMgWsbb9BF" colab_type="text"
# ## Creating filters

# + id="XlpRf_ziDQmP" colab_type="code" colab={}
filt_total_us = (df_usd['STAGES'] == "VC_T") & (df_usd['LOCATION']== "USA")
filt_seed_us = (df_usd['STAGES'] == "SEED") & (df_usd['LOCATION']== "USA")
filt_start_us = (df_usd['STAGES'] == "START") & (df_usd['LOCATION']== "USA")
filt_later_us = (df_usd['STAGES'] == "LATER") & (df_usd['LOCATION']== "USA")

# + [markdown] id="FQIoM-2BcBLh" colab_type="text"
# ## Ploting US VC data 

# + id="CUlOwveFZ2SC" colab_type="code" colab={}
fig, ax = plt.subplots()
plt.style.use("ggplot")
ax.plot(df_usd.loc[filt_total_us].TIME, df_usd.loc[filt_total_us].Value, label = "Total")
ax.plot(df_usd.loc[filt_seed_us].TIME, df_usd.loc[filt_seed_us].Value, label = "Seed")
ax.plot(df_usd.loc[filt_start_us].TIME, df_usd.loc[filt_start_us].Value, label = "Series A")
ax.plot(df_usd.loc[filt_later_us].TIME, df_usd.loc[filt_later_us].Value, label = "Later Stages")

ax.set_xlabel("Years")
ax.set_label("Millions US$")
ax.set_title("USA VC investment")
ax.grid(True)
ax.legend()
plt.show()

# + [markdown] id="QdrPA0ctv-bB" colab_type="text"
# # Playing with GDP data

# + id="u3d_GB5mwGty" colab_type="code" colab={}
filt_total_us = (df_gdp['STAGES'] == "VC_T") & (df_gdp['LOCATION']== "USA")
filt_seed_us = (df_gdp['STAGES'] == "SEED") & (df_gdp['LOCATION']== "USA")
filt_start_us = (df_gdp['STAGES'] == "START") & (df_gdp['LOCATION']== "USA")
filt_later_us = (df_gdp['STAGES'] == "LATER") & (df_gdp['LOCATION']== "USA")

# + id="SdtkpjwnweEa" colab_type="code" colab={}
fig, ax = plt.subplots()
plt.style.use("ggplot")
ax.plot(df_gdp.loc[filt_total_us].TIME, df_gdp.loc[filt_total_us].Value, label = "Total")
ax.plot(df_gdp.loc[filt_seed_us].TIME, df_gdp.loc[filt_seed_us].Value, label = "Seed")
ax.plot(df_gdp.loc[filt_start_us].TIME, df_gdp.loc[filt_start_us].Value, label = "Series A")
ax.plot(df_gdp.loc[filt_later_us].TIME, df_gdp.loc[filt_later_us].Value, label = "Later Stages")

ax.set_xlabel("Years")
ax.set_label("%GDP")
ax.set_title("USA VC investment")
ax.grid(True)
ax.legend()
plt.show()

# + [markdown] id="aMUqCt75qfxq" colab_type="text"
# # Countries Yearly Sum

# + id="6-yrqLZD2Dfy" colab_type="code" colab={}
filt_total = (df_usd['STAGES'] == "VC_T") & (df_usd['TIME'] >= 2007) #not enoght data till 2007
df_usd[filt_total].groupby(['TIME'])['Value'].sum().plot()
plt.title('Total investment')
plt.ylabel('Millions USD')
plt.show()

# + [markdown] id="XPWlyh2HxVkn" colab_type="text"
# # Countries Yearly mean GDP Share

# + id="izQ7TKLPxc3H" colab_type="code" colab={}
filt_total = (df_gdp['STAGES'] == "VC_T") & (df_gdp['TIME'] >= 2007) #not enoght data till 2007
df_gdp[filt_total].groupby(['TIME'])['Value'].mean().plot()
plt.title('Total investment')
plt.ylabel('% GDP')
plt.show()

# + [markdown] id="6FZ5yJNVG8PI" colab_type="text"
# # 2018 Pie Chart creation

# + id="1DgU_CoSHTGI" colab_type="code" colab={}
filt_total_2018 = (df_usd['TIME']==2018)&(df_usd['STAGES']=='VC_T') 
filt_other = df_usd['Value'] > 2185.094678
pie_2018 = df_usd[filt_total_2018 & filt_other]
pie_2018.drop(columns=['STAGES','MEASURE','TIME','Unit Code','PowerCode Code','PowerCode'], inplace=True)
pie_2018

# + id="0GQyhHWPeMzm" colab_type="code" colab={}
pie_2018.loc[1]=['OTH', 'Other', df_usd[filt_total_2018 & ~filt_other]['Value'].sum()]
pie_2018

# + id="ZQ53QDNVUE45" colab_type="code" colab={}
expl = [0,0.1,0]
plt.figure(figsize=(40,10))
plt.pie(pie_2018['Value'], explode=expl)
plt.legend(pie_2018['Country'],fontsize='11',loc='best')
# plt.style.use('qqplot')
plt.title('2018 Total Investment',fontdict={'fontsize':'20'},loc='left')
plt.show()
