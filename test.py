import regex

output_data = []

with open("input.txt",mode="r",encoding='utf-8') as fr:
     word = list(regex.split(r'(?<=[.])(?!$)',fr.read()))
     output_data += word

line_count = len(output_data)
output_data += [""]#dummy

with open("output.txt",mode="w",encoding='utf-8') as fw:
     for i in range(line_count-1):
          if str.isnumeric(output_data[i+1][0]) or output_data[i+1][0].islower():
               fw.write(str(output_data[i].lstrip().rstrip()))
          elif output_data[i+1][0]=="[":
               fw.write(str(output_data[i].lstrip().rstrip()))
          else:
               fw.write(str(output_data[i].lstrip().rstrip())+'\n')