## Installation

venvで仮想環境の作成
$ python3.11 -m venv env_radnlp
$ py -3.11 -m venv env_radnlp # Windows

$ . env_radnlp/bin/activate
$ .\env_radnlp\Scripts\Activate.ps1 # Windows

$ pip install jupyter scipy numpy pandas matplotlib seaborn scikit-learn cython tqdm

$ conda install cudatoolkit

$ pip install tensorflow
# Mac
# $ pip install tensorflow-macos tensorflow-metal
$ pip install tf-keras==2.16 #tensorflowのバージョンに合わせる

#bashで行う。zshだとエラー。
$ pip install transformers[ja] # UTH-BERTで必要
$ pip install transformers[torch] # Debartaで必要

$ pip install torch torchvision torchaudio

$ pip install jaconv neologdn mecab-python3 unidic-lite unidic sentencepiece tiktoken
$ python -m unidic download


condaで仮想環境の作成
$ conda create -n radnlp python==3.11
$ conda activate radnlp

$ conda install jupyter scipy numpy pandas matplotlib seaborn scikit-learn cython
$ conda install conda-forge::tqdm

$ conda install cudatoolkit

$ conda install tensorflow
# Mac
# $ pip install tensorflow-macos tensorflow-metal
$ conda install tf-keras==2.16 #tensorflowのバージョンに合わせる

#bashで行う。zshだとエラー。
$ pip install transformers[ja] # UTH-BERTで必要
$ pip install transformers[torch] # Debartaで必要

$ conda install pytorch::pytorch torchvision torchaudio -c pytorch

$ pip install jaconv neologdn mecab-python3 unidic-lite unidic sentencepiece tiktoken
$ python -m unidic download





## UTH-BERTの事前準備

https://github.com/jinseikenai/uth-bert

＜Install mecab-ipadic-neologd (general dictionary for Mecab) ＞

$ git clone https://github.com/neologd/mecab-ipadic-neologd.git 
$ cd mecab-ipadic-neologd 
$ sudo bin/install-mecab-ipadic-neologd -n -a
→プロジェクトのdic/mecab-ipadic-neologdに事前にコピーずみ

辞書をupdateする際は
$ cd ./dic/mecab-ipadic-neologd-system/mecab-ipadic-neologd
$ .bin/install-mecab-ipadic-neologd -n -a

# install/updateされるパスは以下で確認できる
$ mecab-config --dicdir
→/usr/local/lib/mecab/dic/mecab-ipadic-neologd # Mac

# install/updateされた辞書をプロジェクトのdicフォルダにコピー
$cp -a /usr/local/lib/mecab/dic/mecab-ipadic-neologd dicフォルダ


＜mecabrcファイルの編集＞
ファイルのパス
$ find /usr -name mecabrc
Linux: /usr/etc/mecabrc
Mac: /usr/local/etc/mecabrc

編集内容
#指定する辞書の変更
dicdir = .../ipadic
→
dicdir= .../mecab-ipadic-neologd


＜Download J-Medic (medical dictionary for Mecab) 
MANBYO_201907_Dic-utf8.dicのダウンロード
http://sociocom.jp/~data/2018-manbyo/index.html
→→プロジェクトのdicフォルダにダウンロードずみ
