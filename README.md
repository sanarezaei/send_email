# 📬 Contact API - Django REST Framework

یک پروژه ساده و کاربردی با Django REST Framework برای پیاده‌سازی فرم تماس با ما.  
کاربر می‌تونه با ارسال درخواست POST، پیام خودش رو برای مدیر سایت ارسال کنه و سیستم به‌صورت خودکار ایمیل ارسال می‌کنه.

---

## ✨ Features

- ارسال پیام کاربر از طریق API
- ولیدیشن فرم با `serializers`
- ارسال ایمیل با استفاده از `django.core.mail`
- ساختار تمیز و آماده برای توسعه بیشتر (Celery، ذخیره در DB و...)

---

## 🔧 Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- SMTP Email Backend / Console Backend

---

## 📦 نصب و راه‌اندازی

### 1. کلون کردن پروژه

```bash
git clone https://github.com/your-username/contact-api.git
cd contact-api
