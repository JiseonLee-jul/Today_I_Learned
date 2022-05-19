import matplotlib.ticker as mtick

# na_per_bar_plot : 각 컬럼별 na비율을 bar plot으로 보여주는 그래프
def na_per_bar_plot(data, figsize = (8, 16)):
    fig, ax = plt.subplots(figsize = figsize, facecolor='#fffff6')
    # 축 설정
    for loc in ['bottom', 'left']:
        ax.spines[loc].set_visible(True)
        ax.spines[loc].set_linewidth(2)
        ax.spines[loc].set_color('gray')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # NA percentage
    na_per = []
    for col in data.columns:
        na_per.append(np.around((data[col].isnull().sum() / data.shape[0]) * 100, 3))
    data_na_per = pd.DataFrame({'col_name' : data.columns, 'na_per' : na_per})
        
    ax = sns.barplot(x= 'na_per', y = 'col_name',data = data_na_per,
                     color='coral', lw=1.5, ec='black')
    ax.set_xlabel('Percentage', fontsize=10, weight='bold')
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    
    ax.grid(zorder=0)
    ax.text(0, -0.75, 'NA Percentage for each column', color='black', fontsize=15, ha='left', va='bottom', weight='bold', style='italic')
    ax.set_ylabel('')
    
    plt.show()
