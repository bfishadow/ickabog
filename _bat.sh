#curl "https://www.theickabog.com/rebellion/" -o "en 60.html"
#curl "https://www.theickabog.com/ch/%e5%bc%97%e8%8e%b1%e5%be%b7%e5%9b%bd%e7%8e%8b%e5%bf%a7%e5%bf%83%e5%bf%a1%e5%bf%a1/" -o "cn 33.html"
#curl "https://www.theickabog.com/ch/%e5%8f%a6%e5%a4%96%e4%b8%89%e5%8f%aa%e8%84%9a/" -o "cn 34.html"

python3 _parse.py "en 60.html" > engb_section0060.xhtml
python3 _parse.py "cn 33.html" > zhcn_section0033.xhtml
python3 _parse.py "cn 34.html" > zhcn_section0034.xhtml
