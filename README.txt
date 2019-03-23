注意：
    1.因为可能是xadmin的bug导致添加addform自定义控件的时候会找不到app activityrecord，
    目测是没有区分大小写，
    所以把Python\Python36\Lib\site-packages\django\apps\registry.py 的第 147行添加
            if app_label == "activityrecord":
                app_label = "activityRecord"
    权宜之计，但挺有效