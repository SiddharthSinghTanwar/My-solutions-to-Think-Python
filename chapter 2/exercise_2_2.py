'''
Exercise 2.2. Practice using the Python interpreter as a calculator:
1. The volume of a sphere with radius r is (4/3)πr^3. What is the volume of a sphere with radius 5?
2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
'''
#Answer 1
>>> radius = 5
>>> volume = (4 * 3.14 * radius**3) /3
>>> volume
523.3333333333334

#Answer 2
>>> cover_price = 24.95
>>> discount = 0.40
>>> no_of_copies = 60
>>> shipping_costs = 3 + 0.75 * (no_of_copies - 1)
>>> total_cost = (cover_price * no_of_copies) * (1 - discount) + shipping_costs
>>> total_cost
945.4499999999999

#Answer 3
>>> start_time = (6 * 60 *60) + (52 * 60)
>>> easy_pace = (8 * 60) + 15
>>> easy_pace = easy_pace * 2
>>> tempo = (7 * 60) + 12
>>> tempo = tempo * 3
>>> final_time = start_time + easy_pace + tempo
>>> final_time
27006
>>> final_seconds = final_time % 60
>>> minutes  = final_time / 60
>>> final_minutes = minutes % 60 - final_seconds / 60
>>> final_hours = minutes / 60 - final_minutes / 60
