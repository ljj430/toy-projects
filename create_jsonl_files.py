import jsonlines
import pandas as pd
path = r'F:\SOEN_691\extracted_results\with_docstring_results_full.jsonl'
save_path = r'F:\SOEN_691\extracted_results\with_docstring_results_full_{}.jsonl'

#remove __intit__


# with jsonlines.open(path) as reader:
#     count = 1
#     iter_count = 0
#     for obj in reader:
#         save_list.append(obj)
#         if count%10000 == 0:
#             iter_count +=1
#             ##write
#             with jsonlines.open(save_path.format(iter_count),mode='w') as writer:
#                 for line in save_list:
#                     jsonlines.Writer.write(writer,line)
#             save_list = []
#         count +=1

path1= r'F:\SOEN_691\extracted_results\with_docstring_results_full_1.jsonl'
path2= r'F:\SOEN_691\extracted_results\with_docstring_results_full_2.jsonl'
path3= r"F:\SOEN_691\extracted_results\output4.jsonl"
path4 = r"F:\SOEN_691\extracted_results\output3.jsonl"
path1_list = [9,11,16,18,84,153,207,242,268,315,
              317,323,324,343,344,345,347,349,350,352,
              353,354,370,379,381,386,400,435,463,479,
              480,485,486,548,556,621,634,636,639,641,
              662,673,717,719,724,795,904,918,994,1030
              ]
path2_list = [64,68,73,74,76,98,152,276,296,305,
              319,337,342,380,381,388,420,512,580,593,
              594,765,819,876,878,880,881,894,932,983,
              1334,1404,1415,1416,1440,1446,1478,1480,1515,1572,
              1573,1579,1594,1613,1615,2167,2185,5338,5339,5359]
def sample_process():
    save_list = []
    save_path = r"F:\SOEN_691\extracted_results\selected_methods.jsonl"
    with jsonlines.open(path1) as reader:
        for id,obj in enumerate(reader):
            if (id+1) in path1_list:
                save_list.append(obj)
    with jsonlines.open(path2) as reader:
        for id,obj in enumerate(reader):
            if (id+1) in path2_list:
                save_list.append(obj)
    with jsonlines.open(path3) as reader:
        for id,obj in enumerate(reader):
            save_list.append(obj)
    with jsonlines.open(path4) as reader:
        for id,obj in enumerate(reader):
            if id>=50:
                break
            save_list.append(obj)
    with jsonlines.open(save_path, mode='w') as writer:
        for line in save_list:
            jsonlines.Writer.write(writer, line)
sample_process()

def covert_to_jsonl():
    from_path = r"F:\SOEN_691\extracted_results\Yiping_selection.csv"
    save_path = r"F:\SOEN_691\extracted_results\output3.jsonl"
    save_list = []
    data_df = pd.read_csv(from_path)
    for id,row in data_df.iterrows():
        save_dic = {}
        save_dic['path'] = row['path']
        save_dic['func_head'] = row['func_head']
        save_dic['with_docstring'] = row['with_docstring']
        save_dic['full_method'] = row['full_method']
        save_dic['func_head'] = row['func_head']
        save_list.append(save_dic)

    with jsonlines.open(save_path, mode='w') as writer:
        for line in save_list:
            jsonlines.Writer.write(writer, line)
