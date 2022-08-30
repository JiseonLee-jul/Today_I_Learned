def solution(answers):
    stu1 = '12345' * (int(len(answers) / 5) + 1)
    stu2 = '21232425' * (int(len(answers) / 8) + 1)
    stu3 = '3311224455' * (int(len(answers) / 10) + 1)
    score = [0] * 3
    
    for i, answer in enumerate(answers):
        if answer == int(stu1[i]):
            score[0] += 1
        if answer == int(stu2[i]):
            score[1] += 1    
        if answer == int(stu3[i]):
            score[2] += 1 
            
    return [i+1 for i, v in enumerate(score) if v == max(score)]
