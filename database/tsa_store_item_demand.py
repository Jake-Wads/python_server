#!/usr/bin/env python3

import pandas as pd

def partition(seq, size):
    # from http://stackoverflow.com/a/434328
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

# http://www.grocery.com/open-grocery-database-project/ + randomly generated prices
insert_items_sql = '''
INSERT INTO items(item_id, item_upc14, item_upc12, item_brand, item_name, item_price) VALUES
(1,00035200264013,035200264013,'Riceland','Riceland American Jazmine Rice',0.84),
(2,00011111065925,011111065925,'Caress','Caress Velvet Bliss Ultra Silkening Beauty Bar - 6 Ct',6.44),
(3,00023923330139,023923330139,'Earths Best','Earths Best Organic Fruit Yogurt Smoothie Mixed Berry',2.43),
(4,00208528800007,208528800007,'Boars Head','Boars Head Sliced White American Cheese - 120 Ct',3.14),
(5,00759283100036,759283100036,'Back To Nature','Back To Nature Gluten Free White Cheddar Rice Thin Crackers',2.61),
(6,00074170388732,074170388732,'Sally Hansen','Sally Hansen Nail Color Magnetic 903 Silver Elements',6.93),
(7,00070177154004,070177154004,'Twinings Of London','Twinings Of London Classics Lady Grey Tea - 20 Ct',9.64),
(8,00051600080015,051600080015,'Lea & Perrins','Lea & Perrins Marinade In-a-bag Cracked Peppercorn',1.68),
(9,00019600923015,019600923015,'Van De Kamps','Van De Kamps Fillets Beer Battered - 10 Ct',1.79),
(10,00688267141676,688267141676,'Ahold','Ahold Cocoa Almonds',3.17),
(11,00657622604842,657622604842,'Honest Tea','Honest Tea Peach White Tea',3.93),
(12,00074676640211,074676640211,'Mueller','Mueller Sport Care Basic Support Level Medium Elastic Knee Support',8.4),
(13,00603084234561,603084234561,'Garnier Nutritioniste','Garnier Nutritioniste Moisture Rescue Fresh Cleansing Foam',6.47),
(14,00041167300121,041167300121,'Pamprin','Pamprin Maximum Strength Multi-symptom Menstrual Pain Relief',7.54),
(15,00079400847201,079400847201,'Suave','Suave Naturals Moisturizing Body Wash Creamy Tropical Coconut',9.11),
(16,00792850014008,792850014008,'Burts Bees','Burts Bees Daily Moisturizing Cream Sensitive',5.17),
(17,00088313590791,088313590791,'Ducal','Ducal Refried Red Beans',1.16),
(18,00021200725340,021200725340,'Scotch','Scotch Removable Clear Mounting Squares - 35 Ct',4.39),
(19,00041520035646,041520035646,'Careone','Careone Family Comb Set - 8 Ct',0.74),
(20,00204040000000,204040000000,'Usda Produce','Plums Black',5.62),
(21,00753950001954,753950001954,'Doctors Best','Doctors Best Best Curcumin C3 Complex 1000mg Tablets - 120 Ct',8.09),
(22,00016000288829,016000288829,'Betty Crocker','Betty Crocker Twin Pack Real Potatoes Scalloped 2 Pouches For 2 Meals - 2 Pk',7.31),
(23,00070670009658,070670009658,'Reese','Reese Mandarin Oranges Segments In Light Syrup',1.78),
(24,00688267084225,688267084225,'Smart Living','Smart Living Charcoal Lighter Fluid',5.34),
(25,00044100117428,044100117428,'Hood','Hood Latte Iced Coffee Drink Vanilla Latte',2.43),
(26,00300436344045,300436344045,'Triaminic','Triaminic Syrup Night Time Cold & Cough Grape 4oz',0.98),
(27,00024600017008,024600017008,'Morton','Morton Kosher Salt Coarse',6.01),
(28,00719175900007,719175900007,'Usda Produce','Guava',7.52),
(29,00013000001038,013000001038,'Heinz','Heinz Tomato Ketchup - 2 Ct',8.65),
(30,00723503568678,723503568678,'Petmate','Petmate Booda Bones Steak Bacon & Chicken Flavors - 9 Ct',8.39),
(31,00652790100226,652790100226,'Zhenas Gypsy Tea','Zhenas Gypsy Tea Herbal Red Tea Sachets Fire Light Chai - 22 Ct',4.21),
(32,00008500004528,008500004528,'Barefoot','Barefoot Pinot Grigio  187',0.68),
(33,00071463060078,071463060078,'The First Years','Tomy The First Years Gumdrop Orthodontic Pacifiers 6m+ - 2ct',6.52),
(34,00312546628694,312546628694,'Halls','Halls Menthol Cough Suppresant/oral Anesthetic Drops Honey-lemon - 30 Ct',4.17),
(35,00033674100066,033674100066,'Natures Way','Natures Way Forskohlii - 60 Ct',5.19),
(36,00610358991525,610358991525,'Deerfields Gluten Free','Rice Bran Gluten Free Dinner Rolls Plain',7.95),
(37,00073575295003,073575295003,'Nakano','Nakano Seasoned Rice Vinegar Original',9.59),
(38,00030768540548,030768540548,'Sundown Naturals','Sundown Naturals Essential Electrolytes Tropical Punch Watermelon And Fruit Punch Gummies - 60 Ct',3.45),
(39,00028400029254,028400029254,'Munchies','Munchies Sandwich Crackers Cheddar Cheese On Golden Toast Crackers - 8 Pk',9.02),
(40,00042272008063,042272008063,'Amys','Amys Light & Lean Spaghetti Italiano',0.6),
(41,00031000670016,031000670016,'P.f. Changs','P.f. Changs Home Menu Meal For Two Beef With Broccoli',5.62),
(42,00883978129115,883978129115,'Moms Best Naturals','Moms Best Naturals Cereal Toasted Cinnamon Squares',2.97),
(43,00071403000379,071403000379,'Ferrara','Ferrara Vanilla Syrup',8.4),
(44,00026000001403,026000001403,'Elmers','Elmers Board Mate Dual Tip Glue Pen',7.06),
(45,00038000542237,038000542237,'Kelloggs','Kelloggs Disney Pixar Cars 2 Cereal',4.4),
(46,00035457770664,035457770664,'Mama Marys','Pizza Sauce',4.65),
(47,00884623708976,884623708976,'Bear Naked','Bear Naked Fit Almond Crisp 100 Percent Natural Energy Cereal',7.38),
(48,00079400271631,079400271631,'Dove','Dove Men + Care Antiperspirant Deodorant Cool Silver',3.72),
(49,00062338879772,062338879772,'Easy-off','Easy-off Oven Cleaner Lemon Scent',9.54),
(50,00047445919221,047445919221,'Choice','Choice Organic Teas Black Tea Classic Black - 16 Ct',5.2);
'''

