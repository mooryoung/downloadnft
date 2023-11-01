import os
import requests
import hashlib
import json


# 【地址方式】#########################################################################################
# 下载图片并，获取url图片的sha256 hash值
def down_img_by_url(name='punk', number='0000', img_type='png', url='https://cryptopunks.app/public/images/cryptopunks/', isreturnhash=False):
    try:
        filename = name + number + '.' + img_type
        r = requests.get(url + filename, allow_redirects=True, stream=True)
        if os.path.exists(name) == False: os.makedirs(name)
        with open(f'./{name}/{name}{number}.{img_type}', 'wb') as f:
            f.write(r.content)
        if isreturnhash:
            sha256obj = hashlib.sha256(r.content)
            myhash = sha256obj.hexdigest()
            # print(myhash)
            return myhash
    except Exception as e:
        # print(e.args)
        pass


# 获取文件并保存
def get_all_punk_imgs():
    try:
        for i in range(10000):
            myhash = down_img_by_url('punk', str(i).zfill(4), 'png', url='https://cryptopunks.app/public/images/cryptopunks/')
            print('punk' + str(i) + '.png', myhash)
    except Exception as e:
        print(e.args)
        

# 【IPFS方式】#########################################################################################
# 【ipfs方式】下载图片并，获取url图片的sha256 hash值
def down_img_by_ipfs(name='bayc', number='0', img_type='png', url='http://127.0.0.1:8080/ipfs/-----cid-----', isreturnhash=False):
    try:
        filename = name + number + '.' + img_type
        r = requests.get(url, allow_redirects=True, stream=True)
        if os.path.exists(name) == False: os.makedirs(name)
        with open(f'./{name}/{name}{number}.{img_type}', 'wb') as f:
            f.write(r.content)
        if isreturnhash:
            sha256obj = hashlib.sha256(r.content)
            myhash = sha256obj.hexdigest()
            # print(myhash)
            return myhash
    except Exception as e:
        # print(e.args)
        pass


# 【ipfs方式】获取bayc的json
def get_bayc_json(id):
    # base_url = "http://127.0.0.1:8080/ipfs/QmZcH4YvBVVRJtdn4RdbaqgspFU8gH6P9vomDpBVpAL3u4/"#AZUKI
    base_url = "http://127.0.0.1:8080/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/"  # bayc
    try:
        r = requests.get(base_url + str(id), )
        if r.status_code == 200:
            myjson = json.loads(r.content)

            return myjson
    except Exception as e:
        # print(e.args)
        pass


# 【ipfs方式】获取文件并保存
def get_all_bayc_imgs():
    try:
        for i in range(10000):
            cid = get_bayc_json(i)['image'][7:]
            myhash = down_img_by_ipfs('bayc', str(i), 'png', url=f'http://127.0.0.1:8080/ipfs/{cid}/')
            print('bayc' + str(i) + '.png', myhash)
    except Exception as e:
        print(e.args)


# 【下载azuki】#########################################################################################
# 下载某个azuki的图片
def down_img_azuki(dir='azuki', number='0', img_type='png', url='http://127.0.0.1:8080/ipfs/QmYDvPAXtiJg7s8JdRBSLWdgSphQdac8j1YuQNNxcGE1hg/', isreturnhash=False):
    try:
        filename = number + '.' + img_type
        r = requests.get(url+filename, allow_redirects=True, stream=True)
        if os.path.exists(dir) == False: os.makedirs(dir)
        with open(f'./{dir}/{dir}{number}.{img_type}', 'wb') as f:
            f.write(r.content)
        if isreturnhash:
            sha256obj = hashlib.sha256(r.content)
            myhash = sha256obj.hexdigest()
            # print(myhash)
            return myhash
    except Exception as e:
        # print(e.args)
        pass


# 获取所有azuki的图片
def get_all_azuki_imgs():
    base_url = "http://127.0.0.1:8080/ipfs/QmYDvPAXtiJg7s8JdRBSLWdgSphQdac8j1YuQNNxcGE1hg/"   #AZUKI
    try:
        for i in range(10000):
            myhash = down_img_azuki('azuki', str(i), 'png', url=base_url)
            print('azuki' + str(i) + '.png', myhash)
    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    get_all_punk_imgs()
    get_all_bayc_imgs()
    get_all_azuki_imgs()
    pass
