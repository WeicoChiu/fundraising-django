Django-Fundrasing-demo
===

Django 實作募資網站(Nginx + Supervisor + Gunicorn + Django + MySQL)

功能實作
---

+ 會員註冊和登入(支持 username 或 email 登入)
+ 使用者新增、刪除或修改募資方案
+ 募資方案關鍵字搜尋
+ 查看目前已贊助的方案
+ 藍新金流作為第三方金流支付(信用卡或ATM轉帳)
+ 上傳圖片檔案至 Cloud Storage(GCP)
+ [Restful API(部分功能實作)](https://github.com/WeicoChiu/fundraising-django/tree/restfulAPI)
	+ JWT 認證機制
	+ API 文件自動生成
+ Docker 自動化部署(Gunicorn + Django + MySQL)

使用技術
---

+ 後端:
	+ Django(3.2.5)
    	+ django-storages
	+ DjangoRest Framework(3.1)
		+ Simple JWT
		+ dry-yasg
+ 前端:
	+ Bootstrap(5.13)
+ 資料庫:
	+ MySQL
+ 部署:
	+ Nginx
		+ Certbot(Let's encrypt)
	+ Supervisor
	+ Gunicorn
	+ Docker
	+ GCP
		+ Cloud Computing(Ubuntu virtual machine)
		+ Cloud Storage(static files)
			+ google-cloud-storage
		+ Cloud SQL

網站預覽
---
![](https://storage.googleapis.com/fundraising-static-bucket/Fundraising-demo.gif)

資料庫設計
---
[![](https://i.imgur.com/WCkHrZo.png)](https://drawsql.app/myself-69/diagrams/donaterasing)

安裝教學
---
[開發版部署](https://hackmd.io/@Weico/rJOEM6fit)<br>
上線版部署 [TODO]<br>
Docker 版部署 [TODO]

參考資料
---
[Securely Deploy a Django App With Gunicorn, Nginx, & HTTPS](https://realpython.com/django-nginx-gunicorn/)<br>
[Nginx+Gunicorn+Supervisor 部署 Django 部落格應用](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/74/)
