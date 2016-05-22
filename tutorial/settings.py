# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
DOWNLOAD_DELAY = 0.25

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
HEADER = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'107',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'www.zhihu.com',
    'Pragma':'no-cahce',
    'Referer':'http://www.zhihu.com/',
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
    'X-Requested-With':'XMLHttpRequest',
    'Accep-Encoding':'gzip,deflate',
}
COOKIES={"_ga":r"GA1.2.935939982.1450617254",
        "q_c1":r"6a4c93ab51184adf8d36b544e8b164bf|1463803459000|1463803459000",
        "_za":r"ace8c159-73dd-4811-ac94-3798fbdf519f",
        "__utma":r"51854390.935939982.1450617254.1463875186.1463879047.3",
        "__utmz":r"51854390.1463879047.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
        "udid":r"AEAA2eUKlQmPTuByXgmG7um3FR0hhuuL3qI=|1457502778",
        "d_c0":r"ABCAf4D7oQmPTjlaOoWgB6GVbUvtQva7fz0=|1460986058",
        "_zap":r"40e792c6-a3d7-4ee9-8397-daebe80bebba",
        "_xsrf":r"214421ad2d9da17b8add3bbf1a2ab71f",
        "l_cap_id":r"NWQyYTM3ZDcxMDVmNDE1MjgzZjcxYjUwYjY0OTI3YTY=|1463879046|e7b6628ca1fd30a04a9504177dec9df39857353e",
        "cap_id":r"YWVmZWM3ZjA0YTJjNDRkNzg3YzY1NDI0NjIwZTRiMjE=|1463879046|796bc077a8551ed8ac4bc033fbf6cccf5cdfc11d",\
        "__utmv":r"51854390.100-1|2=registration_date=20130309=1^3=entry_date=20130309=1",
        "login":r"YmUzYzMwNDAxYTFmNGYzNWJjMmZiZmVkYjUyZjA2MTI=|1463879057|2c557b4a1b890541e426223c6da8cea407c4ab41",\
        "l_n_c":r"1",\
        "__utmc":r"51854390",
        "__utmb":r"51854390.4.10.1463879047",
        "z_c0":r"Mi4wQUFCQTNYSWFBQUFBRUlCX2dQdWhDUmNBQUFCaEFsVk5rWkpvVndETm8tdnF3TlhMSERYc21aU1RjblhDRDRrclN3|1463879057|d3063a7d69054c3f039c33203a5a6acff9a919ea"
}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {'tutorial.pipelines.SearchPipeline':300,
#                  'tutorial.pipelines.JsonWritePipeline':500}
#    'tutorial.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