# "randomly" selected from google maps
insert_stores_sql = '''
INSERT INTO stores(store_id, store_address, store_zipcode, store_city, store_state) VALUES
(1, '12125 Alamo Ranch Pkwy', '78253', 'San Antonio', 'TX'),
(2, '9255 FM 471 West', '78251', 'San Antonio', 'TX'),
(3, '2118 Fredericksburg Rdj', '78201', 'San Antonio', 'TX'),
(4, '516 S Flores St', '78204', 'San Antonio', 'TX'),
(5, '1520 Austin Hwy', '78218', 'San Antonio', 'TX'),
(6, '1015 S WW White Rd', '78220', 'San Antonio', 'TX'),
(7, '12018 Perrin Beitel Rd', '78217', 'San Antonio', 'TX'),
(8, '15000 San Pedro Ave', '78232', 'San Antonio', 'TX'),
(9, '735 SW Military Dr', '78221', 'San Antonio', 'TX'),
(10, '8503 NW Military Hwy', '78231', 'San Antonio', 'TX');
'''

print('reading csv')
df = pd.read_csv('./data/tsa_store_item_demand_train.csv')
for col in df:
    df[col] = df[col].astype(str)
df.date = df.date.apply(lambda d: f"'{d}'")

# print('DEBUG: limiting to 100 rows')
# df = df.head(100)

# sales_values = ' VALUES (' + '), ('.join([', '.join(row.values) for _, row in df.iterrows()]) + ');'
sales_values = [', '.join(row.values) for _, row in df.iterrows()]

db_structure_sql = f'''
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS items;

CREATE TABLE stores(
    store_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    store_address VARCHAR(255) NOT NULL,
    store_zipcode VARCHAR(255) NOT NULL,
    store_city VARCHAR(255) NOT NULL,
    store_state VARCHAR(255) NOT NULL,
    PRIMARY KEY (store_id)
);

CREATE TABLE items(
    item_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    item_upc14 VARCHAR(14) NOT NULL,
    item_upc12 VARCHAR(12) NOT NULL,
    item_brand VARCHAR(255) NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    item_price DECIMAL(4, 2) NOT NULL,
    PRIMARY KEY (item_id)
);

CREATE TABLE sales(
    sale_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    sale_date DATE NOT NULL,
    store_id INT UNSIGNED NOT NULL,
    item_id INT UNSIGNED NOT NULL,
    sale_amount INT UNSIGNED NOT NULL,
    PRIMARY KEY(sale_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);
'''

def get_db_structure():
    return db_structure_sql

def get_stores_sql():
    return insert_stores_sql

def get_items_sql():
    return insert_items_sql

def format_insert_stmt(rows):
    sql = 'INSERT INTO sales(sale_date, store_id, item_id, sale_amount) VALUES ('
    sql += '), ('.join(rows)
    sql += ');'
    return sql

def get_sales_sql(chunksize=1000):
    return [format_insert_stmt(rows) for rows in partition(sales_values, chunksize)]

if __name__ == '__main__':
    print(get_db_structure())
    print(get_stores_sql())
    print(get_items_sql())
    for stmt in get_sales_sql():
        print(stmt)
