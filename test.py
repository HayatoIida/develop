import discord # インストールした discord.py
import random
import math

length = math.ceil(7/2)
print(str(length))



# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('!flocation'):
        await client.send_message(message.channel, random.choice(['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']))

    if message.content.startswith('!fteam'):
        mem = c.voice_members
        length = math.ceil(len(mem)/2)
        for x in mem:
            t1len = len(t1.voice_members)
            t2len = len(t2.voice_members)
            if t1len < length and t2len < length:
                await client.move_member(x, random.choice([t1,t2]))
            elif t1 < length:
                await client.move_member(x, t1)
            elif t2 < length:
                await client.move_member(x, t2)

    if message.content.startswith('!fgather'):
        t1mem = t1.voice_members
        for x in t1mem:
            await client.move_member(x, c)
        t2mem = t2.voice_members
        for x in t2mem:
            await client.move_member(x, c)


# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTE5NTU0NDUzODM0MTcwMzk0.DuhAjg.5yDotuamRFXDJQ2e19twGhIJKsE')
