# map : Series의 single value를 입력값으로 받음
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

# apply : DataFrame의 each row를 입력값으로 받음 
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
