def solution(participant, completion):
    p_hash = {name : 0 for name in participant}
    for name in participant:
        p_hash[name] += 1
    for name in completion:
        p_hash[name] -= 1
    p_hash_rev = {v : k for k, v in p_hash.items()}
    return p_hash_rev[1]
