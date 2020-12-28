# ロボットシステム学　課題２

## 概要
ROS2とRPi.GPIOを用いてRaspberry Pi4 ModelB でLEDを操作する。

## プログラムの説明
サブスクライバがパブリッシャから読み込んだ値が3の倍数の時LEDが点灯します。

## 使用方法
1. ledの+側をGPIO21に繋げる
2. sudo chmod 666 /dev/gpio*　を実行する
3. colcon build　を実行する
4. 端末1で　ros2 run mypkg talker　を実行する
5. 端末2で　ros2 run mypkg listener　を実行する
6. Ctrl + c　で終了
