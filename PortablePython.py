import re
import sys
import os
import getopt
import traceback

code=""
namespace={}
version="1.0"
programname="PortablePython"

def import_replace(obj):
# 定义正则表达式模式，匹配 "from 库名 import 库" 或 "import 库"
	pattern=r'(?<!")((from\s+(\S+)\s+import\s+(\S+))|(import\s+(\S+)))'

# 定义替换函数，根据匹配的情况进行相应的替换
	def replace_func(match):
		full_match=match.group(1)
		from_part=match.group(3)
		module_name=match.group(4)
		import_part=match.group(6)

		if from_part:
			return f'{from_part}=__import__("{from_part}")\nfrom {from_part} import {module_name}'
		elif import_part:
			return f'{import_part}=__import__("{import_part}")'

# 切分代码中的字符串和非字符串部分
	parts=re.split(r'("[^"]*")',obj)

	# 对非字符串部分执行替换操作
	for i in range(len(parts)):
		if not parts[i].startswith('"'):
			parts[i]=re.sub(pattern,replace_func, parts[i])

	# 重新组合代码
	result="".join(parts)
	return result

def embed(c,n):
	code_in=c
	while True:
		embed_code=input("... "+n*"  ")
		if embed_code in (""," "):
			break
		elif embed_code.split(" ")[-1][-1] == ":":
			embed(code_in,n+1)
		else:
			tabs="\t"*n
			code_in+=f"\n{tabs}{embed_code}"
	return code_in

def explain(outputmode="简洁"):
	exec(f"sys=__import__(\"sys\")\nsys.argv={sys.argv[1:]}",namespace)
	while True:
		try:
			code=input(">>> ")
		except:
			break
		if code in ("exit","quit"):
			break
		while code == "clean":
			choice=input("The previous code will be retained, but the screen will be cleared. Are you sure you want to clean it? (yes or no)")
			if choice == "yes":
				os.system("cls")
				print(f"{programname} Version {version}")
				code = input(">>> ")
			else:
				break
		if code == "" or code == " ":
			pass
		elif code.split(" ")[-1][-1] == ":":
			code=embed(code,1)
		for i in namespace.keys():
			if code == i:
				exec(f"print({code})",namespace)
				break
		else:
			code=import_replace(code)    #re.sub("(?<!\")import\\s+(\\w+)","\\1 = __import__(\"\\1\")",code)
			try:
				exec(code,namespace)
			except Exception as e:
				if outputmode == "简洁":
					print(e)
				elif outputmode == "详细":
					traceback.print_exc()
				
def main(args=sys.argv):
	if __name__ == "__main__":
		sys.path.append(os.getcwd())
		opts,args=getopt.getopt(sys.argv[1:],"hvd",["help","version","develop","concise","detailed"])
		for opt,arg in opts:
			if opt in ("-h","--help"):
				print(f"""{programname} User Manual v{version}
  Usage1. Add Python files directly from the command line, just like:
    {programname}.exe "Your Python file"
	  
  Usage2. Directly open the program for interaction, just like:
    {programname}.exe
	  
  Usage3. Use the -d or --develop parameter for development interaction, just like:
    {programname}.exe -d/--develop
  But it is currently under development and cannot be used temporarily. Please be patient and wait
	  
  Usage4. Use the --concise parameter for concise output, it is default output mode, just like:
    {programname}.exe --concise
    >>> var
    NameError: name 'var' is not defined
	  
  Usage5. You also can use the --detailed parameter for detailed output, just like:
    {programname}.exe --detailed
    >>> var
    Traceback (most recent call last):
    File "{programname}.exe", line 80, in explain
      exec(code,namespace)
    File "<string>", line 1, in <module>
    NameError: name 'var' is not defined
	  
  Usage6. Use the -v or --version parameter to view the version, just like:
   v.exe -v/--version
   The version of {programname} is v{version}
	  
  Usage7. Use th -h or --help parameter to view help, just like:
   {programname}.exe -h/--help
				""")
				return 0
			elif opt in ("-v","--version"):
				print(f"The version of {programname} is v{version}")
				return 0
			elif opt in ("-d","--develop"):
				print("It is currently under development and cannot be used temporarily. Please be patient and wait")
				return
				print(f"{programname} Version {version}")
				explain()
				return 0
			elif opt == "--concise":
				explain("简洁")
				return 0
			elif opt == "--detailed":
				explain("详细")
				return 0
			else:
				with open(sys.argv[1],"r") as pyf:
					code=pyf.read()
					code=import_replace(code)
					code=f"sys=__import__(\"sys\")\nsys.argv={sys.argv[1:]}\n\n{code}"
					compile_code=compile(code,filename="<string>",mode="exec")
					exec(compile_code,namespace)
				return 0
		print(f"{programname} Version {version}\nUse -h or --help to view help")
		explain()
		return 0

sys.exit(main())