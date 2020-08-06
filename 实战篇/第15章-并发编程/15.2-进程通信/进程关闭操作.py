"""
在使用subprocess.Popen创建进程时也可以直接获取当前的进程对象，随后就可以利用subprocess模块中
提供的kill()方法杀死进程
本程序启动了windows系统中的chrome.exe,并获得了一个进程对象，延迟3秒后实现了对指定进程的自动关闭
"""
import subprocess, time				# 模块导入
def main():					# 主函数
    notepad_process = subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")	# 启动进程
    time.sleep(3) 					# 让该进程运行3秒时间
    notepad_process.kill()				# 关闭进程
if __name__ == "__main__":				# 判断程序执行名称
    main()
