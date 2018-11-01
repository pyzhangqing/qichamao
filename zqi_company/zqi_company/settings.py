# -*- coding: utf-8 -*-

# Scrapy settings for zqi_company project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'zqi_company'

SPIDER_MODULES = ['zqi_company.spiders']
NEWSPIDER_MODULE = 'zqi_company.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zqi_company (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

def get_user_agent():
    agent = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]
    return random.choice(agent)




# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': get_user_agent(),
    # 'Cookie': 'PSTM=1530925377; BIDUPSID=D16289C7C798A4428D2C0249A8C9C00D; BDUSS=y0walU4WThRcG0wUnFDZVloN0VXWWptR3JWQUotNWljUVBFWGJERW9aQjVFdnBiQVFBQUFBJCQAAAAAAAAAAAEAAACyM4QXenF3d3cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHmF0lt5hdJbM; MCITY=-75%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=291AC074E9842A8F0DA3E5FD648B4E55:FG=1; H_PS_PSSID=26525_1439_21094_27401_26350_20719; BDSFRCVID=664sJeC626Ne6rR7cF3B-hKDbeOD74nTH6aI81l7dj9doHQdqnOlEG0Pff8g0Ku-VcowogKKXgOTHw3P; H_BDCLCKID_SF=tJIHoC-aJKI3fP36q4JohtQH-UnLetJXfbReLPOF5l8-hl0G545GDT-S24Rxe4vi3Ir-aKoVQp7xOKQphUv5D4L4bnolWn3hMNQuB45N3KJms-P9bT3v5tDheh5r2-biWabM2MbdbKOmbCD6ej0KDT3M5fT02-CX5I6X0bbqaJ0_Hn7zePthLntpbtbmhU-eyJALBD3JMDnlER8w5qO8yhDrhHbEaJFJQn7ZVD8bfI-MMKtr5nJbq4kj-fcK2PAXKK_sQl3n-hcqEpO9QTbNQncBjUbEBt7vBNLfaRnKQCOWJlR6DP-VDUThDNAtt6_JJR3fL-082t5VeJIk-PnVeTt_0hbZKxtqte6T366GJC3jJlnnqt7vQ-D8hfbjh4JnWncKWKbXJf3_8I3N248bBpLLQn5405OTWDFO0KJcb66keKnIhPJvypksXnO7-5JTfJAO_CKhJIK3fP36q46hhtLtqxby26nO3D3eaJ5nJDoCqfJebJDb-UK1Mec3BM3a3nRCWK5lQpP-HJAlLluB34CHMfQN0fRtbmjvKl0MLpctbb0xyn_Vy43bbxnMBMnv52OnaP0bLIFaMIIRj5_beP0W2mT22jnM0JneaJ5n0-nnhUcs34Cb-UKzbU7IBx5EyJ59L6675Uo8q4_Ry6C5e5Q0DH8tqbbfb-oBLR6H26rjDnCrD45MKUI8LNDHQJoT3ITq_bOI2K8Vjhve-x82LtR00JO7ttoytmrkVxQ8aJTHVlQO5JoYWML1Db3ZKjvMtg3tslcefnQoepvoW-Jc3MkWDn0EJ6DeJbIO_IvaaJToD66nh-rjMICqb2T22-usJJFJQhcH0KLKMlrNjR5CjPtzDPKLaUnRKDT9KI02afb1MRjVe5QSjP0qefOyBpob-Co9Wp5TtUJteCnTDMRhqqKShpJyKMniyIv9-pn5tMt0HPonHj8KDT333e; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=3',
    # 'referer': 'www.85781.com',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zqi_company.middlewares.ZqiCompanySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zqi_company.middlewares.ZqiCompanyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zqi_company.pipelines.ZqiCompanyPipeline': 300,
   'zqi_company.pipelines.MysqlPipeline': 310,
   # 'zqi_company.pipelines.MongoPipeline': 320,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FEED_EXPORT_ENCODING = 'utf-8'


MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'companys'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306



# SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# # 去重
# DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# REDIS_URL = 'redis://@10.7.154.54:6379'



MONGO_URI = 'mongodb://10.7.154.54:27017'
MONGO_DB = 'zq'
