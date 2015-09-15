#encoding:utf-8
import struct

#axml文件解析
def replace_axml_string(axml_data, old_string, new_string):
    print 'beigin parseAxml'
    '''
    axml_data: the raw bytearray readed from AndroidManifest.xml
    '''
    new_string_pack = axml_utf16_pack(new_string)
    old_string_pack = axml_utf16_pack(old_string)
    new_string_pack_len = len(new_string_pack)
    old_string_pack_len = len(old_string_pack)
    if old_string_pack_len < new_string_pack_len:
        raise ValueError('new_string cannot be larger than old_string! ')
    pos = 0
        
    while True:
        pos = find_pack_in_axml(axml_data, old_string_pack, pos + 1)
        if pos < 0:
            break
        print('find channel at:' + str(pos))
        axml_data[pos : pos + new_string_pack_len] = new_string_pack[ : new_string_pack_len]
        delta = old_string_pack_len - new_string_pack_len
        if delta:
            print('new channel has a different length')
            axml_data[pos + new_string_pack_len: pos + old_string_pack_len] = bytearray(delta)
        else:
            print('new channel has same length as the old')

def axml_utf16_pack(string):
    pack = bytearray(string.encode('utf-16'))
    str_len_pack = struct.pack('<I', len(string))
    pack[ : 2] = struct.unpack('BB', str_len_pack[ : 2])
    return pack

def find_pack_in_axml(axml_data, pack, start):
    pos = axml_data.find(pack, start, -1)
    return pos
