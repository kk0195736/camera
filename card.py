# -*- coding: utf-8 -*-
from smartcard.System import readers
import smartcard.util
from key_open import key_open
from display_message import display_message
import key

flag = False

# カードリーダーを取得する
reader_list = readers()
if len(reader_list) < 1:
    print('カードリーダーが見つかりませんでした。')
    exit()
reader = reader_list[0]

# 接続する
#print('カードリーダーに接続中...')
connection = reader.createConnection()
while True:
    try:
        connection.connect()
        #print('カードリーダーに接続しました。')

        # カード情報を読み取る
        while True:
            try:
                # カードUIDを読み取る
                SELECT = [0xFF, 0xCA, 0x00, 0x00, 0x00]
                response, sw1, sw2 = connection.transmit(SELECT)
                uid = smartcard.util.toHexString(response)

                # 結果を出力する
                if flag == False:
                    print('カード情報:', uid)
                    if uid == key.KI or uid == key.AI:
                        print('open')
                        key_open()
                        display_message('メッセージ', 'OPEN')
                    else:
                        display_message('メッセージ', 'REJECTED')
                        print('rejected')
                    flag = True
                # 切断する
                connection.disconnect()
                #print('カードリーダーから切断しました。')
                break

            except Exception as e:
                print('カードリーダーからの読み取りエラー:', e)

    except Exception as e:
        flag = False
        #print('カードリーダーに接続できませんでした。', e)

# 切断する
connection.disconnect()
print('カードリーダーから切断しました。')

