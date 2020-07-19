with open('data.json') as f:
	global curr1,curr2,curr1_di,curr2_di
	curr1 = []
	curr2 = []
	curr1_di = {}
	curr2_di = {}
	lst = f.readlines()
	curr_1_str = 'INR'
	curr_2_str = 'GBP'
	
	start_date = '2019-01-01'
	end_date = '2019-01-31'
	
	for i in range(len(lst)):
		if lst[i].strip()[1:11]<end_date and lst[i].strip()[1:11]>start_date:
			f1=False
			f2=False 
			k = lst[i].strip()[1:11]
			while True:
				if lst[i].strip()[1:4] == curr_1_str:
					curr1.append(float(lst[i].strip()[7:-1]))
					curr1_di[k] = float(lst[i].strip()[7:-1])
					f1 = True
				elif not f2 and lst[i].strip()[1:4] == curr_2_str:
					curr2.append(float(lst[i].strip()[7:-1]))
					curr2_di[k] = float(lst[i].strip()[7:-1])
					f2 = True
				if f1 and f2:
					break
				i+=1
		else: 
			i+=1

min_curr_1 = min(curr1)
max_curr_1 = max(curr1)
min_curr_2 = min(curr2)
max_curr_2 = max(curr2)
	
start_date_int = int(start_date[:4]+start_date[5:7]+start_date[8:10])
end_date_int = int(end_date[:4]+end_date[5:7]+end_date[8:10])
	
pre = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1920\" height=\"1080\">"
suf = "</svg>"
	
data = "<text x=\"70\" y=\"15\" fill=\"red\">"+curr_1_str+"</text>"
data += "<text x=\"70\" y=\"40\" fill=\"blue\">"+curr_2_str+"</text>"
data += "<text x=\"120\" y=\"15\" fill=\"black\"> Start Date :"+start_date+"</text>"
data += "<text x=\"120\" y=\"40\" fill=\"black\"> End Date :"+end_date+"</text>"

curr1_di = {key: value for key, value in sorted(curr1_di.items())}
curr2_di = {key: value for key, value in sorted(curr2_di.items())}
point_x = 100
for k,v in curr1_di.items():
	k_s = k
	k = int(k[:4]+k[5:7]+k[8:10])
	point_x +=10
	point_y1 = 350 - 150 * (v-min_curr_1)/(max_curr_1-min_curr_1)
	point_y1=int(point_y1)
	data += "<circle cx=\"" + str(point_x) + "\" cy=\"" + str(point_y1) + "\" r=\"2\" fill=\"red\" />"
	data += "<text x=\"" + str(point_x-5) + "\" y=\"400\" fill=\"red\" style=\"font: 10px sans-serif;\" transform=\"rotate(90,"+str(point_x-5)+",400)\">"+k_s+"</text>"
	
point_x = 100
for k,v in curr2_di.items():
	k_s = k
	k = int(k[:4]+k[5:7]+k[8:10])
	point_x +=10
	point_y1 = 350 - 150 * (v-min_curr_2)/(max_curr_2-min_curr_2)
	point_y1=int(point_y1)
	data += "<circle cx=\"" + str(point_x) + "\" cy=\"" + str(point_y1) + "\" r=\"2\" fill=\"blue\" />"
	data += "<text x=\"" + str(point_x-5) + "\" y=\"50\" fill=\"blue\"  style=\"font: 10px sans-serif;\" transform=\"rotate(90,"+str(point_x-5)+",50)\">"+k_s+"</text>"
	
data += "<text x=\"10\" y=\"350\" fill=\"red\" style=\"font: 10px sans-serif;\">"+str(min_curr_1)+"</text>"
data += "<text x=\"10\" y=\"200\" fill=\"red\" style=\"font: 10px sans-serif;\">"+str(max_curr_1)+"</text>"
data += "<text x=\""+str(len(curr1)*10+150)+"\" y=\"350\" fill=\"blue\" style=\"font: 10px sans-serif;\">"+str(min_curr_2)+"</text>"
data += "<text x=\""+str(len(curr1)*10+150)+"\" y=\"200\" fill=\"blue\" style=\"font: 10px sans-serif;\">"+str(max_curr_2)+"</text>"
data += "<text x=\"700\" y=\"15\" fill=\"black\" > Base currency EUR </text>"	
f = open ('latest-rates.json')
latest = f.readlines()
for i in latest:
	if i.strip()[1:4] == "INR":
		data += "<text x=\"350\" y=\"15\" fill=\"black\">Current INR rate :"+i.strip()[7:-1]+"</text>"
	elif i.strip()[1:4] == "GBP":
		data += "<text x=\"350\" y=\"40\" fill=\"black\">Current GBP rate :"+i.strip()[7:-1]+"</text>"
		
f.close()
f = open ('win3.svg','w')
f.writelines(pre+data+suf)
f.close()
