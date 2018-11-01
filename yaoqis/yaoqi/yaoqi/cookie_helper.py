class TransCookie:
  def __init__(self, cookie):
     self.cookie = cookie

  def stringToDict(self):

     itemDict = {}
     items = self.cookie.split(';')
     for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        itemDict[key] = value
     return itemDict

if __name__ == "__main__":
  cookie = "comic_order=asc; CNZZDATA30031742=cnzz_eid%3D1952822585-1536887064-null%26ntime%3D1537427080; CNZZDATA30088157=cnzz_eid%3D1564721445-1536887450-null%26ntime%3D1537425816; _cnzz_CV30031742=%E7%94%A8%E6%88%B7%E7%B1%BB%E5%9E%8B%7C%E6%B8%B8%E5%AE%A2%7C1537431210346; chapter_record_ids=793554; register_guide_five=1; register_guide_four=1; register_guide_one=1; register_guide_three=1; register_guide_two=1; bdshare_firstime=1537430856091; index_mobile_do_ad=1; Hm_lpvt_9aa72b7e4e92f182872acd1c8031f141=1537431210; Hm_lvt_9aa72b7e4e92f182872acd1c8031f141=1536891837,1536891911,1536892168,1537430778; xxlastcomic=%5B%5B%2298416%22%2C%22%E8%82%96%E8%8A%B1%E9%95%87%22%2C%22793553%22%2C%2201%20%E5%BE%81%E5%85%86%22%5D%5D; xxreadmode=; xxsetting=%7B%22tucao%22%3A%221%22%7D; U17SID=pfcah6hb62u4ybk61lx97z36qhs7h2u8; UM_distinctid=165d5e431cd93-07ef11ea1031ae-49183706-fa000-165d5e431ce41e"
  trans = TransCookie(cookie)
  print(trans.stringToDict())