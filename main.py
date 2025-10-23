import tkinter as tk
from tkinter import ttk, messagebox
import random
from collections import defaultdict
import string

# 参加者データ
members = [
    {"名前":"祐太","パート":"Vo","学年":4,"経験レベル":"上級"},
    {"名前":"おうた","パート":"Vo","学年":1,"経験レベル":"初級"},
    {"名前":"大西真福","パート":"Vo","学年":3,"経験レベル":"中級"},
    {"名前":"美咲","パート":"Vo","学年":3,"経験レベル":"中級"},
    {"名前":"中村玲奈","パート":"Vo","学年":4,"経験レベル":"上級"},
    {"名前":"nao","パート":"Vo","学年":1,"経験レベル":"初級"},
    {"名前":"ハナノ","パート":"Vo","学年":1,"経験レベル":"初級"},
    {"名前":"かなた","パート":"Gt","学年":4,"経験レベル":"中級"},
    {"名前":"むこむこ","パート":"Gt","学年":1,"経験レベル":"上級"},
    {"名前":"井上涼也","パート":"Gt","学年":3,"経験レベル":"上級"},
    {"名前":"りな","パート":"Gt","学年":1,"経験レベル":"初級"},
    {"名前":"向垣内光","パート":"Gt","学年":3,"経験レベル":"上級"},
    {"名前":"綾斗","パート":"Gt","学年":2,"経験レベル":"初級"},
    {"名前":"こうた","パート":"Gt","学年":3,"経験レベル":"上級"},
    {"名前":"まゆ","パート":"Gt","学年":1,"経験レベル":"初級"},
    {"名前":"栗林","パート":"Gt","学年":4,"経験レベル":"中級"},
    {"名前":"まなか","パート":"Gt","学年":1,"経験レベル":"初級"},
    {"名前":"ほの","パート":"Ba","学年":4,"経験レベル":"中級"},
    {"名前":"結愛","パート":"Ba","学年":1,"経験レベル":"初級"},
    {"名前":"優里","パート":"Ba","学年":4,"経験レベル":"上級"},
    {"名前":"はると","パート":"Ba","学年":2,"経験レベル":"上級"},
    {"名前":"桑村","パート":"Ba","学年":2,"経験レベル":"上級"},
    {"名前":"mizu","パート":"Ba","学年":1,"経験レベル":"中級"},
    {"名前":"わたべです","パート":"Ba","学年":3,"経験レベル":"中級"},
    {"名前":"りょうすけ","パート":"Ba","学年":2,"経験レベル":"初級"},
    {"名前":"大和","パート":"Ba","学年":3,"経験レベル":"上級"},
    {"名前":"侑知","パート":"Ba","学年":1,"経験レベル":"中級"},
    {"名前":"さかいや","パート":"Dr","学年":4,"経験レベル":"上級"},
    {"名前":"あんどうりょうが","パート":"Dr","学年":3,"経験レベル":"中級"},
    {"名前":"Mizuki","パート":"Dr","学年":1,"経験レベル":"初級"},
    {"名前":"阪本","パート":"Dr","学年":4,"経験レベル":"上級"},
    {"名前":"いたもち","パート":"Dr","学年":1,"経験レベル":"初級"},
    {"名前":"宏太郎","パート":"Dr","学年":4,"経験レベル":"上級"},
    {"名前":"結菜","パート":"Dr","学年":1,"経験レベル":"初級"},
    {"名前":"やっすー","パート":"Dr","学年":2,"経験レベル":"上級"},
    {"名前":"ゆうな","パート":"Dr","学年":1,"経験レベル":"初級"},
    {"名前":"しんのすけ","パート":"Dr","学年":3,"経験レベル":"上級"},
    {"名前":"玲飛","パート":"Dr","学年":2,"経験レベル":"中級"},
    {"名前":"きしあやと","パート":"Key","学年":3,"経験レベル":"上級"},
    {"名前":"Chisaki","パート":"Key","学年":1,"経験レベル":"初級"},
    {"名前":"Perry","パート":"Key","学年":2,"経験レベル":"中級"},
    {"名前":"ひょり","パート":"Key","学年":1,"経験レベル":"初級"},
    {"名前":"まつもとこうき","パート":"Key","学年":4,"経験レベル":"上級"}
]

