import sys
import discord

# Token読み込み
file_name = sys.argv[1]
with open(file_name) as f:
    discord_settings = [s.strip() for s in f.readlines()]
    print(discord_settings)
    TOKEN = discord_settings[0]
    SERVER_NAME = discord_settings[1]
    TEXT_CHANNEL_NAME = discord_settings[2]
    VOICE_CHANNEL_NAME_LIST = discord_settings[3:]

# 接続に必要なオブジェクトを生成
client = discord.Client()

class MentionToVocechannelMembers:

    def __init__(self, server_name, voice_channel_name, text_channel_name):

        print("servername " + server_name +" vc " + voice_channel_name + " tc " + text_channel_name)
        self.server_name = server_name   
        self.voice_channel_name = voice_channel_name
        self.text_channel_name = text_channel_name

    def send_nero(self):
        print(self.server_name)
        guild = discord.utils.get(client.guilds, name=self.server_name)
        print("guild is " + str(guild))

        voice_channel = discord.utils.get(guild.voice_channels, name=self.voice_channel_name)
        
        text_channel = discord.utils.get(guild.text_channels, name=self.text_channel_name)

        # VCに参加している人のID取得
        member = voice_channel.voice_states.keys()

        member_mention = []

        print(member)
        if len(member) == 0:
            return text_channel.send( self.voice_channel_name + "には誰もいません")
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

    for voice_channel_name in VOICE_CHANNEL_NAME_LIST :
        mention_to_voice_channel = MentionToVocechannelMembers(SERVER_NAME, voice_channel_name,TEXT_CHANNEL_NAME)

        await mention_to_voice_channel.send_nero()

    await client.logout()
    await sys.exit()
   
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
