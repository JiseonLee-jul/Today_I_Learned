import matplotlib.ticker as mtick

# na_per_bar_plot_categorical_var : 각 범주형 변수의 카테고리별 na비율을 bar plot으로 보여주는 그래프
# hue : categorical or object 변수가 들어가는 것이 좋음
def na_per_bar_plot_categorical_var(data, col, hue, figsize = (8, 16)):
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
    data[hue] = data[hue].astype('category')
    for x in data[hue].unique():
        subdata = data[data[hue] == x]
        na_per.append(np.around((subdata[col].isnull().sum() / subdata.shape[0]) * 100, 3))
    var_na_per = pd.DataFrame({'col_name' : data[hue].unique(), 'na_per' : na_per})
        
    ax = sns.barplot(x= 'na_per', y = 'col_name',data = var_na_per,
                     color='coral', lw=1.5, ec='black')
    ax.set_xlabel('Percentage', fontsize=10, weight='bold')
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    
    ax.grid(zorder=0)
    ax.text(0, -0.75, f'NA Percentage for each category in {col} variable', color='black', fontsize=15, ha='left', va='bottom', weight='bold', style='italic')
    ax.set_ylabel('')
    
    plt.show()
