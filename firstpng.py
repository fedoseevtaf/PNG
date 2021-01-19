filename = 'firstpng.png'

import zlib

with open(filename, 'wb') as file:
    signature = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

    IHDRname = b'IHDR'
    IHDRdata = b'\x00\x00\x00\x02\x00\x00\x00\x02\x08\x02\x00\x00\x00'
    IHDRlen = len(IHDRdata).to_bytes(4, 'big')
    IHDRcrc = zlib.crc32(IHDRname + IHDRdata).to_bytes(4, 'big')
    IHDR = IHDRlen + IHDRname + IHDRdata + IHDRcrc

    IDATname = b'IDAT'
    IDATdata = zlib.compress(b'\x00\xdd\x88\xdd\x44\xff\xff\x00\x44\xff\xff\xdd\x88\xdd')
    IDATlen = len(IDATdata).to_bytes(4, 'big')
    IDATcrc = zlib.crc32(IDATname + IDATdata).to_bytes(4, 'big')
    IDAT = IDATlen + IDATname + IDATdata + IDATcrc

    IENDname = b'IEND'
    IENDlen = b'\x00\x00\x00\x00'
    IENDcrc = zlib.crc32(IENDname).to_bytes(4, 'big')
    IEND = IENDlen + IENDname + IENDcrc

    bytecode = signature + IHDR + IDAT + IEND

    file.write(bytecode)
    
