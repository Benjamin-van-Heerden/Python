import base64

MESSAGE = '''
GUIdHwIODB0FTxEDGRAFFwsLFUpFTlELXlVVUgMCGw9GTVNOUQ1CTVxSDwAKTU1NTgsQDl5LTURF 
RVRKRgQHDQQNVVBbWwdCQkpGDAoGHw1HXFRSDBFJSltNThsYBF5aUlIGQkJKRh8IDBQBRUoeF1hF 
SRkACwxJWkgWX1ZYRUVUSkYaAABXT0w=
'''

KEY = 'benjaminvh1997'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result) #{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}