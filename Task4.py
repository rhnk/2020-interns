import requests

start_date = '2019-01-01'
end_date = '2019-01-31'

url='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols=INR,GBP'.format(start_date,end_date)

response = requests.get(url)
f = response.text
f = f.replace('{','{\n')
f = f.replace(',',',\n')
f = f.replace('}},','\n}},')
f = f.replace('},','\n},')

curr1 = []
curr2 = []
curr1_di = {}
curr2_di = {}
lst = [i for i in f.split('\n')]

curr_1_str = 'INR'
curr_2_str = 'GBP'

for i in range(2,len(lst)-4,4):
	d = lst[i][1:11]
	i += 1
	curr1_di[d] = float(lst[i][6:-1])
	curr1.append(float(lst[i][6:-1]))
	i += 1
	curr2_di[d] = float(lst[i][6:])
	curr2.append(float(lst[i][6:]))
	
min_curr_1 = min(curr1)
max_curr_1 = max(curr1)
min_curr_2 = min(curr2)
max_curr_2 = max(curr2)

start_date_int = int(start_date[:4]+start_date[5:7]+start_date[8:10])
end_date_int = int(end_date[:4]+end_date[5:7]+end_date[8:10])
	
pre = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1280\" height=\"720\">"
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

data += "<text x=\"400\" y=\"15\" fill=\"black\" > Base currency EUR </text>"	
f = open ('win4.svg','w')
f.writelines(pre+data+suf)
