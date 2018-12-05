import discord # インストールした discord.py
import random

client = discord.Client() # 接続に使用するオブジェクト
#locaton = ['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']

# 起動時に通知してくれる処理tests
@client.event
async def on_ready():
    print('Fortnite Location Ready')


@client.event
async def on_message(message):
    if message.content.startswith('!flocation'):
        await client.send_message(message.channel, random.choice(['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']))


    if message.content.startswith('!fteam'):
        c = client.get_channel('489330400032849940')
        t1 = client.get_channel('519678340232249344')
        t2 = client.get_channel('519678398214176789')
        mem = c.voice_members
        length = len(mem)
        teammem = -(- length // 2 )
        t1len = len(t1.voice_members)
        t2len = len(t2.voice_members)
        while length > 0:
            if t1len < teammem and t2len < teammem:
                await client.move_member(mem[0], random.choice([t1,t2]))
            elif t1len < teammem:
                await client.move_member(mem[0], t1)
            elif t2len < teammem:
                await client.move_member(mem[0], t2)
            mem = c.voice_members
            length = len(mem)
            t1len = len(t1.voice_members)
            t2len = len(t2.voice_members)


    if message.content.startswith('!fgather'):
        c = client.get_channel('489330400032849940')
        t1 = client.get_channel('519678340232249344')
        t2 = client.get_channel('519678398214176789')

        t1mem = t1.voice_members
        t1len = len(t1mem)
        while t1len > 0:
            await client.move_member(t1mem[0], c)
            t1mem = t1.voice_members
            t1len = len(t1mem)

        t2mem = t2.voice_members
        t2len = len(t2mem)
        while t2len > 0:
            await client.move_member(t2mem[0], c)
            t2mem = t2.voice_members
            t2len = len(t2mem)

    if message.content.startswith('!fcommand'):
        if client.user == message.author:
            return
        await client.send_message(message.channel,'!flocation, !fteam, !fgather')



# botの接続と起動
client.run('NTE5NTU0NDUzODM0MTcwMzk0.DuhAjg.5yDotuamRFXDJQ2e19twGhIJKsE')
