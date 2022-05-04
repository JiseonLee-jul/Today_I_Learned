##### my code
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

#####
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
