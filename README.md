# 说明

使用图像识别的方式来一键切换队伍, 使用热键`alt+1,2,3,4,5,6,7,8,9,0`来切换`1-10`支队伍。
该程序不会修改任何游戏数据，从原理来说不存在封号风险，但是也不保证不会被封号，使用本程序请自行承担风险。
一般情况下该程序不限制分辨率和游戏版本。

# 使用

下载`dist`目录下exe可执行文件，双击运行即可。

# 构建

`Pyinstaller --onefile -F --add-binary "./icon/*;./icon/" --uac-admin --clean --noconsole --icon=.\icon\right.ico .\main.py`
