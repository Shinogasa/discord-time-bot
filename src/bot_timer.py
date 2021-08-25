import sys
import discord

# Token読み込み
file_name = sys.argv[1]
with open(file_name) as f:
    TOKEN = f.read()

# 接続に必要なオブジェクトを生成
client = discord.Client()

class MentionToVocechannelMembers:

    def __init__(self, server_name, voice_channel_name, text_channel_name):

        self.server_name = server_name   
        self.voice_channel_name = voice_channel_name
        self.text_channel_name = text_channel_name

    def send_nero(self):
        guild = discord.utils.get(client.guilds, name=self.server_name)
        print(guild)

        voice_channel = discord.utils.get(guild.voice_channels, name=self.voice_channel_name)
        
        text_channel = discord.utils.get(guild.text_channels, name=self.text_channel_name)

        # VCに参加している人のID取得
        member = voice_channel.voice_states.keys()

        member_mention = []

        print(member)
        if len(member) == 0:
            return text_channel.send("<@310449075763806209> あ？？？？？？？")
        else:
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

    server_name = 'スナック志乃'
    text_channel_name = 'juke-box'
    

    mention_to_barcounter = MentionToVocechannelMembers(server_name, 'Bar Counter', text_channel_name)
    mention_to_terrace = MentionToVocechannelMembers(server_name, 'Terrace', text_channel_name)


    await mention_to_barcounter.send_nero()
    await mention_to_terrace.send_nero()

    await sys.exit()
   

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
