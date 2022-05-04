def solution(id_list, report, k):
    answer = []
    report_dict = {}
    for user_id in id_list:
        report_dict[user_id] = []

    for j in report:
        user_id, rp_ids = j.split(' ')
        if rp_ids not in report_dict[user_id]:
            report_dict[user_id].append(rp_ids)
        
    count_dict = {}
    for user_id, rp_ids in report_dict.items():
        for rp_id in rp_ids:
            if rp_id in count_dict:
                count_dict[rp_id] += 1
            else:
                count_dict[rp_id] = 1
            
    report_list = []
    for i, i_num in count_dict.items():
        if i_num >= k:
            report_list.append(i)

    
    for user_id, rp_ids in report_dict.items():
        num = 0
        for rp_id in rp_ids:
            if rp_id in report_list:
                num += 1
        answer.append(num) 
    
    return answer
