import streamlit as st
import pandas as pd
import random
from collections import defaultdict
import string
from io import BytesIO

# --- 初期データ ---
if "members_df" not in st.session_state:
    members_list = [
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
        {"名前":"栗林","パート":"Gt","学年":4,"経験レベル":"上級"},
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
        {"名前":"まつもとこうき","パート":"Key","学年":4,"経験レベル":"上級"},
        {"名前":"あいみ","パート":"Ba","学年":4,"経験レベル":"中級"},
        {"名前":"瑛音","パート":"Dr","学年":3,"経験レベル":"中級"},
        {"名前":"あつし","パート":"Gt","学年":4,"経験レベル":"中級"},
        {"名前":"あやか","パート":"Gt","学年":3,"経験レベル":"中級"},
        {"名前":"歌野天海","パート":"Key","学年":4,"経験レベル":"上級"},
        {"名前":"おーい","パート":"Gt","学年":2,"経験レベル":"初級"},
        {"名前":"おくけいと","パート":"Gt","学年":4,"経験レベル":"上級"},
        {"名前":"がい","パート":"Vo","学年":2,"経験レベル":"中級"},
        {"名前":"かほ","パート":"Dr","学年":2,"経験レベル":"中級"},
        {"名前":"こすがはな","パート":"Gt","学年":4,"経験レベル":"中級"},
        {"名前":"佐藤裕馬","パート":"Gt","学年":4,"経験レベル":"上級"},
        {"名前":"たかつぐ","パート":"Dr","学年":2,"経験レベル":"初級"},
        {"名前":"辻本直哉","パート":"Dr","学年":4,"経験レベル":"上級"},
        {"名前":"夏綸","パート":"Key","学年":4,"経験レベル":"上級"},
        {"名前":"西田佳祐","パート":"Gt","学年":4,"経験レベル":"上級"},
        {"名前":"林莉子","パート":"Key","学年":3,"経験レベル":"上級"},
        {"名前":"はるや","パート":"Gt","学年":3,"経験レベル":"上級"},
        {"名前":"柊（しゅう）","パート":"Dr","学年":3,"経験レベル":"上級"},
        {"名前":"みかこ","パート":"Vo","学年":2,"経験レベル":"上級"},
        {"名前":"美咲2","パート":"Ba","学年":2,"経験レベル":"中級"},
        {"名前":"りーま","パート":"Ba","学年":4,"経験レベル":"上級"},
        {"名前":"りゅうへい","パート":"Gt","学年":2,"経験レベル":"初級"},
        {"名前":"濱田りょう","パート":"Ba","学年":3,"経験レベル":"中級"},
        {"名前":"るな","パート":"Key","学年":4,"経験レベル":"上級"},
        {"名前":"kei","パート":"Vo","学年":4,"経験レベル":"上級"},
        {"名前":"yuzuki","パート":"Key","学年":1,"経験レベル":"初級"},
        {"名前":"高原","パート":"Ba","学年":4,"経験レベル":"上級"}
    ]
    st.session_state.members_df = pd.DataFrame(members_list)

# --- 初期チェック状態 ---
if "selected" not in st.session_state:
    st.session_state.selected = {idx: False for idx in st.session_state.members_df.index}

st.title("🎸 バンド作成アプリ")

