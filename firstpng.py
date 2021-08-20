from zlib import compress, crc32


sign = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

IHDRname = b'IHDR'
IHDRdata = b'\x00\x00\x00\x02\x00\x00\x00\x02\x08\x02\x00\x00\x00'
IHDRlen = len(IHDRdata).to_bytes(4, 'big')
IHDRcrc = crc32(IHDRname + IHDRdata).to_bytes(4, 'big')

IHDR = IHDRlen + IHDRname + IHDRdata + IHDRcrc

IDATname = b'IDAT'
IDATdata = compress(b'\x00\x00\xff\xff\xff\x00\xff\x00\xff\x00\xff\x00\xff\xff')
IDATlen = len(IDATdata).to_bytes(4, 'big')
IDATcrc = crc32(IDATname + IDATdata).to_bytes(4, 'big')

IDAT = IDATlen + IDATname + IDATdata + IDATcrc

IENDname = b'IEND'
IENDlen = b'\x00\x00\x00\x00'
IENDcrc = crc32(IENDname).to_bytes(4, 'big')

IEND = IENDlen + IENDname + IENDcrc

with open('first.png', 'wb') as file:
	file.write(sign + IHDR + IDAT + IEND)
