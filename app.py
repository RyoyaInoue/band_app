import streamlit as st
import pandas as pd
import random
from collections import defaultdict
from io import BytesIO
import string
from datetime import timedelta, datetime

st.set_page_config(page_title="Band Maker", layout="wide")


# ===============================================================
# 初期データの準備
# ===============================================================
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
        {"名前":"綾斗","パート":"Gt","学年":1,"経験レベル":"初級"},
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
        {"名前":"健二","パート":"Gt","学年":2,"経験レベル":"初級"},
        {"名前":"Kazuma","パート":"Gt","学年":2,"経験レベル":"初級"},
        {"名前":"すなお","パート":"Gt","学年":4,"経験レベル":"上級"},
        {"名前":"高原","パート":"Ba","学年":4,"経験レベル":"上級"}
        ]
    st.session_state.members_df = pd.DataFrame(members_list)
    st.session_state.selected = {idx: False for idx in range(len(members_list))}
    st.session_state.bands_result = []
    st.session_state.bands_manual = []

# ===============================================================
# サイドバーでページ選択
# ===============================================================
st.sidebar.title("ページ選択")
page = st.sidebar.radio("ページ", ["バンド作成", "ライブハウス予約・料金計算","ライブスケジュール"])

# ===============================================================
# 並び替え関数
# ===============================================================
def sort_members(df, option):
    df_sorted = df.copy()
    if option == "パート順":
        df_sorted = df_sorted.sort_values(by=["パート", "名前"])
    elif option == "学年順":
        df_sorted = df_sorted.sort_values(by=["学年", "名前"])
    elif option == "経験レベル順":
        level_order = {"初級": 0, "中級": 1, "上級": 2}
        df_sorted["経験値"] = df_sorted["経験レベル"].map(level_order)
        df_sorted = df_sorted.sort_values(by=["経験値", "名前"]).drop(columns=["経験値"])
    return df_sorted

