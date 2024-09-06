import seaborn as sns

from sklearn.metrics import cohen_kappa_score
from itertools import combinations

# heatmap
def draw_heatmap(df):
    sns.heatmap(df, annot=True, fmt='.3f', cmap="crest")
    #plt.savefig(dpi=300, fname='pe_corr.png', format='png')
    plt.show()

# IAA
def get_iaa(df):
    """스코어가 주어졌을 때 평가자간 IAA 구한다"""
    def get_iaa(df):
    tmp = dict()
    combi = combinations(df.columns.tolist(), 2)
    for cb in combi:
        score = cohen_kappa_score(df[cb[0]], df[cb[1]])
        tmp[f'{cb[0]}-{cb[1]}'] = score
    return tmp

def collect_score(flist: list, col: str):
    # .csv만 취급
    flist = [f for f in flist if f.endswith('.csv')]
    
    tmp = pd.DataFrame()
    for fname in flist:
        df = pd.read_csv(os.path.join(indir, fname))
        tmp[fname[0]] = df[col]
    return tmp
