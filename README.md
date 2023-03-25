# サッカーのウェブサイト

Djangoアプリケーションをベースとして, テンプレートを用いてHTTPレスポンスを構造化し, それぞれのビューからテンプレートにデータを渡す.

・views.index
Description : ランディングページ
View: スポーツシーンの画像URLリストをランダムに1つテンプレートに渡す.
Template: index.htmlではimgタグを挿入

・views.rules
Description: ルールの説明
View: テンプレートのレンダリング

・views.detail
Description:選手の名前, 説明
View: 選手の説明

・view.notables
Description:選手への内部リンクリスト

・view.external
Description:スポーツに関する情報を得るための外部リンク
