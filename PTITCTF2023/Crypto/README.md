# PTITCTF 2023

CTF lần này có 2 Crypto, ***Easy Crypto*** và ***Just for fun***

## Easy Crypto

Challenge cho mình một file [EzCrypto.txt](https://github.com/HappyFalcon22/Writeup/blob/Master/PTITCTF2023/Crypto/Easy%20Crypto/EzCrypto.txt), mở file ra thì mình nhần được một con số : 

```56369025297691660392004556373781623445966955195801799383478576454199136227591253023415024495794577295554691617060609433091389```

Việc đầu tiên mình thử là đổi nó về bytes (hơn nữa chall description cũng có nói là kết hợp giữa 2 loại mã hóa, nên cũng có chút tự tin) :

```Python
c = 56369025297691660392004556373781623445966955195801799383478576454199136227591253023415024495794577295554691617060609433091389
print(long_to_bytes(c))
```

Kết quả in ra : `b'UElTQ1RGe1RoMXNfMXNfNF9tM3NTQGczX0ZyMG1fQ3JZcHQwfQ=='`

Kết quả đang ở `base64` vì có một ký hiệu padding `=` ở cuối

Vậy tiếp tục decode base64 thui :

```Python
c = b'UElTQ1RGe1RoMXNfMXNfNF9tM3NTQGczX0ZyMG1fQ3JZcHQwfQ=='
print(base64.b64decode(c))
```

Thế là ra flag : `b'PISCTF{Th1s_1s_4_m3sS@g3_Fr0m_CrYpt0}'`

Full solve : [Solve.py](https://github.com/HappyFalcon22/Writeup/blob/Master/PTITCTF2023/Crypto/Easy%20Crypto/Solve.py)

## Just for fun

Theo mình cảm nhận là nó hơi guessy vì Tiktok gần đây lắc hông nhiều lắm :(

Trước tiên, mình nhận được 1 ciphertext : `limh_xwd_oqkl_zndn_ieclithkqv`

và source code [crypto2.py](https://github.com/HappyFalcon22/Writeup/blob/Master/PTITCTF2023/Crypto/Just%20For%20Fun/crypto2.py)

Theo source code thì đây là một subtitution cipher thuần, tức là không có lỗi nào trong việc hiện thực. Có vài cách để đánh cái cipher này
+ Dùng phân tích tần số (frequency analysis) : Tuy nhiên, ciphertext này quá ngắn để thực hiện
+ Vét cạn (bruteforce) : Không khả thi nốt vì số trường hợp quá lớn (26!)

Oke, hơi bí rồi thì bỗng nhớ lại cái description :

> Trong lúc viết đoạn code này tôi chợt nghĩ đến vũ điệu lắc hông của ai đó mà không thể nhớ nổi! Bạn có đoán được là ai không? Hmmm... nghĩ lại vẫn còn nổi da gà 😑

Không biết đây có phải là intended solution không nhưng mình nghĩ tới MONO với cái điệu lắc hông hôm LIVE Waiting For You đầu tiên. Nên mình cũng thử với cái ciphertext này xem sao : mình nhìn vào 1 đoạn của ciphertext : `zndn`, khá có khả năng là `mono`, thế thử thì nó ra :

`limk_xwn_oqkk_mono_ieclithkqv`

Cùng lúc đó mình chợt nhớ tới loại của cipher này : ***monoalphabetic cipher***, vì vậy, trước khi mình quăng đống ciphertext này vào Cryptogram Solver thì mình xem thử xem cái đoạn `ieclithkqv` có đúng là từ `alphabetic` hay không, 2 chữ `i` của ciphertext này đặt đúng chỗ, và các chữ còn lại của ciphertext và `alphabetic` đều khác nhau. Hợp lý, mình thay vào thử thì được : 

`hame_xwn_oith_mono_alphabetic`

Vậy là đúng hướng rồi , `oith` thì có thể là từ `with`, từ đây thì mình đoán luôn đoạn đầu là `have fun` :

`have_fun_with_mono_alphabetic`

Warp lại theo format và nộp flag thôi.




