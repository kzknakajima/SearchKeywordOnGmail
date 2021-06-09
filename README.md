＜概要＞

GmailのAPIを用いることで、Gmail内で、
指定したキーワードを含むメールおよびメールの文章を検索結果として表示するプログラムです。


私は中島聡さんの「Life is beautiful」というメルマガを購読しています。
中島聡さんのメルマガは一つ一つがかなり長文（情報量満載）のため、
気になるキーワードが利用されている箇所をさかのぼって検索したいと思っても、
そのメールを探すのも大変ですし、メールを特定できたとしても長文の中からその箇所を探すのは大変です。


そこで本プログラムを利用すれば、いつのメルマガ回に、何回くらい、どのような文脈でキーワードが使われたか、
をリスト化することができます。


＜メイン関数の説明＞

main関数の初めの２行で引数を設定します。
  
  queryはGmailのAPIに投げるクエリ（検索条件）です。
  例えば、'from:mailmag@mag2premium.com'と設定することで、
  上記のメールアドレスから受信したメールを抽出できます。
  
  max_Resultsはqueryでヒットさせるメールの最大件数を設定します。
  この最大件数を設定しておくことで、最新のメールのみに絞って検索することができます。
  
＜環境＞

OS MacOS 11.2.3

python 3.7.7

＜その他＞

Googleアカウントが必要です。
Gmailのメールアドレスが必要です。
初回実行時にはWebブラウザでのGoogleアカウント認証が必要です。

＜クイックスタートガイド＞

GmailのAPIを使用するには、GmailAPIを有効化する必要があります。
クライアントIDが作成できたら、jsonをダウンロードします。
ダウンロードしたjsonファイルを「credentials.json」にリネームします。
pythonファイルと同一ディレクトリにjsonファイルを設置し、
pythonファイルを実行します。

＜参考URL＞

https://qiita.com/orikei/items/73dc1ccc95d1872ab1cf
