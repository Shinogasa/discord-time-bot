import sys
import discord

# Token読み込み
file_name = sys.argv[1]
with open(file_name) as f:
    TOKEN = f.read()

# 接続に必要なオブジェクトを生成
client = discord.Client()

class MentionNero:

    server_name = 'Your server name'
    voice_channel_name = 'Your voice channel name'
    text_channel_name = 'Your text channel name'

    def send_message(self):
        guild = discord.utils.get(client.guilds, name=self.server_name)
        print(guild)

        voice_channel = discord.utils.get(guild.voice_channels, name=self.voice_channel_name)
        
        text_channel = discord.utils.get(guild.text_channels, name=self.text_channel_name)

        # VCに参加している人のID取得
        member = voice_channel.voice_states.keys()

        member_mention = []

        # メンション作成
        for i in member :
            print(i)
            member = "<@" + str(i) + ">"
            member_mention.append(member)

        # Botからメンション飛ばす
        return text_channel.send( str(" ".join(member_mention)) + " そろそろ寝ませんか？")

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        nero = MentionNero()

        await nero.send_message()
    

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
