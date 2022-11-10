<code>
  <ol style="list-style:decimal-leading-zero outside;in-left:0;padding-left:36px;margin:0;background-color:#F7F7F7;color:#000;">
                <li>import schedule</li>
                <li>import time</li>
                <li></li>
                <li>#時間設定</li>
                <li>print(<font style="color:brown;">"スリープBGMを再生する時間を指定してください"</font>)</li>
                <li>hour = input(<font style="color:brown;">"時間（hour）:"</font>)</li>
                <li>minute = input(<font style="color:brown;">"分（minute）:"</font>)</li>
                <li>target = f<font style="color:brown;">"{hour.zfill(2)}:{minute.zfill(2)}"</font></li>
                <li>print(target+<font style="color:brown;">"に再生時間を設定しました"</font>)</li>
                <li></li>
                <li>#再生したい動画を指定</li>
                <li>print(<font style="color:brown;">"再生したいスリープBGMのURLを貼ってください"</font>)</li>
                <li>movie = input(<font style="color:brown;">"URL :"</font>)</li>
                <li>print(target+<font style="color:brown;">"に指定したBGMを再生します"</font>)</li>
                <li></li>
                <li>#defは「定義」ということ</li>
                <li>def job():</li>
                <li>&nbsp;&nbsp;&nbsp;&nbsp;import webbrowser</li>
                <li>&nbsp;&nbsp;&nbsp;&nbsp;webbrowser.open(movie)</li>
                <li></li>
                <li>schedule.every().day.at(target).do(job)</li>
                <li></li>
                <li>#時間待ち</li>
                <li>while True:</li>
                <li>&nbsp;&nbsp;schedule.run_pending()</li>
                <li>&nbsp;&nbsp;time.sleep(60)</li>
                </ol></code>