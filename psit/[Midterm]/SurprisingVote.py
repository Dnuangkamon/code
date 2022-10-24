"""SurprisingVote"""
def main():
    """SurprisingVote"""
    score = float(input()) #20
    score_maxx = float(input()) #8
    score_summ = score-score_maxx #12
    if score_summ > score_maxx:
        score_summ_2 = score_summ-score_maxx #12-8 = 4
    elif score_summ <= score_maxx:
        score_summ_2 = 0
    if score_maxx-score_summ_2 > 2:
        print('Surprising')
    else:
        print('Not surprising')
main()

# หลังจากฉันและเพื่อนๆฉันอีกสองคน(????)ได้ใช้เครื่องไล่ยุงนี้
# ก็ถึงเวลาโหวดให้คะแนนกับเครื่องนี้ที่หน้าเว็ปที่พวกฉันซื้อมา

# ระบบให้คะแนนนั้นสามารถให้ได้ตั้งแต่ 0 ถึง 10 คะแนน เป็นจำนวนจริง
# เมื่อพวกฉันโหวดกันเสร็จแล้ว ระบบจะแสดงเพียงคะแนนรวม และคะแนนสูงสุดเพียงค่าเดียว

# อย่างไรก็ตาม คน(?)ซื้อคน(???)อื่นก็ยังสามารถเข้าไปดูคะแนนรายคน(??????? ...พอเถอะ)ได้อยู่ดี
# ถ้าคะแนนโหวดของคนที่ให้คะแนนสูงสุด และคะแนนต่ำสุดห่างกันเกินสองคะแนน จะทำให้คนมาดูคะแนนรู้สึกประหลาดใจ (Surprising)
# และพาลคิดไปว่า มันต้องมีหน้าม้ามาอวยแน่ๆ!!
# ทำให้อาจรับการกระทำนั้นไม่ได้อย่างยิ่งยวด จนตกใจจนเกิดอาการหัวใจวายตายในที่สุด...

# ระบบเว็ปจึงต้องมีการแจ้งว่า มีโอกาสที่จะเกิด Surprising หรือไม่ที่หน้ารีวิวสินค้า

# Surprising ถ้ามีโอกาส
# Not surprising ถ้าไม่มีโอกาส
# by นายเชาว์วัฒน์ ยาทองชุน
# 21 September 2021, 15:40
#  Specification
#  Input Specification	 Output Specification

# 2 บรรทัด
# คะแนนรวมของทั้งสามคน(???)
# คะแนนสูงสุดของทั้งสามคนนี้

# 1 บรรทัดเท่านั้น "Surprising" หรือ "Not surprising"
#  Sample Case
#  Sample Input	 Sample Output
# 29
# 10
# Not surprising
# 20
# 8
# Surprising