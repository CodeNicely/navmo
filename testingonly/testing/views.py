from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from io import BytesIO
import os
import subprocess

# Create your views here.
# def test(request):

# 	import os
	
# 	from reportlab.lib.pagesizes import A4
# 	from reportlab.lib.units import inch
# 	from reportlab.pdfgen import canvas
# 	buffer = BytesIO()

# 	filename = './i1.png'

# 	#c = canvas.Canvas('imagetest.pdf', pagesize=A4)
# 	c=canvas.Canvas(buffer)
# 	width, height = A4
# 	print"inch",inch
# 	ratio=3
# 	c.drawImage(filename, width-inch*2.5,height-inch*3,width=300/ratio,height=400/ratio) # Who needs consistency?
# 	c.drawString(100, 100, "Hello world.")
# 	c.showPage()
# 	c.save()
# 	pdf = buffer.getvalue()
# 	buffer.close()
    
# 	response = HttpResponse(content_type='application/pdf')
# 	response['Content-Disposition'] = 'attachment; filename="admitcard_navmo.pdf"'
	
# 	response.write(pdf)
# 	return response
def test(request):
	input_txt=""
	code_txt=""
	var=""
	if request.method=="POST":
		handle1=open('code.cpp','w')
		handle1.write(request.POST.get("code"))
		code_txt=request.POST.get("code")
		handle1.close()
		handle2=open('input.txt','w')
		handle2.write(request.POST.get("input"))
		input_txt=request.POST.get("input")
		handle2.close()
		txt1="g++ -o output code.cpp"
		txt2="timeout .002 ./output < input.txt"
		sp1= subprocess.Popen(txt1,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
		p1=sp1.communicate()
		print"p1=",p1
		print "p1 return code=",sp1.returncode
		if(int(sp1.returncode)!=0):
			var="error:"+str(p1[1])
		else:
			sp2= subprocess.Popen(txt2,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
			p2=sp2.communicate()
			print "p2",p2
			print "p2 return code=",sp2.returncode			
			if(int(sp2.returncode)!=0):
				var="runtime error:"+str(p2[1])
			else:
			#	print "p2=",p2.communicate()
				var=str(p2[0])
			#print var
	return render(request,"home.html",{"input":input_txt,"output":var,"code":code_txt})