# これはなに？

文献リポジトリの情報可視化についてのサーベイ論文を見つけたので、その文献リストを作成したものです。

- Federico, P., Heimerl, F., Koch, S., and Miksch, S., [/ [A Survey on Visual Approaches for Analysing Scientific Literature and Patents http://dx.doi.org/10.1109/TVCG.2016.2610422] ], IEEE Transactions on Visualisation and Computer Graphics, 2016.

単なる文献リストではなく、論文中で使われている文献番号 (Citenoフィールド)、論文中に出現する節、各文献の分類タグの情報が含まれています。

このサーベイ論文は文献を番号で引用しており、ハイパーリンクが設定されていないために、各引用の出展を見比べながら読むのがかなり難しいです。その不便を補う目的で、このリストを作成しました。

後述のように Mac ユーザならば BibDesk を利用すれば、快適に閲覧できるような索引情報を追加してあります。


# `references.pdf` はなに？


節ごとの引用文献リストをまとめたものです。後述の BibDesk を利用できない人々のために用意しました。



# ここは Mac ユーザ限定：BibDesk での閲覧にあたって

![BibDesk で閲覧した様子](bibdesk.png)

BibDesk は MacTeX が標準装備している強力な文献管理ソフトです。MacユーザでLaTeXを使っているひとであれば、おそらくすでにインストールされているはずです。/Applications/TeX の下をさがしてみて下さい。ネットでも簡単に見つかります。

BibDesk のデフォルトの設定でもそこそこ見られますが、ここで配布しているサーベイの `.bib` については以下の設定を施すとより快適です。

- BibDesk メニューの **View / Group Fields / Add Group Field...** で **Categories** を追加。

- 表のタイトル (First Author, Year, Title などが列挙されている箇所）を右クリックし、 **Add other ...** で `Citeno` （サーベイで用いられている文献番号を記入するために脇田が追加したカスタムフィールド）を追加。追加されたフィールドをドラッグして列の並びの一番左に移動。

# Federico のサーベイ論文を読むとき

- 特定のセクションを読むときは Static 欄の該当するフォルダを選択すると、その節で引用されている論文が一覧できます。

    たとえば、 **Section 3.2: Citations** のなかの **Section 3.2.3 Synoptic Tasks (Patterns)** を読むときは、Static 欄の **3.2.3 Citation - Patterns** を開いて下さい。 この節で引用されている文献 [57, 67, 68, ..., 74] が表示されます。

    なお、論文の節の表題はわかりにくいと思ったので、BibTeX の Static 欄では、著者らが使っていたタグシステムを参考にした、よりわかりやすいものに変更しました。

- 特定の論文の分類を知るには、論文を検索し、選択すると Static 欄のハイライトでその論文を引用している論文の節が示されます。また、Categories 欄にはその論文の分類タグがハイライトされます。

    たとえば、Koch 2011 [23] を選択すると、この論文が 3.1.1 節と 3.5.4 節で言及されていることがわかります。また、分類タグを見ることで、この論文が特許関連の研究であり、引用情報、メタ情報、テキスト情報を扱っており、タスクとして文献検索、関連性探索、テンポラルな探索をサポートしていることがわかります。

- Categories欄の要素を選択することで、個々のタグに分類された文献のリストを取得できます。

    たとえば、Categories欄の **multiple/5-views** を選択すれば、該当する文献 [0, 30, 34, 39, 55, ...] を取得できます。

    AND 検索を要する検索をする場合は、メニューの **Database / New Smart Group...** を使うのかなぁ。。。高度な検索機能があるといいのだけど。



# この `.bib` ファイルはどのように作成したのか

1. [著者のサイト](http://ieg.ifs.tuwien.ac.at/%7Efederico/LiPatVis/) から元データを入手

1. `[jan, ..., dec] => [1, ..., 12]` なマクロの追加

    biblatex が嫌うため

1. `address` と `location` を共に有する項目について `address` を削除。

    biblatex が嫌うため

1. Markdown で記述された `annotate` 項目の内容を LaTeX 形式に変換

1. Citeno に引用番号を追加：Citeno欄の追加はスクリプト。番号の記入は手作業

1. Keywords 欄を Categories 欄に複製

1. 3章の節それぞれについて Static 欄を作成

1. 論文を Static 欄に分類 (DnD)

1. Static 欄と Categories 欄のラベルをわかりやすいように変更

