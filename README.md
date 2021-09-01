＜プログラムの概要＞

　このプログラムはGmailのAPIを用いることで指定したキーワードを含むメールおよび該当する文章の前後の数行を抜き出して一覧表示するプログラムです。

＜作成の背景＞

　私は中島聡さんの「Life is beautiful」というメルマガを購読（愛読）しています。
 
　中島聡さんのメルマガは毎週かなりの長文（情報量満載）です。
 
　そのため、あるキーワードに関する記事を、過去に遡って探したいと思った場合、
 
　Gmailのメーラー等の機能により該当のメールは特定できるのですが、そのメールの中から該当の文章を探すのは結構手間でした。


　そこで、キーワードに関連する部分だけを一覧表示できたら便利なのに！と思い、このプログラムを作成しました。
 
　このプログラムを利用すれば、指定したキーワードが、どの回（どの号）で、何回、どのような文章中で使われたか、

　を一覧化して表示することができます。


＜私の環境＞

　・OS MacOS 11.2.3

　・python 3.7.7
  

＜その他必要事項＞

　・Googleアカウントが必要です。

　・Gmailアドレスが必要です。

　・初回実行時にはWebブラウザでのGoogleアカウント認証が必要です。

　・GmailのAPIを使用する必要があり、それにはGmailAPIを有効化する必要があります。（詳細は次項で説明します。）

＜GmailAPI有効化のクイックスタートガイド＞

　GmailのAPIを使用するには、GmailAPIを有効化する必要があります。

　方法は以下のとおりです。
 
　・まず、Gmail APIでクライアントIDを有効にします。
 
　　→Gmail APIでクライアントIDを有効にするまでの手順は調べたらたくさん出てきますので、そちらを参考にしてみてください。
   
　・クライアントIDが作成できたら、jsonをダウンロードします。
 
　・ダウンロードしたjsonファイルを「credentials.json」にリネームします。
 
　・このプログラム（.py）と同一ディレクトリにjsonファイルを設置し、pythonを実行します。



