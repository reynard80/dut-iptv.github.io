from resources.lib.base.language import _

CONST_BASE_URL = 'https://tv.kpn.com'

CONST_BASE_HEADERS = {
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'DNT': '1',
    'AVSSite': 'http://www.itvonline.nl',
    'Accept': '*/*',
    'Origin': CONST_BASE_URL,
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': CONST_BASE_URL + '/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q: 0.9,nl;q: 0.8',
}

CONST_DEFAULT_API = 'https://api.tv.kpn.com/101/1.2.0/A/nld/pctv/kpn'
CONST_IMAGE_URL = 'https://images.tv.kpn.com'

CONST_ONLINE_SEARCH = False

CONST_VOD_CAPABILITY = [
    { 'file': 'series', 'label': _.SERIES, 'start': 0, 'online': 0, 'split': 0 },
    { 'file': 'movies', 'label': _.MOVIES, 'start': 0, 'online': 0, 'split': 0 },
    { 'file': 'kidsseries', 'label': _.KIDS_SERIES, 'start': 0, 'online': 0, 'split': 0 },
    { 'file': 'kidsmovies', 'label': _.KIDS_MOVIES, 'start': 0, 'online': 0, 'split': 0 },
]

CONST_WATCHLIST = False

SETUP_DB_QUERIES = [
    '''CREATE TABLE IF NOT EXISTS `vars` (
        `profile_id` INT(11) PRIMARY KEY,
        `api_url` VARCHAR(255) DEFAULT '',
        `arch` VARCHAR(255) DEFAULT '',
        `browser_name` VARCHAR(255) DEFAULT '',
        `browser_version` VARCHAR(255) DEFAULT '',
        `cookies` TEXT DEFAULT '',
        `devicekey` VARCHAR(255) DEFAULT '',
        `epg_md5` VARCHAR(255) DEFAULT '',
        `epgrun` TINYINT(1) DEFAULT 0,
        `epgruntime` INT(11) DEFAULT 0,
        `first_boot` TINYINT(1) DEFAULT 1,
        `images_md5` VARCHAR(255) DEFAULT '',
        `last_login_success` TINYINT(1) DEFAULT 0,
        `last_login_time` INT(11) DEFAULT 0,
        `last_playing` INT(11) DEFAULT 0,
        `last_tested` VARCHAR(255) DEFAULT '',
        `os_name` VARCHAR(255) DEFAULT '',
        `os_version` VARCHAR(255) DEFAULT '',
        `proxyserver_port` INT(11) DEFAULT 0,
        `pswd` VARCHAR(255) DEFAULT '',
        `search1` VARCHAR(255) DEFAULT '',
        `search2` VARCHAR(255) DEFAULT '',
        `search3` VARCHAR(255) DEFAULT '',
        `search4` VARCHAR(255) DEFAULT '',
        `search5` VARCHAR(255) DEFAULT '',
        `search6` VARCHAR(255) DEFAULT '',
        `search7` VARCHAR(255) DEFAULT '',
        `search8` VARCHAR(255) DEFAULT '',
        `search9` VARCHAR(255) DEFAULT '',
        `search10` VARCHAR(255) DEFAULT '',
        `stream_duration` INT(11) DEFAULT 0,
        `stream_hostname` VARCHAR(255) DEFAULT '',
        `system` VARCHAR(255) DEFAULT '',
        `test_running` TINYINT(1) DEFAULT 0,
        `user_agent` VARCHAR(255) DEFAULT '',
        `username` VARCHAR(255) DEFAULT '',
        `vod_md5` VARCHAR(255) DEFAULT ''
    )''',
]