import matplotlib.pyplot as plt
import numpy as np


colors = {'fluency': 'RdYlGn',
         'ranking1': 'Greens',
         'ranking2': 'YlOrRd'}


def display(func, fname: str, **kwargs):
    func(**kwargs)
    plt.savefig(fname, dpi=300)
    plt.show()


def radar_plot(labels: list, data: dict):
    num_labels = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_labels, endpoint=False).tolist()

    # 원형 배치를 위해 1번째 값 추가:
    for v in data.values():
        v.append(v[0])
    angles += angles[:1]
    labels += labels[:1]
    assert len(angles) == len(labels) == len(data.values)
    
    # display:
    fig, ax = plt.subplots(figsize=(9, 6), subplot_kw=dict(polar=True))

    for value, legend in data.items():
        ax.plot(angles, value, linewidth=1, label=legend)
        ax.fill(angles, value, alpha=.3)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles), labels)

    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
    return fig, ax
    
    
def bar_horizontal_plot(labels: list, data: dict, color='RdYlGn'):
    categories = list(data.keys()) # judge a, b, c, ...
    data = np.array(list(data.values()))
    data_cum = data.cumsum(axis=1)
    cat_colors = plt.colormaps[color](
        np.linspace(0.15, 0.85, data.shape[1]))
    
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.set_xlim(0, np.sum(data, axis=1).max())
    
    for i, (colname, color) in enumerate(zip(labels, cat_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(categories, widths, left=starts, height=0.5,
                       label=colname, color=color)
        r, g, b, _ = color
        text_color = 'black' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncols=len(labels), bbox_to_anchor=(0, 1),
             loc="lower left", fontsize='large')
    return fig, ax


def bar_plot(df, color=("grey", "yellow"), hatch=("/", "+")):
    ax = df.plot.bar(color=color, legend=False, 
                     edgecolor='grey', rot=0, fontsize=15)
    for container, hatch in zip(ax.containers, hatch):
        for patch in container.patches:
            patch.set_hatch(hatch)
            
    ax.legend(loc='upper right', fontsize=12)
    return ax