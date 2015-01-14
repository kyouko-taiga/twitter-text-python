import re


# Some of this code has been translated from the twitter-text-java library:
# <http://github.com/mzsanford/twitter-text-java>
AT_SIGNS = r'[@\uff20]'
UTF_CHARS = r'a-z0-9_\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff'
SPACES = r'[\u0020\u00A0\u1680\u180E\u2002-\u202F\u205F\u2060\u3000]'

# Lists
LIST_PRE_CHARS = r'([^a-z0-9_]|^)'
LIST_END_CHARS = r'([a-z0-9_]{1,20})(/[a-z][a-z0-9\x80-\xFF-]{0,79})?'
LIST_REGEX = re.compile(LIST_PRE_CHARS + '(' + AT_SIGNS + '+)' + LIST_END_CHARS,
                        re.IGNORECASE)

# Users
USERNAME_REGEX = re.compile(r'\B' + AT_SIGNS + LIST_END_CHARS, re.IGNORECASE)
REPLY_REGEX = re.compile(r'^(?:' + SPACES + r')*' + AT_SIGNS
                         + r'([a-z0-9_]{1,20}).*', re.IGNORECASE)

# Hashtags
HASHTAG_EXP = r'(^|[^0-9A-Z&/]+)(#|\uff03)([0-9A-Z_]*[A-Z_]+[%s]*)' % UTF_CHARS
HASHTAG_REGEX = re.compile(HASHTAG_EXP, re.IGNORECASE)

# URLs
PRE_CHARS = r'(?:[^/"\':!=]|^|\:)'
DOMAIN_CHARS = r'([\.-]|[^\s_\!\.\/])+\.[a-z]{2,}(?::[0-9]+)?'
PATH_CHARS = r'(?:[\.,]?[%s!\*\'\(\);:=\+\$/%s#\[\]\-_,~@])' % (UTF_CHARS, '%')
QUERY_CHARS = r'[a-z0-9!\*\'\(\);:&=\+\$/%#\[\]\-_\.,~]'

# Valid end-of-path chracters (so /foo. does not gobble the period).
# 1. Allow ) for Wikipedia URLs.
# 2. Allow =&# for empty URL parameters and other URL-join artifacts
PATH_ENDING_CHARS = r'[%s\)=#/]' % UTF_CHARS
QUERY_ENDING_CHARS = '[a-z0-9_&=#]'

URL_REGEX = re.compile('((%s)((https?://|www\\.)(%s)(\/(%s*%s)?)?(\?%s*%s)?))'
                       % (PRE_CHARS, DOMAIN_CHARS, PATH_CHARS,
                          PATH_ENDING_CHARS, QUERY_CHARS, QUERY_ENDING_CHARS),
                       re.IGNORECASE)
