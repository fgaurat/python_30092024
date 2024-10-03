import json
from pprint import pprint

def main_format_string():
    a = 2
    b = 3
    c = a/b
    # f-string
    print(f"{a=}/{b=} = {c:010.3f}")

    s = "b: {1} a: {0}".format(a, b)
    print(s)

    s = "b: {valb} a: {vala}".format(vala=a, valb=b)
    print(s)

    l = [23, 54, 65]
    str_l = ",".join([str(i) for i in l])
    print(str_l)

    s = "{}".format(*l)
    print(s)

    d = {
        "val1": 12,
        "val2": 322,
        "val3": 162,
    }
    s = "{val1},{val2},{val3}".format(**d)

def main_read_write_file():

    # f = open("the_values.txt", 'w')
    # a= 2/0
    # f.close()

    # context manager
    with open("the_values.txt", 'w') as f:
        for i in range(10):
            # f.write(f"Valeur {i+1}\n")
            print(f"Valeur {i+1}", file=f)
    
    # with open("the_values.txt",'r') as f:
    # with open("the_values.txt") as f:
    #     read_data = f.read()
    #     lines = read_data.splitlines()
    #     print(lines)

    # with open("the_values.txt") as f:
    #     lines = f.readlines()
    #     print(lines)

    # with open("the_values.txt") as f:
    #     line = f.readline()
    #     while line:
    #         print(line.strip())
    #         line = f.readline()

    with open("the_values.txt") as f:
        for line in f:
            print(line.strip())

def main_json():
    data = {"employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"}
    ]}
    
    print(data['employees'][1]["lastName"])
    with open ('data.json','w') as json_file :
        json.dump(data,json_file,indent=4)

    with open ('data.json','r') as json_file :
        all_data = json.load(json_file)
        # from pprint import pprint
        pprint(all_data)

def main():
    results = []
    
    with open('MOCK_DATA.csv') as csv_file:
        all_data = [line.strip() for line in csv_file.readlines()]
        header = all_data[0].split(',')

        le_reste = all_data[1:]
        for d in le_reste:
            data = d.split(',')
            r= zip(header,data)
            d = dict(r)
            results.append(d)
    
    print(results)
    with open('data.json','w') as le_json:
        json.dump(results,le_json,indent=4)



        # for line in csv_file:
        #     clean_line = line.strip()
        #     print(clean_line.split(','))

if __name__ == '__main__':
    main()
