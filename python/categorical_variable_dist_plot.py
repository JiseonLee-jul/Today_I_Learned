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
plt.tight_layout()
plt.show()
