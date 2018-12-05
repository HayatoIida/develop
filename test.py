import discord # インストールした discord.py
import random
import math

client = discord.Client() # 接続に使用するオブジェクト
#locaton = ['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']

# 起動時に通知してくれる処理tests
@client.event
async def on_ready():
    print('Fortnite Location Ready')


# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('!flocation'):
        await client.send_message(message.channel, random.choice(['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']))

    if message.content.startswith('!fteam'):
        c = client.get_channel('518769872944103442')
        t1 = client.get_channel('519646996118896661')
        t2 = client.get_channel('519646907639791616')
        mem = c.voice_members
        l = len(mem)
        length = -(- l // 2 )
        for x in mem:
            t1len = len(t1.voice_members)
            t2len = len(t2.voice_members)
            if t1len < length and t2len < length:
                await client.move_member(x, random.choice([t1,t2]))
            elif t1len < length:
                await client.move_member(x, t1)
            elif t2len < length:
                await client.move_member(x, t2)

    if message.content.startswith('!fgather'):
        c = client.get_channel('518769872944103442')
        t1 = client.get_channel('519646996118896661')
        t2 = client.get_channel('519646907639791616')
        t1mem = t1.voice_members
        for x in t1mem:
            await client.move_member(x, c)
        t2mem = t2.voice_members
        for x in t2mem:
            await client.move_member(x, c)

    if message.content.startswith('!fcommand'):
        if client.user == message.author:
            return
        await client.send_message(message.channel,'!flocation: random location /n !fteam: random team /n !fgather:gether user')



# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTE5NTU0NDUzODM0MTcwMzk0.DuhAjg.5yDotuamRFXDJQ2e19twGhIJKsE')
