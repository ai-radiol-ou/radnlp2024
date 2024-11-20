
# プログラムの説明書 (README)

RadNLP2024のタスクの方針です。

## 目次

- [概要](#概要)
- [前提条件](#前提条件)
- [セットアップとインストール](#セットアップとインストール)
- [コードの構成](#コードの構成)
- [使用方法](#使用方法)
- [コードの詳細な説明](#コードの詳細な説明)
- [注意事項](#注意事項)
- [ライセンス](#ライセンス)

## 概要

このプログラムは、以下のことを行います。

- 与えられた放射線読影所見文から、肺がんのTNM分類を予測します。
- OpenAIのLLMを使用して、テキストデータを解析します。
- 解析結果をCSVファイルに保存します。

## 前提条件

- Python 3.7以上
- OpenAI APIキー（環境変数として設定するか、コード内で指定）
- 必要なPythonライブラリのインストール
  - `langchain`
  - `openai`
  - `pandas`

## セットアップとインストール

1. **Python環境のセットアップ**

   Python 3.7以上がインストールされていることを確認してください。

2. **必要なライブラリのインストール**

   以下のコマンドを実行して、必要なPythonライブラリをインストールします。

   ```bash
   pip install langchain pandas openai




3. **OpenAI APIキーの設定**


     コード内で以下のように設定します。ただし、セキュリティ上の理由から、コード内にAPIキーをハードコーディングすることは推奨されません：

     ```python
     os.environ["OPENAI_API_KEY"] = 'your-api-key-here'
     ```

## コードの構成

- **モデルの指定**

  使用する言語モデルをリストで指定します。

  ```python
  model_names = ['gpt-4', 'gpt-3.5-turbo', 'other-model-name']
  ```

- **プロンプトの読み込み**

  TNM分類の詳細が記載されたテキストファイル `tnm_prompt.txt` を読み込みます。

- **プロンプトテンプレートの定義**

  医師としての役割を指定し、与えられた文章からTNM分類を選択するプロンプトを定義します。

- **LLMチェーンの作成**

  `langchain` を使用して、言語モデルとプロンプトテンプレートを組み合わせたチェーンを作成します。

- **テキストデータの読み込み**

  TNM分類を予測するためのテキストファイルを指定のフォルダから読み込みます。

- **TNM分類の予測と結果の保存**

  各テキストファイルに対して、TNM分類を予測し、結果をCSVファイルに保存します。

- **出力形式の検証と修正**

  モデルの出力が期待する形式であるかを正規表現で検証し、不正な形式の場合はデフォルト値に修正します。

## 使用方法

1. **コードの取得**

   このリポジトリからコードをクローンまたはダウンロードします。

2. **設定の確認**

   - OpenAI APIキーが正しく設定されていることを確認します。
   - テキストデータのフォルダパス `txt_folder` を適切に設定します。
   - 使用する言語モデルのリスト `model_names` を必要に応じて変更します。

3. **プロンプトテキストの準備**

   `tnm_prompt.txt` ファイルに、TNM分類の詳細情報を記載しておきます。

4. **プログラムの実行**

   ターミナルから以下のコマンドを実行します：

   ```bash
   python your_script_name.py
   ```

5. **結果の確認**

   プログラムが正常に実行されると、指定したCSVファイルに結果が保存されます。
