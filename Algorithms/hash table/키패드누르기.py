def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(1,0),3:(2,0),\
                4:(0,1),5:(1,1),6:(2,1),\
                7:(0,2),8:(1,2),9:(2,2),\
                '*':(0,3),0:(1,3),'#':(2,3)}
    
    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            i_pos = key_dict[i]
            lh_pos = key_dict[lhand]
            rh_pos = key_dict[rhand]
            dis_l = abs(lh_pos[0] - i_pos[0]) + abs(lh_pos[1] - i_pos[1])
            dis_r = abs(rh_pos[0] - i_pos[0]) + abs(rh_pos[1] - i_pos[1])
            if dis_l < dis_r:
                answer += 'L'
                lhand = i
            elif dis_l > dis_r:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i  
                else:
                    answer += 'R'
                    rhand = i 
                     
    return answer
