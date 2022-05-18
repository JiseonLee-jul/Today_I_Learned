############## dist plot
m = 5, n = 4
plt.subplots(m,n, figsize=(15,15))
for idx, col in enumerate(df_dropna.columns[4:24]):
    ax = plt.subplot(m, n, idx + 1)
    ax.yaxis.set_ticklabels([])
    sns.distplot(df_dropna[df_dropna['성별코드']==2][col], hist=False, axlabel=False,
               kde_kws={'linestyle':'-', 'color':'orange', 'label':'Female'})
    sns.distplot(df_dropna[df_dropna['성별코드']==1][col], hist=False, axlabel=False,
               kde_kws={'linestyle':'-', 'color':'blue', 'label':'Male'})
    ax.set_title(col)
plt.legend(bbox_to_anchor=(1.04, 3), loc="upper left")
plt.tight_layout()
plt.show()


############## count_plot 
m = 2, n = 3
plt.subplots(m, n, figsize=(12,12))
col_names_category = ['청력(좌)', '청력(우)', '요단백', '흡연상태', '음주여부', '구강검진수검여부']
for idx, col in enumerate(df_dropna[col_names_category]):
    ax = plt.subplot(m, n, idx + 1)
    ax.yaxis.set_ticklabels([])
    sns.countplot(col, hue = '성별코드', data = df_dropna, palette = 'Set1')
    plt.legend(labels = ['여자', '남자'], title = '성별')
    # ax.legend()
plt.tight_layout()
plt.show()
