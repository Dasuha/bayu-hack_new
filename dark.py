# Compile by Bayu Dasuha
# Created by DASUHA (https://github.com/Dasuha)
# Instagram : @dasuha.5656

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))