"""[Recommend] Ping"""
def main():
    """[Recommend] Ping"""
    ping = ""
    time = 0
    time_max = time_min = time_sum = 0
    count = 0
    for i in range(1, 8):
        data = str(input())
        if i == 1:
            ping = data[data.find("ping") + 5:]
        if i == 3 and ("[") and ("]") in data:
            ping = data[data.find("[") + 1: data.find("]")]
        elif i > 3 and data.count("time=") != 0:
            time = int(data[data.find("time=") + 5: data.find("ms")])
            if time_max == 0:
                time_min = time
            if time > time_max:
                time_max = time
            if time < time_min:
                time_min = time
            time_sum += time
        if i >= 4 and data.count("Reply") != 0:
            count += 1
    print("Ping statistics for %s:"%(ping))
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s loss),"\
          %(count, 4 - count, str((4 - count) * 25) + "%"))
    if count != 0:
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms"\
              %(time_min, time_max, time_sum / count))
main()

# ; [Recommend] Ping Home Course Problem Solv... Problem [Recommend]...
# ;  Description
# ; Ping

# ; การ Ping คือการส่ง packet ไปที่ Server แล้วให้ Server ตอบกลับมา โดยจะมีการจับเวลาว่า Server ตอบกลับมาช้าหรือเร็วเพียงใด และมี packet loss หรือไม่ (packet ส่งไปไม่ถึง Server หรือ Server ตอบกลับมาไม่ถึง)

# ; การ Ping แต่ละครั้งจะมีการส่ง packet ไปที่ Server จำนวน 4 packets ดังแสดงในแถวที่มีคำว่า Reply from โดยจะมีการแสดงค่าหมายเลข IP ของ Server มาด้วย โดยอาจจะเป็น IPv4 (IP version 4) หรือ IPv6 (IP version 6) ก็ได้

# ; ตัวอย่างที่ 1

# ; C:\Users\chotipat>ping www.google.com

# ; Pinging www.google.com [2404:6800:4001:806::2004] with 32 bytes of data:
# ; Reply from 2404:6800:4001:806::2004: time=27ms
# ; Reply from 2404:6800:4001:806::2004: time=28ms
# ; Reply from 2404:6800:4001:806::2004: time=33ms
# ; Reply from 2404:6800:4001:806::2004: time=28ms

# ; Ping statistics for 2404:6800:4001:806::2004:
# ;     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# ; Approximate round trip times in milli-seconds:
# ;     Minimum = 27ms, Maximum = 33ms, Average = 29ms


# ; ตัวอย่างที่ 2

# ; C:\Users\chotipat>ping www.google.com

# ; Pinging www.google.com [2404:6800:4001:806::2004] with 32 bytes of data:
# ; Reply from 2404:6800:4001:806::2004: time=44ms
# ; Reply from 2404:6800:4001:806::2004: time=32ms
# ; Reply from 2404:6800:4001:806::2004: time=38ms
# ; Reply from 2404:6800:4001:806::2004: time=28ms

# ; Ping statistics for 2404:6800:4001:806::2004:
# ;     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# ; Approximate round trip times in milli-seconds:
# ;     Minimum = 28ms, Maximum = 44ms, Average = 35ms

# ; กำหนดให้รับค่าผลการตอบรับจาก Server แล้วให้พิมพ์แค่ Statistics ดังตัวอย่าง



 
# ; by นายเชาว์วัฒน์ ยาทองชุน
# ; 22 September 2021, 00:06
# ;  Specification
# ;  Input Specification	 Output Specification

# ; ข้อความจำนวน 7 บรรทัด

# ; ข้อความจำนวน 4 บรรทัด
# ;  Sample Case
# ;  Sample Input	 Sample Output
# ; C:\Users\chotipat>ping www.google.com

# ; Pinging www.google.com [2404:6800:4001:806::2004] with 32 bytes of data:
# ; Reply from 2404:6800:4001:806::2004: time=27ms
# ; Reply from 2404:6800:4001:806::2004: time=28ms
# ; Reply from 2404:6800:4001:806::2004: time=33ms
# ; Reply from 2404:6800:4001:806::2004: time=28ms
# ; Ping statistics for 2404:6800:4001:806::2004:
# ;     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# ; Approximate round trip times in milli-seconds:
# ;     Minimum = 27ms, Maximum = 33ms, Average = 29ms
# ; C:\Users\chotipat>ping www.google.com

# ; Pinging www.google.com [2404:6800:4001:806::2004] with 32 bytes of data:
# ; Reply from 2404:6800:4001:806::2004: time=44ms
# ; Reply from 2404:6800:4001:806::2004: time=32ms
# ; Reply from 2404:6800:4001:806::2004: time=38ms
# ; Reply from 2404:6800:4001:806::2004: time=28ms
# ; Ping statistics for 2404:6800:4001:806::2004:
# ;     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# ; Approximate round trip times in milli-seconds:
# ;     Minimum = 28ms, Maximum = 44ms, Average = 35ms
# ; C:\Users\chotipat>ping www.facebook.com

# ; Pinging star-mini.c10r.facebook.com [157.240.10.35] with 32 bytes of data:
# ; Reply from 157.240.10.35: bytes=32 time=24ms TTL=51
# ; Reply from 157.240.10.35: bytes=32 time=120ms TTL=51
# ; Reply from 157.240.10.35: bytes=32 time=25ms TTL=51
# ; General failure.

# ; Ping statistics for 157.240.10.35:
# ;     Packets: Sent = 4, Received = 3, Lost = 1 (25% loss),
# ; Approximate round trip times in milli-seconds:
# ;     Minimum = 24ms, Maximum = 120ms, Average = 56ms
# ; D:\Photo\MyGirlFriend\Lastday_14-2-2019>ping 127.0.0.1

# ; Pinging 127.0.0.1 with 32 bytes of data:
# ; Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
# ; Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
# ; Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
# ; Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
# ; Ping statistics for 127.0.0.1:
# ;     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# ; Approximate round trip times in milli-seconds:
# ;     Minimum = 0ms, Maximum = 0ms, Average = 0ms
# ; C:\Users\KMITL>ping onlearn.it.kmitl.ac.th

# ; Pinging onlearn.it.kmitl.ac.th [161.246.38.36] with 32 bytes of data:
# ; Request timed out.
# ; Request timed out.
# ; Request timed out.
# ; Request timed out.
# ; Ping statistics for 161.246.38.36:
# ;     Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),