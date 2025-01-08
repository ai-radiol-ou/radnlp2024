import os
import pandas as pd
import json


# ファイルパスの設定

for dataset in ['train','val']:
    txt_folder_path = f"../radnlp_2024_train_val_20240731/ja/main_task/{dataset}/"  # TXTファイルが保存されているフォルダ
    csv_file_path = f"../radnlp_2024_train_val_20240731/ja/main_task/{dataset}/label.csv"  # ラベルファイル

    # ラベルCSVファイルを読み込む
    label_data = pd.read_csv(csv_file_path)

    # ファインチューニング用データを格納するリスト
    finetune_data = []

    # フォルダ内のTXTファイルを処理
    for txt_file in os.listdir(txt_folder_path):
        if txt_file.endswith(".txt"):
            file_id = txt_file.split(".")[0]  # ファイル名からIDを取得
            file_path = os.path.join(txt_folder_path, txt_file)

            # 対応するラベルを検索
            matching_label = label_data[label_data["id"] == int(file_id)]
            if not matching_label.empty:
                # テキストを読み込む
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read().strip()

                # ラベルを取得
                t = matching_label["t"].values[0]
                n = matching_label["n"].values[0]
                m = matching_label["m"].values[0]

                # ファインチューニング用データを追加
                finetune_data.append({
                    "prompt": content,
                    "completion": f"{t} {n} {m}",
                    "id": file_id,
                })

    # ファインチューニング用データをJSONL形式で保存
    output_file = f"../finetune_jsons/finetune_dataset_{dataset}.jsonl"
    with open(output_file, 'w', encoding='utf-8') as jsonl_file:
        for entry in finetune_data:
            json.dump(entry, jsonl_file, ensure_ascii=False)
            jsonl_file.write('\n')

    print(f"ファインチューニング用データが {output_file} に保存されました！")