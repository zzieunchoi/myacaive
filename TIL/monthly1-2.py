restaurant = dict(id = [0, 1, 2, 3, 4], user_rating = [4.5, 7.3, 1.9, 5.6, 9], name = ['burger-r', 'pasta-r', 'soup-r', 'chicken-r', 'ice-cake-r'], 
menus = ['burger', 'pasta', 'soup', 'chicken', 'ice-cake'], location = ['busan', 'suwon', 'seoul', 'gumi', 'daejeon'])

print(restaurant)

def my_len(a):
    cnt = 0
    for i in a:
        cnt += 1
    return cnt

def menu_count(dict):
    return my_len(dict['menus'])
    
print(f'음식점에서 판매하는 메뉴의 개수: {menu_count(restaurant)}')