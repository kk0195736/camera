# -*- coding: utf-8 -*-
import openai
from voice_to_text import recognize_speech_from_mic
import key

# あなたのOpenAI APIキーをセットアップ
openai.api_key = key.AP

SECRET_PHRASE = "オープンセサミ"  # 実際の合言葉を設定してください。


def verify_phrase_with_gpt3(input_phrase):
    prompt = f"""
    合言葉は{SECRET_PHRASE}です。以下は合言葉でしょうか？そうである場合は「はい」を、違う場合は「いいえ」を返してください。
    {input_phrase}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    response_content = response.choices[0]["message"]["content"].strip()
    # print(f"GPT-3 Request: {prompt}")  # GPT-3へのリクエストを表示
    # print(f"GPT-3 Response: {response_content}")  # GPT-3からのレスポンスを表示
    return response_content


def main():
    print("合言葉を入力してください: ")
    user_input = recognize_speech_from_mic()
    print(user_input)

    if verify_phrase_with_gpt3(user_input) == "はい":
        print("解錠しました！")
    else:
        print("合言葉が違います。")


if __name__ == "__main__":
    main()
