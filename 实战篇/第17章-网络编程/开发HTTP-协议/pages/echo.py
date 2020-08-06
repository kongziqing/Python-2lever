def service(param):  #服务处理函数
    """
    实现动态web请求处理，本程序返回的内容为最终HTML显示内容，service（）为自定义方法名称
    :param param: 要处理的参数内容
    :return: 如果有参数，传递则处理，如果没有参数传递，则直接返回NOPARAM信息
    """
    if param:
        return "<h1>" +param+"</h1>"  #HTML数据
    else:
        return "<h1>NOPARAM</h1>"