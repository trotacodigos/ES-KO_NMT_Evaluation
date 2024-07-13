import matplotlib.pyplot as plt
import numpy as np

def radar_plot(labels: list, data: dict, fname: str):
    num_labels = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_labels, endpoint=False).tolist()

    # 원형 배치를 위해 1번째 값 추가:
    for v in data.values():
        v.append(v[0])
    angles += angles[:1]
    labels += labels[:1]
    
    # display:
    fig, ax = plt.subplots(figsize=(9, 6), subplot_kw=dict(polar=True))

    for value, legend in data.items():
        ax.plot(angles, value, linewidth=1, label=legend)
        ax.fill(angles, value, alpha=.3)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles), labels)

    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
    #plt.title('GNMT - Fluency (%)', position=(0.1, 1))
    plt.savefig(f'{fname}.png', dpi=300)
    print("saved")
    plt.show()