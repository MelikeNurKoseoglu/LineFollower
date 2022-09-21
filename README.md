### LineFollower (Çizgi Takibi)

-Line Follower(Çizgi takibi) projesinde Raspberry Pi 4 Model B+ bilgisayarı kullanılarak görüntü işleme ile siyah çizgi takibi yapılmıştır.

-Porjede 'Python' programlama dili ve kütüphanelerinden Open Cv, Numpy ve RPi.GPIO kullanılmıştır.

-Line Follower projesinde siyah çizgi takibi yaparken  belirli alt ve üst renk aralıklarındaki siyah rengi algılayıp kontür işlemi yapılıyor.Yapılan kontür işleminde en büyük kontür alanı belirlenip bu alanın orta noktasına bir daire çiziliyor. Çizilen daire açılan pencerenin(frame) x eksenindeki konumuna göre aracın gitmesi gereken yönü belirleniyor. Yön belirlendikten sonra  GPIO pinlerine komut gönderiliyor. Bu komutlara göre PWM değeri ayarlanmış olan aracın sağ , sol veya düz gitmesi için Dc motorlar hıgh ve low değerlerini uygulayarak araca yön veriyor. Çizginin algılanmaması durumunda (belirlenen alt ve üst değerlere sahip renk bulunmazsa) GPIO pinleri ile Dc motorlara low değeri gönderiliyor.

-Raspberry GPIO pinleri ile L298N motor sürücü kartı  bağlantıları şu şekilde yapılmıştır:
- ✨Enable pinleri raspberry pi üzerinde pvm pinlerine bağlanmıştır.
- ✨İnput pinleri raspberry pi üzerinde GPIO4 GPIO17 GPIO27 GPIO22 pinlerine bağlanmıştır.
- ✨Motor sürücü kartındaki diğer çıkışlardan birini raspberry pi üzerindeki pinlerden 5volta diğerini de gnd pinine bağlanmıştır.
  
  
  

-Araçta kullanılan malzemler
- ✨Raspberry Pi 4 Model B+
- ✨Raspberry Kamera Modülü
- ✨L298N Motor Sürücü Kartı
- ✨4 adet 12V DC motors
- ✨Güç Kaynağı
- ✨Jupmer Kablo

## Çizgi takibi projesinden  görüntüler


https://user-images.githubusercontent.com/74611768/191590479-98ad6ca7-db50-4ff0-80c6-02cba3a6252a.mp4

## Güç kaynağı ve motor sürücü kartı bağlantıları

![WhatsApp Image 2022-09-07 at 14 49 10 (1)](https://user-images.githubusercontent.com/74611768/189600127-a2d4b6eb-8edc-4510-b6e4-38601479cb04.jpeg)

## Motor sürücü kartı 
![WhatsApp Image 2022-09-07 at 14 49 10](https://user-images.githubusercontent.com/74611768/189600535-f09c532f-3364-44ec-a01a-6ecb0620584b.jpeg)











### 📩 Connect with me:

[<img align="left" height="24" width="24" src="https://cdn.jsdelivr.net/npm/simple-icons@v4/icons/gmail.svg" />][gmail]

[<img align="left" alt="linkedin | LinkedIn" width="24px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg" />][linkedin]

<br />

[linkedin]:https://www.linkedin.com/in/melike-nur-k%C3%B6seo%C4%9Flu-2aaa27209/

[gmail]: mailto:koseoglumelikenur@gmail.com

<br />
