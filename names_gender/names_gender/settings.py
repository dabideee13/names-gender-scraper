BOT_NAME = 'names_gender'

SPIDER_MODULES = ['names_gender.spiders']
NEWSPIDER_MODULE = 'names_gender.spiders'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
AUTOTHROTTLE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

HTTPCACHE_ENABLED = True
