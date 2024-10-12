import mip
import pandas as pd

# データの読み込み
students_df = pd.read_csv("resource/students.csv")
cars_df = pd.read_csv("resource/cars.csv")

# 学生の乗車グループ分け問題（0-1整数計画問題）のインスタンス作成
prob = mip.Model("ClubCarProblem", sense=mip.MINIMIZE)

# リスト
# 学生のリスト
S = students_df["student_id"].to_list()
# 車のリスト
C = cars_df["car_id"].to_list()
# 学年のリスト
G = [1, 2, 3, 4]
# 学生と車のペアのリスト
SC = [(s, c) for s in S for c in C]
# 免許を持っている学生のリスト
S_license = students_df[students_df["license"] == 1]["student_id"]
# 学年が  g  の学生のリスト
S_g = {g: students_df[students_df["grade"] == g]["student_id"] for g in G}
# 男性と女性のリスト
S_male = students_df[students_df["gender"] == 0]["student_id"]
S_female = students_df[students_df["gender"] == 1]["student_id"]

# 定数
# 車の乗車定員
U = cars_df["capacity"].to_list()

# 変数
# 学生をどの車に割り当てるかを変数として定義
x = {(s, c): prob.add_var(name=f"x_{s}_{c}", var_type=mip.BINARY) for s, c in SC}

# 制約
# (1) 各学生を１つの車に割り当てる
for s in S:
    prob.add_constr(mip.xsum([x[s, c] for c in C]) == 1)

# (2) 法規制に関する制約：各車には乗車定員より多く乗ることができない
for c in C:
    prob.add_constr(mip.xsum([x[s, c] for s in S]) <= U[c])

# (3) 法規制に関する制約：各車にドライバーを1人以上割り当てる
for c in C:
    prob.add_constr(mip.xsum([x[s, c] for s in S_license]) >= 1)

# (4) 懇親を目的とした制約: 各車に各学年の学生を１人以上割り当てる
for c in C:
    for g in G:
        prob.add_constr(mip.xsum([x[s, c] for s in S_g[g]]) >= 1)

# (5) 各車に男性を1人以上割り当てる
for c in C:
    prob.add_constr(mip.xsum([x[s, c] for s in S_male]) >= 1)

# (6) 各車に女性を1人以上割り当てる
for c in C:
    prob.add_constr(mip.xsum([x[s, c] for s in S_female]) >= 1)

# 求解
status = prob.optimize()
print("Status:", status)

# 最適化結果を表示
# 各車に割り当てられている学生のリストを辞書に格納（車 ID→割り当てられた学生のリスト）
car2students = {c: [s for s in S if x[s, c].x == 1] for c in C}

# 各車の乗車定員（車 ID→乗車定員）
max_people = dict(zip(cars_df["car_id"], cars_df["capacity"]))
for c, ss in car2students.items():
    print(f"車ID: {c}")
    print(f"学生数（乗車定員）: {len(ss)}({max_people[c]})")
    print(f"学生ID: {ss}\n")
