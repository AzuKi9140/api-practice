"""最適化問題を解き、最適化結果を返す API"""

import pandas as pd
from flask import Blueprint, make_response, request

from flaskr.modules.car_group_problem import CarGroupProblem

api_bp = Blueprint("api", __name__, url_prefix="/api")


def preprocess(request):
    """リクエストデータを受け取り、データフレームに変換する関数"""
    # 各ファイルを取得する
    students = request.files["students"]
    cars = request.files["cars"]
    # pandas で読み込む
    students_df = pd.read_csv(students)
    cars_df = pd.read_csv(cars)
    return students_df, cars_df


def postprocess(solution_df):
    """データフレームを csv に変換する関数"""
    solution_csv = solution_df.to_csv(index=False)
    response = make_response()
    response.data = solution_csv
    response.headers["Content-Type"] = "text/csv"
    return response


@api_bp.route("/", methods=["POST"])
def solve():
    """最適化問題を解く API 用の関数"""
    # 1. リクエスト受信
    students_df, cars_df = preprocess(request)
    # 2. 最適化実行
    solution_df = CarGroupProblem(students_df, cars_df).solve()
    # 3. レスポンス返送
    response = postprocess(solution_df)
    return response
