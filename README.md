# README

これは特定のVCに参加しているユーザーへメンションを飛ばすBOTです

## How to build

コンテナ起動

```bash
docker-compose up -d --build
```

コンテナへアクセス

```bash
docker exec -it bot bash
```

個人的にはVSCodeにコンテナアタッチして開発のほうが楽です

## How to use

[/src/token/token](./src/token/token)へBotのTokenを記載しておくこと

```bash
python bot.py ./token/token
```

## 参考

- <https://qiita.com/1ntegrale9/items/cb285053f2fa5d0cccdf>
- <https://teratail.com/questions/275857>

## Special Thanks

モブプロでアドバイスをくれた素敵なエンジニアの方々

- [cormojs](https://nayukana.info/@cormojs)
- [いぶし銀P](https://twitter.com/pimako_P)
