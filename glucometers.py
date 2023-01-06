def read_file(file_name):
    datas=[]
    try:
        with open(file_name,"r") as in_file:
            for element in in_file:
                element.strip()
                my_list=element.split()
                list1=[]
                i=0
                for elements in my_list:
                    if i==0:
                        list1.append(str(elements))
                    elif i==2 or i==4:
                        list1.append(int(elements))
                    elif i==3:
                        list1.append(float(elements))
                    else:
                        list1.append(elements)
                    i+=1
                datas.append(list1)
            return datas
    except IOError:
        print("not exist")

def calculator(data_reader):
    overs=[]
    for line in data_reader:
        if line[2]>=200:
            overs.append(line)
        else:
            pass
    return overs

def main():
    data_reader=read_file("glucometers.txt")
    ali=calculator(data_reader)
    sorted_ali=sorted(ali)
    for eleman in range(len(sorted_ali)):
        print(sorted_ali[eleman][0],"",sorted_ali[eleman][1],"",sorted_ali[eleman][2])
main()
