import sys
import random

def get_user_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("無効な入力です。整数を入力してください。")
        get_user_input(prompt)

def main():
    print("Rondom Number!!")
    N = get_user_input("最小値の入力をしてください")
    M = get_user_input("最大値の入力をしてください")

    if N > M:
        print("エラー：最小値は最大値よりちいさくなければなりません。")
        sys.exit(1)
    
    target_number = random.randint(N, M)

    print(f"NからMの間の数。")
    attempt = 3
    for attempt in range(attempt):
        guess = get_user_input(f"{attempt + 1}回目の入力：")
        
        if guess == target_number:
            print("正解！！")
            break
        elif guess < target_number:
            print("もっと大きい")
        else:
            print("もっと小さい")
    if guess != target_number:
        print("不正解。答えは{target_number}でした")

if __name__=="__main__":
    main()

