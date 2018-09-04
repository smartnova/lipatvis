# How I created this BibDesk

1. The original BibTeX database is [kindly offered by the survey authors](http://ieg.ifs.tuwien.ac.at/%7Efederico/LiPatVis/).

1. Addition of month macros: `[jan, ..., dec] => [1, ..., 12]`

1. When both `address` and `location` fields are given I dropped the `address` field.

1. Markdown で記述された `annotate` 項目の内容を LaTeX 形式に変換

1. Citeno に引用番号を追加：Citeno欄の追加はスクリプト。番号の記入は手作業

1. Copied Keywords 欄を Categories 欄に複製

1. 3章の節それぞれについて Static 欄を作成

1. 論文を Static 欄に分類 (DnD)

1. Static 欄と Categories 欄のラベルをわかりやすいように変更


