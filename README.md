# Python Data Analysis Practice（100本ノック）

このリポジトリは、書籍 **『Python実践データ分析100本ノック』** を用いた学習用プロジェクトです。  
Python によるデータ分析の基礎から実践までを、コードとノートブックで整理・管理します。

---

## 📌 目的

- Pythonによるデータ分析の基礎力を身につける
- numpy / pandas / matplotlib / scikit-learn などの主要ライブラリに慣れる
- ノートブックとコードをGitHubで管理する練習
- 将来的な機械学習・可視化・最適化への発展に備える

---

## 📁 ディレクトリ構成

```text
python-data-analysis-practice/
├─ requirements.txt            # 基本（必須）ライブラリ
├─ requirements-vision.txt     # 画像処理系（任意）
├─ requirements-ml.txt         # 機械学習・生成AI系（任意）
├─ requirements-nlp.txt        # 日本語処理系（任意）
├─ notebooks/                  # Jupyter Notebook（各ノック）
├─ data/                       # CSVなどのデータ
├─ .gitignore
└─ README.md
```

---

## 🛠 開発環境

- OS: macOS
- Python: 3.11.x（pyenvで管理）
- エディタ: Visual Studio Code
- 仮想環境: venv

---

## ⚙️ セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/yourname/python-data-analysis-practice.git
cd python-data-analysis-practice
```

### 2. 仮想環境の作成と有効化

```bash
python -m venv .venv
source .venv/bin/activate
```

※ ターミナルの先頭に `(.venv)` が表示されれば有効化されています。

---

### 3. 必須ライブラリのインストール

```bash
pip install -r requirements.txt
```

#### （任意）用途別ライブラリ

```bash
# 画像処理系
pip install -r requirements-vision.txt

# 機械学習・生成AI系
pip install -r requirements-ml.txt

# 日本語処理系
pip install -r requirements-nlp.txt
```

---

## 📓 学習メモ

- 各章・各ノックは `notebooks/` 以下に整理
- エラーや気づきは Notebook 内の Markdown に記録
- 重要なポイントは README に追記する

---

## ⚠️ 注意事項

- `dlib` など一部ライブラリは **ビルドが重く環境依存**のため、必要な場合のみインストールしてください
- torch の GPU（CUDA）対応版は環境ごとに設定が異なるため、本リポジトリでは CPU 版を前提とします

---

## 📚 参考

- Python実践データ分析100本ノック（技術評論社）
- pandas / numpy / scikit-learn 公式ドキュメント

---

## ✍️ Author

- Name: Daiki
- Purpose: Data Analysis Learning & Practice

---

## 🚀 今後の予定

- ノック完了ごとのチェックリスト作成
- グラフ・可視化コードの整理
- 発展的テーマ（最適化・ネットワーク分析）の追加
