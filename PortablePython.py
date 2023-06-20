import sys
import os
import getopt
import traceback
import json
import locale

version="1.0.2-alpha"
programname="PortablePython"

language={
	"en":{
		"DisplayVersion":f"The version of {programname} is v{version}",
		"BeforeCleanTip":"Previously running code will not be cleared, but the terminal will be cleared and the previous code cannot be viewed. Are you sure you want to empty it? (yes or no)>> ",
		"UserManual":f"""{programname} User Manual v{version}
  Usage1. Add Python files directly from the command line, For example:
    {programname}.exe "Your Python file"
	  
  Usage2. Directly open the program for interaction, For example:
    {programname}.exe
	  
  Usage3. Use the -d or --develop parameter for development interaction, For example:
    {programname}.exe -d/--develop
  But it is currently under development and cannot be used temporarily. Please be patient and wait
	  
  Usage4. Use the --concise parameter for concise output, it is default output mode, For example:
    {programname}.exe --concise
    >>> var
    NameError: name 'var' is not defined
	  
  Usage5. You also can use the --detailed parameter for detailed output, For example:
    {programname}.exe --detailed
    >>> var
    Traceback (most recent call last):
    File "{programname}.exe", line 80, in explain
      exec(code,namespace)
    File "<string>", line 1, in <module>
    NameError: name 'var' is not defined
    
  Usage6. Use the -p or --path parameter to change work path, For example:
    {programname}.exe -p/--path "WorkPath"
    {programname} Version {version}
    Use -h or --help to view help  Current work path: "WorkPath"

  Usage7. Use the -l or --language to change language to other language, For example:
    {programname}.exe -v -l/--language cn
    {programname}现在的版本是v{version}。
  Default language is English.
  
  You can also create a '.lang' file yourself in the current directory
  (the name can be chosen arbitrarily, just enter the file name when using it),
  and the content should be like:
  {{
    "BeforeCleanTip":"...",
    "UserManual":"...",
    "DiplayVersion":"...",
    "DevelopTip":"...",
    "Prompt":"...",
    "OutputComplexity":{{
      "Concise":"...",
      "Detailed":"..."
    }},
    "Word":{{
      "Version":"..."
    }}
  }}
	
	You can use {{programname}} to get porgram name, use {{version}} to get version.

	Usage9. Use the -s or --save parameter to save as a file after exit, For example:
		{programname}.exe -s/--save
		>>> print("Hello World")
		>>> exit
		Your Python File name>> HelloWorld.py

  Usage10. Use the -v or --version parameter to view the version, For example:
    {programname}.exe -v/--version
    The version of {programname} is v{version} now.
	  
  Usage11. Use the -h or --help parameter to view help, For example:
    {programname}.exe -h/--help
				""",
		"DevelopTip":"It is currently under development and cannot be used temporarily. Please be patient and wait",
		"Prompt":f"{programname} Version {version}\nUse -h or --help to view help  Current work path: \"{os.getcwd()}\"\nSave as Python File: ",
		"CurrentPath":f"Current work path: ",
		"Yes":"Yes",
		"No":"No",
		"OutputComplexity":{
			"Concise":"Error Mode: concise.",
			"Detailed":"Error Mode: detaile."
		},
		"Word":{
			"Version":"Version"
		}
	},
	"cn":{
		"DiplayVersion":f"{programname}现在的版本是v{version}",
		"BeforeCleanTip":"之前运行过的代码不会清除，但终端将会清空，且无法查看之前的代码。你确定要清空吗？（yes或no）>> ",
		"UserManual":f"""{programname} 使用手册 v{version}
  用法1. 直接在命令行添加Python文件，例如：
    {programname}.exe "Python文件"
	  
  用法2. 直接打开软件进行交互，例如：
    {programname}.exe
	  
  用法3. 在命令行使用-d或--develop参数打开开发者模式，例如：
    {programname}.exe -d/--develop
  但它现在还在开发中，敬请期待……
	  
  用法4. 在命令行使用--concise参数设置输出简洁的报错，它是默认的输出模式，例如：
    {programname}.exe --concise
    >>> var
    NameError: name 'var' is not defined
	  
  用法5. 同样可以在命令行使用--detailed参数输出详细的报错，例如：
    {programname}.exe --detailed
    >>> var
    Traceback (most recent call last):
    File "{programname}.exe", line 80, in explain
      exec(code,namespace)
    File "<string>", line 1, in <module>
    NameError: name 'var' is not defined
    
  用法6. 在命令行使用-p或--path参数更改工作路径，例如：
    {programname}.exe -p/--path "工作路径"
    {programname} Version {version}
  使用-h或--help获取帮助  当前工作路径："工作路径"

  用法7. 在命令行使用-l或--language参数更改语言，例如：
    {programname}.exe -v -l/--language en
    The version of {programname} is v{version} now.
  Default language is English.
  
  你也可以自己在当前目录下创建一个.lang文件
  （名字可以随便取，使用时输入文件名就行了），
  内容应该像是：
  {{
    "BeforeCleanTip":"...",
    "UserManual":"...",
    "DiplayVersion":"...",
    "DevelopTip":"...",
    "Prompt":"...",
    "OutputComplexity":{{
      "Concise":"...",
      "Detailed":"..."
    }},
    "Word":{{
      "Version":"..."
    }}
  }}
	
	你可以使用{{programname}}获取程序名,{{version}}获取版本号

	用法9. 退出后使用-s或--save参数另存为文件，例如：
    {programname}.exe -s/--save
    >>> print("Hello World")
    >>> exit
    保存为>> HelloWorld.py

  用法9. 在命令行使用-v或--version参数获取{programname}的版本，例如：
    {programname}.exe -v/--version
    {programname}现在的版本是v{version}。
	  
  Usage10. 在命令行使用-h或--help参数获取帮助，例如：
    {programname}.exe -h/--help
				""",
		"DevelopTip":"它目前正在开发中，暂时无法使用。敬请期待……",
		"Prompt":f"{programname} Version {version}\n使用-h或--help获取帮助  当前工作路径：\"{os.getcwd()}\"\n是否保存为Python文件：",
		"CurrentPath":"当前工作路径：",
		"Yes":"是",
		"No":"否",
		"OutputComplexity":{
			"Concise":"报错模式：简洁。",
			"Detailed":"报错模式：详细。"
		},
		"Word":{
			"Version":"版本"
		}
	}
}

