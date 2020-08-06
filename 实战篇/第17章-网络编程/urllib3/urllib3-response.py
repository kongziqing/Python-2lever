"""
urllib3是Python提供的一个用于发送URL请求的官方标准库，利用urllib3可以模拟浏览器请求访问，
向服务器发送请求的同时，也可以进行头部信息的传递

本程序直接利用urllib3模块中的PoolManager类构造了一个请求对象，随后利用urlopen（）向指定的路径发出了一个GET请求，当服务器端
成功接收到请求后可以直接获取响应的头部信息与数据信息
"""
import urllib3 #模块导入
YOOTK_URL = "http://www.yootk.com/video/3"   #请求的服务器地址
def main():  #主函数
    request_headers = {'User-Agent':'Yootk Python'}  #请求头部信息
    #PoolManager实现请求的发送，实例化对象时可以设置缓冲区的大小以及请求所需要携带的头部信息
    http = urllib3.PoolManager(num_pools=5,headers=request_headers)
    response = http.urlopen("GET",YOOTK_URL)  #发送GET请求
    print(response.headers)  #获取响应头部信息
    print(response.data.decode("UTF-8"))   #获取响应的HTML数据
if __name__ == '__main__':
    main()