# ===============================================================
# バンド作成関数
# ===============================================================
def create_bands(df, selected):
    selected_members = df[[selected[i] for i in df.index]].copy()
    if selected_members.empty:
        st.warning("参加者が選択されていません")
        return []

    max_per_band = {"Ba": 2, "Dr": 2}
    parts = defaultdict(list)
    for _, row in selected_members.iterrows():
        parts[row["パート"]].append(row)

    # バンド数をパートごとに計算
    band_counts = []
    for part_name, members_list in parts.items():
        if part_name in max_per_band:
            band_counts.append((len(members_list) + max_per_band[part_name] - 1) // max_per_band[part_name])
        else:
            band_counts.append(len(members_list))
    num_bands = min(band_counts) if band_counts else 1
    bands = [defaultdict(list) for _ in range(num_bands)]

    # ===== まず全体で3年生を均等に割り振る =====
    members_3rd = selected_members[selected_members["学年"] == 3].to_dict("records")
    for idx, member in enumerate(members_3rd):
        band_idx = idx % num_bands
        part_name = member["パート"]
        bands[band_idx][part_name].append(member["名前"])

    # ===== 残りメンバーをパートごとに振り分け =====
    for part_name, members_list in parts.items():
        # 3年生はすでに割り振ったので除外
        remaining_members = [m for m in members_list if m["学年"] != 3]

        # 経験順でシャッフル
        if part_name in ["Gt", "Ba", "Dr"]:
            high = [m for m in remaining_members if m["経験レベル"] == "上級"]
            mid = [m for m in remaining_members if m["経験レベル"] == "中級"]
            low = [m for m in remaining_members if m["経験レベル"] == "初級"]
            random.shuffle(high); random.shuffle(mid); random.shuffle(low)
            members_sorted = high + mid + low
        else:
            members_sorted = remaining_members.copy()
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
# バンド作成ページ
# ===============================================================
if page == "バンド作成":
    st.title("🎸 バンド作成アプリ")

    # 並び替えオプション
    sort_option = st.selectbox(
        "並び替え",
        ["一覧", "パート順", "学年順", "経験レベル順"],
        index=2
    )
    df_display = sort_members(st.session_state.members_df, sort_option)

    # チェックボックス表示（3列）
    def display_members(df_group):
        cols = st.columns(3)
        for i, (_, row) in enumerate(df_group.iterrows()):
            col_idx = i % 3
            checkbox_key = f"chk_{row.name}"
            st.session_state.selected[row.name] = cols[col_idx].checkbox(
                f"{row['名前']}（{row['パート']}・{row['学年']}年・{row['経験レベル']}）",
                value=st.session_state.selected[row.name],
                key=checkbox_key
            )

    if sort_option in ["学年順", "パート順", "経験レベル順"]:
        group_key = {"学年順": "学年", "パート順": "パート", "経験レベル順": "経験レベル"}[sort_option]
        group_label = {"学年": "🎓", "パート": "🎶", "経験レベル": "⭐"}[group_key]
        for key_value, group in df_display.groupby(group_key):
            st.markdown(f"#### {group_label} {key_value}")
            display_members(group)
    else:
        display_members(df_display)

    # 選択人数表示
    total_selected = sum(st.session_state.selected.values())
    st.markdown(f"### ✅ 現在の選択人数：{total_selected}人")

    # バンド作成ボタン
    if st.button("🎵 バンド作成"):
        st.session_state.bands_result = create_bands(st.session_state.members_df, st.session_state.selected)

    # バンド結果表示
    if st.session_state.bands_result:
        st.subheader("🎶 バンド分け結果")
        result_df = pd.DataFrame(columns=["Vo", "Gt", "Ba", "Dr", "Key"])
        for i, band in enumerate(st.session_state.bands_result):
            band_label = "Band " + string.ascii_uppercase[i]
            row = {col: ", ".join(band.get(col, ["（空き）"])) for col in ["Vo", "Gt", "Ba", "Dr", "Key"]}
            result_df.loc[band_label] = row
        st.table(result_df)

        if st.button("このバンドをライブスケジュールに追加"):
            for i, band in enumerate(st.session_state.bands_result):
                band_name = "Band " + string.ascii_uppercase[i]
                st.session_state.bands_manual.append({"バンド名": band_name, "メンバー": band})
            st.success("ライブスケジュールページに追加しました！")


# ===============================================================
# ライブハウス予約・料金計算ページ
# ===============================================================
elif page == "ライブハウス予約・料金計算":
    st.title("🎤 ライブハウス予約・料金計算")

    livehouses = ["CLUB GATE"]
    selected_house = st.selectbox("ライブハウスを選択", livehouses)

    day_options = ["月〜木/平日", "金・日・祝", "土・祝前休日"]
    selected_day = st.selectbox("日程を選択", day_options)

    hours = st.number_input("利用時間（時間）", min_value=4, max_value=12, value=8, step=1)

    use_dressing_room = st.checkbox("楽屋使用 (2F別室, 10,000円 税別)")

    # 基本料金設定（4時間・8時間）
    if selected_day == "月〜木/平日":
        price_4h, price_8h = 45000, 80000
    elif selected_day == "金・日・祝":
        price_4h, price_8h = 55000, 100000
    else:  # 土・祝前休日
        price_4h, price_8h = 65000, 120000

    # 時間に応じた料金計算
    if hours <= 4:
        total_price = price_4h
    elif hours <= 8:
        total_price = price_4h + (price_8h - price_4h) * ((hours - 4) / 4)
    else:
        # 8時間を超えた場合：8時間料金 + 30分ごとに6,000円加算
        extra_hours = hours - 8
        half_hours = int(extra_hours * 2)  # 30分単位に変換
        total_price = price_8h + half_hours * 6000

    # 楽屋使用料追加
    if use_dressing_room:
        total_price += 10000

    # 税込計算（10%）
    tax_rate = 0.1
    total_price_incl_tax = int(total_price * (1 + tax_rate))

    st.markdown(f"### 💰 合計料金（税別）: {int(total_price):,}円")
    st.markdown(f"### 💴 合計料金（税込10%）: {total_price_incl_tax:,}円")

# ===============================================================
# ライブスケジュールページ（連続出演調整版）
# ===============================================================
elif page == "ライブスケジュール":
    st.title("ライブスケジュール作成（手動バンド登録）")

    import pandas as pd
    from datetime import datetime, timedelta
    from io import BytesIO

    # --------------------------
    # メンバー情報の取得
    # --------------------------
    if "members_df" in st.session_state:
        df_members = st.session_state.members_df.copy()
    else:
        df_members = pd.DataFrame(columns=["名前", "学年", "経験", "パート"])

    parts = ["Vo", "Gt", "Ba", "Dr", "Key"]

    # --------------------------
    # セッションステート初期化
    # --------------------------
    if "bands_manual" not in st.session_state:
        st.session_state["bands_manual"] = []

    if "band_name_input" not in st.session_state:
        st.session_state["band_name_input"] = ""

    if "selected_members_input" not in st.session_state:
        st.session_state["selected_members_input"] = {part: [] for part in parts}

    if "assigned_parts_input" not in st.session_state:
        st.session_state["assigned_parts_input"] = {part: [part] for part in parts}

    # --------------------------
    # バンド入力リセット関数
    # --------------------------
    def reset_band_inputs():
        st.session_state["band_name_input"] = ""
        st.session_state["selected_members_input"] = {part: [] for part in parts}
        st.session_state["assigned_parts_input"] = {part: [part] for part in parts}
        st.session_state["band_name_input_display"] = ""
        for part in parts:
            st.session_state[f"{part}_assigned_parts"] = [part]
            st.session_state[f"{part}_select"] = []

    # --------------------------
    # バンド追加関数
    # --------------------------
    def add_band():
        band_name = st.session_state["band_name_input"]
        selected_members = st.session_state["selected_members_input"]
        if not band_name:
            st.warning("バンド名を入力してください")
            return
        st.session_state["bands_manual"].append({
            "バンド名": band_name,
            "メンバー": selected_members
        })
        st.success(f"{band_name} を追加しました")
        reset_band_inputs()

    # --------------------------
    # バンド削除関数
    # --------------------------
    def delete_band(idx):
        st.session_state["bands_manual"].pop(idx)

    # ===============================
    # バンド登録UI
    # ===============================
    st.markdown("### バンド登録（複数パートの割り当て可能）")
    with st.container():
        band_name = st.text_input(
            "バンド名",
            value=st.session_state["band_name_input"],
            key="band_name_input_display"
        )
        st.session_state["band_name_input"] = band_name

        selected_members = {}
        cols = st.columns(len(parts))
        for i, part in enumerate(parts):
            with cols[i]:
                st.markdown(f"**{part}枠**")
                assigned_parts = st.multiselect(
                    "追加するパート",
                    options=parts,
                    default=st.session_state["assigned_parts_input"].get(part, [part]),
                    key=f"{part}_assigned_parts"
                )
                st.session_state["assigned_parts_input"][part] = assigned_parts

                members_for_assign = []
                for p in assigned_parts:
                    members_for_assign += df_members[df_members["パート"] == p]["名前"].tolist()
                members_for_assign = list(dict.fromkeys(members_for_assign))

                selected = st.multiselect(
                    "メンバー選択",
                    options=members_for_assign,
                    default=st.session_state["selected_members_input"].get(part, []),
                    key=f"{part}_select"
                )
                selected_members[part] = selected

        st.session_state["selected_members_input"] = selected_members

        st.button("バンドを追加", on_click=add_band)
        st.button("入力をリセット", on_click=reset_band_inputs)

    # ===============================
    # 登録済みバンド表示と削除
    # ===============================
    if st.session_state["bands_manual"]:
        st.subheader("登録済みバンド一覧")
        for idx, b in enumerate(st.session_state["bands_manual"]):
            cols = st.columns([4, 1])
            with cols[0]:
                st.markdown(f"**🎸 {b['バンド名']}**")
                member_str_dict = {part: ", ".join(members) if members else "" for part, members in b["メンバー"].items()}
                band_table = pd.DataFrame.from_dict(member_str_dict, orient="index", columns=["メンバー"])
                st.dataframe(band_table, use_container_width=True, height=len(band_table)*35 + 35)
            with cols[1]:
                st.button("削除", key=f"del_{idx}", on_click=delete_band, args=(idx,))

    # ===============================
    # スケジュール設定UI
    # ===============================
    st.markdown("### スケジュール設定")
    start_time = st.time_input("ライブ開始時刻", value=datetime.strptime("10:00", "%H:%M").time())
    band_play_minutes = st.number_input("1バンド演奏時間（分）", value=20, min_value=1)
    band_change_minutes = st.number_input("バンド転換時間（分）", value=10, min_value=0)
    live_total_hours = st.number_input("ライブ全体の所要時間（時間）", value=8, min_value=1)

    # ===============================
    # スケジュール作成関数（連続出演調整付き）
    # ===============================
    def create_schedule_manual():
        import copy
        schedule = []
        start_dt = datetime.combine(datetime.today(), start_time)

        # 幹部集合・参加者集合
        schedule.append({
            "時間": (start_dt).strftime("%H:%M")+"〜"+(start_dt+timedelta(minutes=30)).strftime("%H:%M"),
            "項目":"幹部その他集合"
        })
        schedule.append({
            "時間": (start_dt+timedelta(minutes=30)).strftime("%H:%M")+"〜"+(start_dt+timedelta(minutes=60)).strftime("%H:%M"),
            "項目":"参加者全員集合"
        })
        current_time = start_dt + timedelta(minutes=60)

        parts = ["Vo", "Gt", "Ba", "Dr", "Key"]

        bands = copy.deepcopy(st.session_state["bands_manual"])
        # バンド名に "Band" が含まれるものを固定
        fixed_bands = [b for b in bands if "Band" in b["バンド名"]]
        remaining_bands = [b for b in bands if "Band" not in b["バンド名"]]

        scheduled_bands = []
        last_two_members = []

        # 固定バンドを追加（順番固定）
        for b in fixed_bands:
            scheduled_bands.append(b)
            members = sum(b["メンバー"].values(), [])
            last_two_members.append(members)
            if len(last_two_members) > 2:
                last_two_members.pop(0)

        # 可変バンドを配置
        while remaining_bands:
            # 2連続優先で並び替え（過去2回に出ているメンバーが多い順）
            remaining_bands.sort(
                key=lambda b: -sum(member in m for member in sum(b["メンバー"].values(), []) for m in last_two_members)
            )

            placed = False
            for i, b in enumerate(remaining_bands):
                all_members = sum(b["メンバー"].values(), [])
                # 3連続メンバーがいないか確認
                conflict = any(
                    sum(member in m for m in last_two_members) >= 2
                    for member in all_members
                )
                # 残りバンドが少なければ強制配置
                if conflict and len(remaining_bands) <= 2:
                    conflict = False

                if not conflict:
                    scheduled_bands.append(b)
                    last_two_members.append(all_members)
                    if len(last_two_members) > 2:
                        last_two_members.pop(0)
                    remaining_bands.pop(i)
                    placed = True
                    break
            if not placed:
                # 強制配置（3連続禁止を無視）
                b = remaining_bands.pop(0)
                scheduled_bands.append(b)
                last_two_members.append(sum(b["メンバー"].values(), []))
                if len(last_two_members) > 2:
                    last_two_members.pop(0)

        # スケジュール表作成（★マーク付き）
        prev_members = set()
        for idx, b in enumerate(scheduled_bands):
            end_band = current_time + timedelta(minutes=band_play_minutes)
            row = {
                "時間": f"{current_time.strftime('%H:%M')}〜{end_band.strftime('%H:%M')}",
                "項目": b["バンド名"]
            }

            for part in parts:
                members_marked = []
                for m in b["メンバー"].get(part, []):
                    if m in prev_members:
                        members_marked.append(f"{m}★")
                    else:
                        members_marked.append(m)
                row[part] = ", ".join(members_marked)

            schedule.append(row)
            prev_members = set(sum([b["メンバー"].get(part, []) for part in parts], []))
            current_time = end_band

            # 転換時間
            if idx < len(scheduled_bands) - 1:
                end_change = current_time + timedelta(minutes=band_change_minutes)
                schedule.append({
                    "時間": f"{current_time.strftime('%H:%M')}〜{end_change.strftime('%H:%M')}",
                    "項目": "転換",
                    "Vo":"", "Gt":"", "Ba":"", "Dr":"", "Key":""
                })
                current_time = end_change

        # 撤収
        end_time_dt = start_dt + timedelta(hours=live_total_hours)
        schedule.append({
            "時間": f"{current_time.strftime('%H:%M')}〜{end_time_dt.strftime('%H:%M')}",
            "項目":"撤収",
            "Vo":"", "Gt":"", "Ba":"", "Dr":"", "Key":""
        })

        return pd.DataFrame(schedule)


    # ===============================
    # スケジュール作成ボタン
    # ===============================
    if st.button("スケジュール作成"):
        if not st.session_state["bands_manual"]:
            st.warning("まずバンドを登録してください")
        else:
            schedule_df = create_schedule_manual()
            st.subheader("ライブスケジュール")
            st.dataframe(schedule_df, use_container_width=True, height=600)

            towrite = BytesIO()
            schedule_df.to_excel(towrite, index=False, sheet_name="Schedule", engine="openpyxl")
            towrite.seek(0)
            st.download_button(
                "Excel ダウンロード",
                data=towrite,
                file_name="live_schedule.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