language_type=locale.getdefaultlocale()[1]
if language_type == "en_US":
	lang=language["en"]
elif language_type == "zh_CN":
	lang=language["cn"]

code=""
namespace={}
savecode=False
allcode=""
currentPath=os.getcwd()

def embed(c,n):
	code_in=c
	tabs="\t"*n
	while True:
		embed_code=input("... "+n*"  ")
		if embed_code in (""," "):
			break
		elif embed_code.strip()[-1:] == ":":
			code_in+=f"\n{tabs}"
			code_in+=embed(c,n+1)
		else:
			code_in+=f"\n{tabs}{embed_code}"
	return code_in

def explain(outputmode="concise"): 
	global allcode
	global savecode
	global currentPath

	print(lang["Prompt"],end="")
	print(lang[str(savecode)],end="  ")
	print(lang["OutputComplexity"][outputmode.title()])
	exec(f"import sys\nsys.argv={sys.argv[1:]}",namespace)
	while True:
		try:
			code=input(">>> ")
		except:
			if savecode:
				with open(input("Your Python File name>> "),"w",encoding="utf-8") as f:
					f.write(allcode)
			break
		if code in ("exit","quit"):
			with open(input("Your Python File name>> "),"w",encoding="utf-8") as f:
				f.write(allcode)
			break
		while code == "clean":
			choice=input(lang["BeforeCleanTip"])
			if choice == "yes":
				os.system("cls")
				print("{} {} {}".format(programname,lang["Word"]["Version"],version))
				code = input(">>> ")
			else:
				break
		if code == "" or code == " ":
			pass
		if code.split(" ")[-1][-1] == ":":
			code=embed(code,1)
		for i in namespace.keys():
			if code == i:
				print(namespace[i])
				break
		else:
			try:
				compile_code=compile(code,filename="<stdin>",mode="exec")
				exec(compile_code,namespace)
				allcode=allcode+code
				if not os.getcwd() == currentPath:
					print(lang["CurrentPath"]+f"\"{os.getcwd()}\"") 
					currentPath=os.getcwd()
			except Exception as e:
				if outputmode == "concise":
					print(e)
				elif outputmode == "detailed":
					traceback.print_exc()