# ===============================================================
# バンド作成関数
# ===============================================================
def create_bands(df, selected):
    selected_members = df[[selected[i] for i in df.index]].copy()
    if selected_members.empty:
        st.warning("参加者が選択されていません")
        return None

    max_per_band = {"Ba": 2, "Dr": 2}
    parts = defaultdict(list)
    for _, row in selected_members.iterrows():
        parts[row["パート"]].append(row)

    band_counts = []
    for part_name, members_list in parts.items():
        if part_name in max_per_band:
            band_counts.append((len(members_list) + max_per_band[part_name] - 1) // max_per_band[part_name])
        else:
            band_counts.append(len(members_list))
    num_bands = min(band_counts)
    bands = [defaultdict(list) for _ in range(num_bands)]

    for part_name, members_list in parts.items():
        if part_name in ["Gt", "Ba", "Dr"]:
            high = [m for m in members_list if m["経験レベル"] == "上級"]
            mid = [m for m in members_list if m["経験レベル"] == "中級"]
            low = [m for m in members_list if m["経験レベル"] == "初級"]
            random.shuffle(high); random.shuffle(mid); random.shuffle(low)
            members_sorted = high + mid + low
        else:
            members_sorted = members_list.copy()
            random.shuffle(members_sorted)

        band_idx = 0
        for member in members_sorted:
            attempts = 0
            while attempts < num_bands:
                if part_name in max_per_band and len(bands[band_idx][part_name]) >= max_per_band[part_name]:
                    band_idx = (band_idx + 1) % num_bands
                    attempts += 1
                else:
                    bands[band_idx][part_name].append(member["名前"])
                    band_idx = (band_idx + 1) % num_bands
                    break
            else:
                bands[0][part_name].append(member["名前"])
    return bands

# ===============================================================
# バンド作成処理（上部）
# ===============================================================
if "create_band_trigger" in st.session_state and st.session_state.create_band_trigger:
    bands = create_bands(st.session_state.members_df, st.session_state.selected)
    if bands:
        st.session_state.bands_result = bands
    st.session_state.create_band_trigger = False

# ===============================================================
# 結果表示（上部固定）
# ===============================================================
if "bands_result" in st.session_state and st.session_state.bands_result:
    st.subheader("🎶 バンド分け結果")
    result_df = pd.DataFrame(columns=["Vo", "Gt", "Ba", "Dr", "Key"])
    for i, band in enumerate(st.session_state.bands_result):
        band_label = "Band " + string.ascii_uppercase[i]
        row = {col: ", ".join(band.get(col, ["（空き）"])) for col in ["Vo", "Gt", "Ba", "Dr", "Key"]}
        result_df.loc[band_label] = row
    st.table(result_df)

    towrite = BytesIO()
    result_df.to_excel(towrite, index=True, sheet_name="Bands", engine="openpyxl")
    towrite.seek(0)
    st.download_button(
        "Excel ダウンロード",
        data=towrite,
        file_name="bands.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="download_btn"
    )

# ===============================================================
# 並び替えと参加者リスト
# ===============================================================
st.divider()
st.subheader("🎤 参加者リスト")

# 🔹 初期値を「学年順」に変更
sort_option = st.selectbox(
    "並び替え",
    ["一覧", "パート順", "学年順", "経験レベル順"],
    index=2  # ← 「学年順」を初期選択
)

df_display = st.session_state.members_df.copy()
if sort_option == "パート順":
    df_display = df_display.sort_values(by=["パート", "名前"])
elif sort_option == "学年順":
    df_display = df_display.sort_values(by=["学年", "名前"])
elif sort_option == "経験レベル順":
    level_order = {"初級": 0, "中級": 1, "上級": 2}
    df_display["経験値"] = df_display["経験レベル"].map(level_order)
    df_display = df_display.sort_values(by=["経験値", "名前"]).drop(columns=["経験値"])


# バンド作成ボタン
if st.button("🎵 バンド作成", key="create_band_btn"):
    st.session_state.create_band_trigger = True

# 🔹 学年ごとに見出しを表示（見やすく）
if sort_option in ["学年順", "パート順", "経験レベル順"]:
    if sort_option == "学年順":
        group_key = "学年"
        group_label = lambda x: f"🎓 {x}年"
    elif sort_option == "パート順":
        group_key = "パート"
        group_label = lambda x: f"🎶 {x}"
    else:  # 経験レベル順
        group_key = "経験レベル"
        group_label = lambda x: f"⭐ {x}"

    for key_value, group in df_display.groupby(group_key):
        st.markdown(f"#### {group_label(key_value)}")
        cols = st.columns(3)
        for i, (_, row) in enumerate(group.iterrows()):
            col_idx = i % 3
            checkbox_key = f"chk_{row.name}"
            st.session_state.selected[row.name] = cols[col_idx].checkbox(
                f"{row['名前']}（{row['パート']}・{row['学年']}年・{row['経験レベル']}）",
                value=st.session_state.selected[row.name],
                key=checkbox_key
            )
else:
    # 一覧表示（グループなし）
    cols = st.columns(3)
    for i, (_, row) in enumerate(df_display.iterrows()):
        col_idx = i % 3
        checkbox_key = f"chk_{row.name}"
        st.session_state.selected[row.name] = cols[col_idx].checkbox(
            f"{row['名前']}（{row['パート']}・{row['学年']}年・{row['経験レベル']}）",
            value=st.session_state.selected[row.name],
            key=checkbox_key
        )


# 🔹 参加者リストの上に選択人数を表示
total_selected = sum(st.session_state.selected.values())
st.markdown(f"### ✅ 現在の選択人数：{total_selected}人")
