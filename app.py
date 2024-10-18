from flask import Flask, render_template, request
app = Flask(__name__)


player_score = {
    "Player1": 0,
    "Player2": 0
}
current_player = "Player1"
dart_left = int(3)

score_history = []

#################初期画面#####################
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


#################モードセレクト中継リンク#####################
@app.route('/select_mode',methods=['POST'])
def select_mode():
    global current_player
    global player_score
    global score_history
    global dart_left

    current_player = "Player1"
    player_score = {
        "Player1": 0,
        "Player2": 0
    }
    score_history.clear()
    dart_left = int(3)

    mode = request.form.get('mode')
    if mode == 'CountUp':
        return CountUp()
    #if mode == 'ZeroOne':...


#################ボードクリック計算#####################
@app.route('/calculate', methods=['POST'])
def calculate():
    global current_player
    global dart_left
    if dart_left > 0:
        dart_left = dart_left-1
        thisPoint = int(request.form.get('score'))
        score_history.append((current_player, thisPoint))
        player_score[current_player] += thisPoint
        return render_template('CountUp.html', player1_score=player_score["Player1"], player2_score=player_score["Player2"],current_player=current_player,dart_left=dart_left)
    else:
        return render_template('CountUp.html', player1_score=player_score["Player1"], player2_score=player_score["Player2"],current_player=current_player,dart_left=dart_left, flg=True)
    


#################NextPlayer#####################
@app.route('/next_player', methods=['POSt'])
def next_player():
    global current_player
    global dart_left
    dart_left = int(3)
    if current_player =="Player1":
        current_player = "Player2"
    else:
        current_player = "Player1"
    return render_template('CountUp.html', player1_score=player_score["Player1"], player2_score=player_score["Player2"],current_player=current_player,dart_left=dart_left)


#################取り消しボタン#####################
@app.route('/undo',methods=['POST'])
def undo():
    global current_player
    global dart_left
    if score_history and dart_left < 3:
        dart_left = dart_left + 1
        last_score = score_history.pop()
        player,thisPoint = last_score
        player_score[player] -= thisPoint
    return render_template('CountUp.html', player1_score=player_score["Player1"], player2_score=player_score["Player2"],current_player=current_player,dart_left=dart_left)


#################カウントアップ初期表示#####################
def CountUp():
    return render_template('CountUp.html', player1_score=0, player2_score=0,current_player=current_player,dart_left=dart_left)


if __name__ == '__main__':
    app.run(debug=True)