def main(args=sys.argv):
	if __name__ == "__main__":
		global lang,savecode

		sys.path.append(os.getcwd())
		try:
			opts,args=getopt.getopt(sys.argv[1:],"hvdp:l:s",["help","version","develop","concise","detailed","path=","language=","save"])
		except getopt.GetoptError as ge:
			e=str(ge).split()[1]
			if e in ("-p","--path"):
				print(f"\033[31mError:\033[0m\033[33mYou should add a path after the {e} parameter!\033[0m")
				return 0
			elif e in ("-l","--language"):
				print(f"\033[31mError:\033[0m\033[33mYou should add a language type after the {e} parameter!\033[0m")
				return 0
			else:
				#print(e)
				print("Invalid arguments. Use -h or --help for usage.")
				return 0
			
		for opt,arg in opts:
			for i in opts:
				if i[0] in ("-l","--language"):
					try:
						lang=language[i[1]]
					except KeyError:
						try:
							with open(i[1]+".lang","r") as langf:
								cont=json.loads(langf.read())
							lang["BeforeCleanTip"]=cont["BeforeCleanTip"].format(programname=programname,version=version)
							lang["BeforeCleanTip"]=cont["DiplayVersion"].format(programname=programname,version=version)
							lang["BeforeCleanTip"]=cont["UserManual"].format(programname=programname,version=version)
							lang["BeforeCleanTip"]=cont["DevelopTip"].format(programname=programname,version=version)
							lang["BeforeCleanTip"]=cont["Prompt"].format(programname=programname,version=version)
							lang["BeforeCleanTip"]=cont["OutputComplexity"]["Concise"].format(programname=programname,version=version)
							lang["BeforeCleanTip"]=cont["OutputComplexity"]["Detailed"].format(programname=programname,version=version)
							lang["BeforeCleanTip"]=cont["Word"]["Version"].format(programname=programname,version=version)
						except KeyError:
							print("\033[31mError:\033[0m\033[33mIncorrect file format!\033[0m")
						except FileNotFoundError:
							print(f"\033[33mSorry, we currently do not support the language.'{arg}'\033[0m")
							return 0
						except:
							print(f"\033[33mSorry, there was an error.'{arg}'\033[0m")
							return 0
				if i[0] in ("-s","--save"):
					savecode=True
			if opt in ("-h","--help"):
				print(lang["UserManual"],end="")
				return 0
			elif opt in ("-v","--version"):
				print(lang["DisplayVersion"])
				return 0
			elif opt in ("-d","--develop"):
				print(lang["DevelopTip"])
				return 0
				print(lang["DisplayVersion"])
				explain()
				return 0
			elif opt == "--concise":
				explain("concise")
				return 0
			elif opt == "--detailed":
				explain("detailed")
				return 0
			elif opt in ("-p","--path"):
				try:
					os.chdir(arg)
				except FileNotFoundError:
					print("The path must be a valid path!")
					return 0
				currentPath=arg
		else:
			explain()
			return 0
	try:
		with open(sys.argv[1],"r") as pyf:
			code=pyf.read()
			code=f"import sys\nsys.argv={sys.argv[1:]}\n\n{code}"
			compile_code=compile(code,filename=sys.argv[1],mode="exec")
			exec(compile_code,namespace)
		return 0
	except IndexError:
		lang=language["en"]
		explain()
		return 0

#sys.exit(main())