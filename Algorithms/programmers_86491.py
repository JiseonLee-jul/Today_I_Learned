def solution(sizes):
    
    for i, (w, h) in enumerate(sizes):
        w_max = max([w for w, _ in sizes]) 
        h_max = max([h for _, h in sizes]) 
        if w_max >= h_max:
            sizes[i] = [max(w, h), min(w, h)]
        else:
            sizes[i] = [min(w, h), max(w, h)]           
    
    w_max = max([w for w, _ in sizes]) 
    h_max = max([h for _, h in sizes])
    
    return w_max * h_max
