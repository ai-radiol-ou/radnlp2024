
# OURad@RadNLP2024 shared task in NTCIR-18

RadNLP2024のOURadチームの取り組みです。

### prepare_jsondataset.py
与えられたデータセットからhuggingface用のデータセットに整形してjsonとして保存するコード。finetune_jsonsというフォルダの中にtrain,valそれぞれデータセットが作成される。

 ```bash
python prepare_jsondataset.py
 ```

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
- OpenAIのGPT-o1を使用して、テキストデータを解析します。
- BertモデルやOpen-source LLMと性能の比較を行います。
- 解析結果をCSVファイルに保存します。

## 前提条件

- Python 3.7以上
- OpenAI APIキー（環境変数として設定するか、コード内で指定）

## セットアップとインストール
  - **仮想環境の作成**

      `llm_finetune_env.yml` ファイルを使用して、conda仮想環境を構成します。

      1. **仮想環境の作成とアクティベート**

         以下のコマンドを実行して、仮想環境を作成し、アクティベートします：
        ```bash
        conda create --name llm_finetune_env python=3.7
        conda activate llm_finetune_env
        ```

      2. **必要なライブラリのインストール**

         仮想環境内で、必要なPythonライブラリをインストールします：

         ```bash
         pip install langchain openai unsloth
         ```


3. **OpenAI APIキーの設定**


     コード内で以下のように設定します。ただし、セキュリティ上の理由から、コード内にAPIキーをハードコーディングすることは推奨されません：

     ```python
     os.environ["OPENAI_API_KEY"] = 'your-api-key-here'
     ```

## コードの構成

- **モデルの指定**

  使用する言語モデルをリストで指定します。

  ```python
  model_names = ['gpt-4o', 'gpt-o1-preview']
  ```
  Open-source LLMは以下を使用しました。  
  [google/gemma-2-2b-jpn-it](https://huggingface.co/google/gemma-2-2b-jpn-it)  
  [tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1)  
  [tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.1)


- **プロンプトの読み込み**

  TNM分類の詳細が記載されたテキストファイル `tnm_prompt.txt` を読み込みます。
  Sub taskではそれぞれのクラス分類が記述されたファイル`subask_prompt.txt`を読み込みます。

- **GPTモデルのfew-shot prompting(code/*_few_shot.ipynb)**

  `langchain` を使用して、言語モデルとプロンプトテンプレートを組み合わせたチェーンを作成します。

- **Open-source LLMの作成 (code/*_task_llm_finetune.ipynb)**

  `unsloth` ライブラリを使用して、既存のモデルをQloraによりfinetuningを行います。

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
   `subtask_prompt.txt` ファイルに、subtaskの分類基準を記載しておきます。

4. **プログラムの実行**

   それぞれのipynbファイルを実行してください。

5. **結果の確認**

   プログラムが正常に実行されると、指定したCSVファイルに結果が保存されます。
