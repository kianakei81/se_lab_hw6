# se_lab_hw6

به نام خدا
در این آزمایش به پیاده سازی یک کد backend و سپس dockerize کردن آن میپردازیم. ساختار و کد نهایی بکند در اسکرین شات های زیر نمایش داده شده است. ساختار کلی به این صورت است که app به عنوان interface عمل می کند و درخواست های ورودی را به سرویس های user و item ارسال می کند.

![img_5.png](screenshots/img_5.png)
![img_6.png](screenshots/img_6.png)
![img_7.png](screenshots/img_7.png)
![img_8.png](screenshots/img_8.png)
![img_9.png](screenshots/img_9.png)

اکنون داکر را راه اندازی کرده و اقدام به build و اجرا کردن imageها می کنیم:

![img_10.png](screenshots/img_10.png)
![img_11.png](screenshots/img_11.png)
![img_13.png](screenshots/img_13.png)

در اینجا مشاهده می کنیم که سه سرور مد نظر بالا آمده اند (دو سرویس بکندی و یک سرور interface)

![img_14.png](screenshots/img_14.png)

اندکی تست روی سرور اجرا می کنیم:

![img_15.png](screenshots/img_15.png)

مشاهده می کنیم که تست ها به خوبی اجرا می شوند. اکنون دستورات docker container ls و docker image ls را اجرا می کنیم:

![img_16.png](screenshots/img_16.png)

یک راه جهت کنترل لود بیشتر روی سرور استفاده از caching است که nginx این امکان را به ما می دهد. خط های زیر را به nginx.conf اضافه کرده و سرور را دوباره اجرا می کنیم تا از صحت عملکرد مطمئن شویم:

![img_17.png](screenshots/img_17.png)
![img_18.png](screenshots/img_18.png)
![img_19.png](screenshots/img_19.png)