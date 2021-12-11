#【毎日Python】Pythonで辞書のデータに要素を追加する方法｜setdefault
#https://www.youtube.com/watch?v=RjFGpbCQ9AA

d = {'apple':100, 'banana':150,
     'peach':230}

d.setdefault('cherry',210) #要素追加
d #{'apple': 100, 'banana': 150, 'cherry': 210, 'peach': 230}

d.setdefault('blueberry') #キーのみ指定
d #{'apple': 100, 'banana': 150, 'blueberry': None, 'cherry': 210, 'peach': 230}

d.setdefault('peach',500) #すでに存在するキーに対して値変更はできない
d #{'apple': 100, 'banana': 150, 'blueberry': None, 'cherry': 210, 'peach': 230}

d['peach']=500 #やるならこう
d #{'apple': 100, 'banana': 150, 'blueberry': None, 'cherry': 210, 'peach': 500}