parts = defaultdict(list)
for m in members:
    parts[m["パート"]].append(m)

root = tk.Tk()
root.title("バンド作成")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

check_vars = defaultdict(list)

# ラベルフレームに全体とパートごとの人数を表示
count_frame = tk.Frame(root)
count_frame.pack(pady=5)
overall_label = tk.Label(count_frame, text="選択中の参加者数: 0")
overall_label.pack()
part_labels = {}
for part in parts.keys():
    lbl = tk.Label(count_frame, text=f"{part}: 0")
    lbl.pack(anchor="w")
    part_labels[part] = lbl

def update_count(*args):
    total_count = 0
    part_counts = defaultdict(int)
    for part, vars_list in check_vars.items():
        for m, var in vars_list:
            if var.get():
                total_count += 1
                part_counts[part] += 1
    overall_label.config(text=f"選択中の参加者数: {total_count}")
    for part, lbl in part_labels.items():
        lbl.config(text=f"{part}: {part_counts.get(part,0)}")

for part, plist in parts.items():
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=part)
    for m in plist:
        var = tk.BooleanVar(value=True)
        var.trace_add("write", update_count)  # リアルタイム更新
        cb = tk.Checkbutton(frame, text=f"{m['名前']} (学年:{m['学年']}, {m['経験レベル']})", variable=var)
        cb.pack(anchor="w")
        check_vars[part].append((m, var))

def create_bands():
    selected = defaultdict(list)
    for part, vars_list in check_vars.items():
        for m, var in vars_list:
            if var.get():
                selected[part].append(m)

    if not selected:
        messagebox.showwarning("注意", "参加者が選択されていません")
        return

    max_per_band = {"Ba":2, "Dr":2}
    band_counts = []
    for part, members_list in selected.items():
        if part in max_per_band:
            band_counts.append((len(members_list)+max_per_band[part]-1)//max_per_band[part])
        else:
            band_counts.append(len(members_list))
    num_bands = min(band_counts)
    bands = [defaultdict(list) for _ in range(num_bands)]
    reasons_list = [defaultdict(list) for _ in range(num_bands)]

    for part, members_list in selected.items():
        if part in ["Gt","Ba","Dr"]:
            high = [m for m in members_list if m["経験レベル"]=="上級"]
            mid = [m for m in members_list if m["経験レベル"]=="中級"]
            low = [m for m in members_list if m["経験レベル"]=="初級"]
            random.shuffle(high); random.shuffle(mid); random.shuffle(low)
            members_sorted = high + mid + low
        else:
            members_sorted = members_list.copy()
            random.shuffle(members_sorted)

        band_idx = 0
        for member in members_sorted:
            attempts = 0
            while attempts < num_bands:
                if part in max_per_band and len(bands[band_idx][part]) >= max_per_band[part]:
                    band_idx = (band_idx + 1) % num_bands
                    attempts += 1
                else:
                    bands[band_idx][part].append(member["名前"])
                    reasons_list[band_idx][part].append(f"学年:{member['学年']},経験:{member['経験レベル']}")
                    band_idx = (band_idx + 1) % num_bands
                    break
            else:
                bands[0][part].append(member["名前"])
                reasons_list[0][part].append(f"学年:{member['学年']},経験:{member['経験レベル']}")

    output = tk.Toplevel(root)
    output.title("バンド結果")

    tree = ttk.Treeview(output, columns=["Vo","Gt","Ba","Dr","Key"], show="tree headings", height=num_bands)
    tree.heading("#0", text="Band")
    tree.column("#0", width=80, anchor="center")
    for col in ["Vo","Gt","Ba","Dr","Key"]:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    tree.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(output, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    for i, (band, reasons) in enumerate(zip(bands, reasons_list)):
        band_label = "Band " + string.ascii_uppercase[i]
        row = []
        for part_name in ["Vo","Gt","Ba","Dr","Key"]:
            names = ', '.join(band.get(part_name, ["（空き）"]))
            row.append(names)
        tree.insert("", "end", text=band_label, values=row)

btn = tk.Button(root, text="バンド作成", command=create_bands)
btn.pack(pady=10)

update_count()  # 初期値表示
root.mainloop()
