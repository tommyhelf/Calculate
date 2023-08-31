import random
import time

def main():
    # 隨機挑選出兩個不為零的個位數字 A 和 B

    # 計算使用者完成5次計算所需的時間T
    start_time = time.time()
    for i in range(5):
        # 讓使用者輸入 A和B的乘積
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        prompt = f"請輸入{a} x {b}的乘積："
        while True:
            answer = input(prompt)
            if answer.isdigit():
                answer = int(answer)
                if answer == a * b:
                    break
            print("答案錯誤，請重新輸入。")

    # 計算使用者完成5次計算所需的時間T
    end_time = time.time()
    t = end_time - start_time
    print ("花費時間為", round (t,2))
    # 顯示評價
    if t < 10:
        print("你是天才嗎")
    elif t < 15:
        print("不錯呦")
    elif t < 20:
        print("還可以")
    elif t <25:
        print("繼續加油喔")
    else:
        print("國小沒畢業嗎")
    
if __name__ == "__main__":
    main()

# 將程式碼嵌入 HTML 檔案
def render_html():
    html = """
    <html>
        <head>
            <title>乘法測驗</title>
        </head>
        <body>
            <script>
                {{python}}
            </script>
        </body>
    </html>
    """
    return html.replace("{{python}}", main())

render_html()
