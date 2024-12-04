# import re  # 正規表現ライブラリをインポート

# def validate_and_correct_tnm_output(tnm_stage):
#     """
#     TNM分類の形式を検証し、不正な形式の場合は修正する。
#     """
#     # 正規表現でTNM分類をチェック
#     tnm_pattern = (
#         r"T(?:0|is|1mi|1[abc]?|2[ab]?|3|4) "  # Tの分類
#         r"N(?:0|1|2|3) "                     # Nの分類
#         r"M(?:0|1[abc]?)"                    # Mの分類
#     )
#     if re.fullmatch(tnm_pattern, tnm_stage):
#         # 正しい形式の場合、そのまま返す
#         return tnm_stage
#     else:
#         # 不正な形式の場合、デフォルト値を返す
#         print(f"警告: 出力形式が不正です。修正します: {tnm_stage}")
#         return "T0 N0 M0"

import re
import bitsandbytes as bnb

def validate_and_correct_tnm_output(tnm_stage):
    """
    TNM分類の形式を検証し、不正な形式の場合は修正する。
    TNM以外の文字を除去し、必要な半角スペースを追加する。
    """
    tnm_stage = tnm_stage.split('end')[0]   # end_ 以降の文字を削除
    # TNM以外の文字（漢字、ひらがな、改行、全角スペースなど）を除去
    tnm_stage = re.sub(r"[^\w]", "", tnm_stage)  # 非単語（アルファベット、数字、アンダースコア以外）を削除
    tnm_stage = re.sub(r"[ぁ-んァ-ン一-龥]", "", tnm_stage)  # 日本語文字を削除

    # 必要なスペースを追加
    tnm_stage = re.sub(r"(T(?:0|is|1mi|1[abc]?|2[ab]?|3|4))", r"\1 ", tnm_stage)
    tnm_stage = re.sub(r"(N(?:0|1|2|3))", r"\1 ", tnm_stage)
    tnm_stage = re.sub(r"(M(?:0|1[abc]?))$", r"\1", tnm_stage)  # 最後の部分

    # 多重スペースや前後スペースを整理
    tnm_stage = re.sub(r"\s+", " ", tnm_stage).strip()

    # 正規表現でTNM分類をチェック
    tnm_pattern = (
        r"T(?:0|is|1mi|1[abc]?|2[ab]?|3|4) "  # Tの分類
        r"N(?:0|1|2|3) "                     # Nの分類
        r"M(?:0|1[abc]?)"                    # Mの分類
    )
    if re.fullmatch(tnm_pattern, tnm_stage):
        # 正しい形式の場合、そのまま返す
        return tnm_stage
    else:
        # 不正な形式の場合、デフォルト値を返す
        print(f"警告: 出力形式が不正です。修正します: {tnm_stage}")
        return "T0 N0 M0"


# モデルから4ビット量子化された線形層の名前を取得する関数
def find_all_linear_names(model):
    target_class = bnb.nn.Linear4bit
    linear_layer_names = set()
    for name_list, module in model.named_modules():
        if isinstance(module, target_class):
            names = name_list.split('.')
            layer_name = names[-1] if len(names) > 1 else names[0]
            linear_layer_names.add(layer_name)
    if 'lm_head' in linear_layer_names:
        linear_layer_names.remove('lm_head')
    return list(linear_layer_names)