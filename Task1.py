with open('data.json') as f:
	global curr1,curr2,curr1_di,curr2_di
	curr1 = []
	curr1_di = {}
	lst = f.readlines()
	curr_1_str = 'INR'

	start_date = '2019-01-01'
	end_date = '2019-01-31'
	
	for i in range(len(lst)):
		if lst[i].strip()[1:11]<end_date and lst[i].strip()[1:11]>start_date:
			k = lst[i].strip()[1:11]
			while True:
				if lst[i].strip()[1:4] == curr_1_str:
					curr1.append(float(lst[i].strip()[7:-1]))
					curr1_di[k] = float(lst[i].strip()[7:-1])
					break
				i+=1
		else: 
			i+=1

min_curr_1 = min(curr1)
max_curr_1 = max(curr1)
	
start_date_int = int(start_date[:4]+start_date[5:7]+start_date[8:10])
end_date_int = int(end_date[:4]+end_date[5:7]+end_date[8:10])
	
pre = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1280\" height=\"720\">"
suf = "</svg>"
	
data = "<text x=\"70\" y=\"15\" fill=\"red\">"+curr_1_str+"</text>"
data += "<text x=\"70\" y=\"40\" fill=\"blue\">"+"base EUR"+"</text>"
data += "<text x=\"200\" y=\"15\" fill=\"black\"> Start Date :"+start_date+"</text>"
data += "<text x=\"200\" y=\"40\" fill=\"black\"> End Date :"+end_date+"</text>"

curr1_di = {key: value for key, value in sorted(curr1_di.items())}
point_x = 100
for k,v in curr1_di.items():
	k_s = k
	k = int(k[:4]+k[5:7]+k[8:10])
	point_x +=10
	point_y1 = 350 - 150 * (v-min_curr_1)/(max_curr_1-min_curr_1)
	point_y1=int(point_y1)
	data += "<circle cx=\"" + str(point_x) + "\" cy=\"" + str(point_y1) + "\" r=\"2\" fill=\"red\" />"
	data += "<text x=\"" + str(point_x-5) + "\" y=\"400\" fill=\"red\" style=\"font: 12px sans-serif;\" transform=\"rotate(90,"+str(point_x-5)+",400)\">"+k_s+"</text>"
	
data += "<text x=\"10\" y=\"350\" fill=\"red\" style=\"font: 10px sans-serif;\">"+str(min_curr_1)+"</text>"
data += "<text x=\"10\" y=\"200\" fill=\"red\" style=\"font: 10px sans-serif;\">"+str(max_curr_1)+"</text>"

f = open ('win1.svg','w')
f.writelines(pre+data+suf)
