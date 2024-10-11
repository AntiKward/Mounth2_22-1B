my_list = ["Москва", "Лондон", "Нью-Йорк", "Рок", "Джаз", "Классическая", "Tesla", "BMW", "Audi", "Лето", "Зима", "Весна", "Python", "C++", "Guitar"]
print(my_list[2:7])

numb_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numb_list.reverse()
print(numb_list)

minimum = min(numb_list)
print(minimum)

maximum = max(numb_list)
print(maximum)

sum_list = sum(numb_list)
print(sum_list)

math = sum(numb_list) / len(numb_list)
print(math)

clear_list = numb_list.clear()
print(numb_list)

music = ['song1', 'song2', 'song3', 'song4', 'song5', 'song6', 'song7', 'song8', 'song9', 'song10']
music[3], music[7] = music[7], music[3]
print(music)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110]

print(f'{numbers.count(110)} - раза встречается число 110')

a = [1, 3, 4, 5] 
b = [4, 5, 6, 7]
a.extend(b)
result = list(set(a))
print(result)

name_1 =  "Aidana"
name_2 = "Adilet" 
name_1[0] + name_2[0] + name_1[1] + name_2[1] + name_1[2] + name_2[2] + name_1[3] + name_2[3] + name_1[4] + name_2[4] + name_1[5] + name_2[5]
print(name_1[0] + name_2[0] + name_1[1] + name_2[1] + name_1[2] + name_2[2] + name_1[3] + name_2[3] + name_1[4] + name_2[4] + name_1[5] + name_2[5])

text_cool = ''' Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'''
count_py_1 = text_cool.count('t'); count_py_2 = text_cool.count('s')
print(f'{count_py_1} букв t и {count_py_2} букв s')
name = text_cool.replace('Advert','ADVERT').replace('advert', 'ADVERT')
print(name)