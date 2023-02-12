# PTITCTF 2023

CTF lần này có 2 Crypto, ***Easy Crypto*** và ***Just for fun***

## Easy Crypto

Challenge cho mình một file [EzCrypto.txt](Easy Crypto/EzCrypto.txt), mở file ra thì mình nhần được một con số : 

```56369025297691660392004556373781623445966955195801799383478576454199136227591253023415024495794577295554691617060609433091389```

Chưa biết là có đúng như linh cảm hay không, nhưng việc đầu tiên mình thử là đổi nó về bytes (hơn nữa chall description cũng có nói là kết hợp giữa 2 loại mã hóa, nên cũng có chút tự tin) :

```Python
c = 56369025297691660392004556373781623445966955195801799383478576454199136227591253023415024495794577295554691617060609433091389
print(long_to_bytes(c))
```

Kết quả in ra : `b'UElTQ1RGe1RoMXNfMXNfNF9tM3NTQGczX0ZyMG1fQ3JZcHQwfQ=='`

Kết quả đang ở `base64`. Why ? Một dấu hiệu để nhận biết là cái padding `=` ở cuối

Vậy tiếp tục decode base64 thui :

```Python
c = b'UElTQ1RGe1RoMXNfMXNfNF9tM3NTQGczX0ZyMG1fQ3JZcHQwfQ=='
print(base64.b64decode(c))
```

Thế là ra flag : `b'PISCTF{Th1s_1s_4_m3sS@g3_Fr0m_CrYpt0}'`

Full solve : [Solve.py](Easy Crypto/Solve.py)

## Just for fun

Theo mình cảm nhận là nó hơi guessy vì Tiktok gần đây lắc hông nhiều lắm :(


