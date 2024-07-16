from proxyhelper import ProxyMode, ProxyType, ProxyAuthUserPass

GLOBAL_PROXY_MODE = ProxyMode.PROXY_DIRECT
# GLOBAL_PROXY_MODE = ProxyMode.PROXY_ROTATION
# GLOBAL_PROXY_MODE = ProxyMode.PROXY_LIST
GLOBAL_PROXY_TYPE = ProxyType.SOCKS5
# GLOBAL_PROXY_TYPE = ProxyType.HTTP
GLOBAL_PROXY_GET_DELAY = 0 # Delay to get new proxy
GLOBAL_PROXY_USER_PASS_MODE = ProxyAuthUserPass.LAST
# GLOBAL_PROXY_USER_PASS_MODE = ProxyAuthUserPass.LAST
