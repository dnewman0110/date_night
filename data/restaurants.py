"""Curated restaurant data for the date-night app.

All within easy walking distance of the Esquire IMAX Theatre, 1211 K St,
Sacramento, CA 95814. Menu items are sourced from each restaurant's real,
current published menus.
"""

RESTAURANTS = [
    {
        "id": "ella",
        "name": "Ella Dining Room & Bar",
        "cuisine": "New American · Farm-to-Fork",
        "price_range": "$$$$",
        "rating": "4.5",
        "address": "1131 K St, Sacramento, CA 95814",
        "walk_minutes": 3,
        "blurb": (
            "One block from the theater. Elegant farm-to-fork dining with a "
            "raw bar, wood-fired entrees, and an award-winning wine list."
        ),
        "reservation_platform": "opentable",
        "reservation_url": "https://www.opentable.com/ella-dining-room-and-bar-reservations-sacramento?restref=16474&lang=en-US",
        "menu": {
            "Fruits de Mer": [
                ("Oysters on the Half Shell", "Cocktail sauce and cucumber mignonette", "Half Dozen $24 / Dozen $46"),
                ("Caviar Service", "Tsar Nicoulai Reserve American sturgeon caviar, classic accoutrements, buttermilk blini", "$135"),
                ("Chilled Maine Lobster", "Grilled lemon, drawn butter, herb salad", "$90"),
                ("Grand Seafood Plateau", "1 whole chilled Maine lobster, 18 oysters, 8 poached Gulf prawns, salmon tartare with potato chips", "$185"),
            ],
            "Bread Service": [
                ("Bread & Butter", "Epi baguette, salted butter", "$10"),
                ("Truffle Brioche", "Housemade rolls, truffle butter, shaved black truffles", "$25"),
            ],
            "Small Plates": [
                ("Artisan Cheese", "Creamy goat brie, Estero Gold Reserve, Fennel Bay blue, seasonal accoutrements, crostini", "$25"),
                ("Steak Tartare", "Herb salad, fried capers, farm egg, garlic-parsley popovers", "$18"),
                ("Wood Fired Bone Marrow", "Caramelized onion butter, mushroom conserva, herb salad, grilled sourdough", "$26"),
                ("Heirloom Tomatoes", "Roasted golden beets, aged balsamic, petite fennel, mint chimichurri", "$16"),
            ],
            "Soups and Salads": [
                ("Zucchini Basil Soup", "Sumac pine nuts, farmer's cheese, sourdough crostini", "$16"),
                ("Ella Caesar Salad", "Hearts of romaine, soft egg, white anchovy, herb breadcrumbs", "$22"),
                ("Peach and Endive", "Whipped blue cheese, candied walnut, pickled lemon, white wine vinaigrette", "$18"),
                ("Baby Lettuces", "Fresh strawberries, goat cheese, pickled shallot and Fresno chilies, hazelnuts, Champagne basil vinaigrette", "$16"),
            ],
            "Entrees": [
                ("Crispy Fried Half Chicken", "Roasted garlic, fried herbs, housemade hot sauce, lemon", "$35"),
                ("Pan Roasted King Salmon", "Confit summer squash, zucchini bread, yellow corn, cherry tomatoes, avocado mousse", "$48"),
                ("Smoked Tomato Spaghetti", "Wood fired tomato sauce, slow roasted tomatoes, burrata, peperonata, pesto (add Périgord truffle $30)", "$38"),
                ("Pan Seared California Halibut", "Lardon, black garlic puree, caper agrodolce, Savoy cabbage, bourbon candied Fresno chilies", "$54"),
                ("Wood Fired Brandt Beef Tenderloin", "Salt baked potato, porcini au poivre, butter braised wild mushrooms, charred shallot", "$83"),
                ("Chanterelle Mushroom Paella", "Chanterelle mushrooms, sweet corn, piquillo peppers, roasted cherry tomato, huitlacoche, saffron aioli", "$58"),
                ("Lobster Paella", "Razor clams, calamari, halibut, garlic chorizo, piquillo peppers, roasted cherry tomato, saffron aioli", "$93"),
                ("48oz Tomahawk Ribeye", "Slow roasted tomato, grilled garlic scapes, Bordelaise, choice of side", "$165"),
            ],
            "Sides": [
                ("Grilled Summer Squash", "Bagna cauda, Parmesan, breadcrumbs, lemon", "$14"),
                ("Syracuse Potatoes", "Salt baked potatoes, dill beurre blanc, charred shallot", "$16"),
                ("Wood Fired Roasted Peppers", "Shishitos, sweet peppers, crescenza fondue, peanut crumble", "$16"),
            ],
        },
    },
    {
        "id": "frank_fats",
        "name": "Frank Fat's",
        "cuisine": "Classic Chinese · Since 1939",
        "price_range": "$$$",
        "rating": "4.4",
        "address": "806 L St, Sacramento, CA 95814",
        "walk_minutes": 6,
        "blurb": (
            "A Sacramento institution and James Beard America's Classic "
            "award winner, a short walk from the theater near the Capitol."
        ),
        "reservation_platform": "opentable",
        "reservation_url": "https://www.opentable.com/frank-fats",
        "menu": {
            "Appetizers": [
                ("Pot Stickers", "House favorite with pork and vegetables — a Frank Fat's recipe", "$14.50"),
                ("Yu Kwok", "Frank's special beef and pork dumpling, a Frank Fat specialty", "$14.75"),
                ("Honey Glazed BBQ Pork", "Slices of honey glazed pork roasted in our Chinese BBQ oven, served with pickled cucumbers", "$15.95"),
                ("Vegetable Spring Rolls", "Crispy spring rolls filled with shredded vegetables", "$14.50"),
                ("Salt & Pepper Calamari", "With seasoned salt, fried garlic and fresh jalapeno peppers", "$17.25"),
                ("Fats Special Wok-fried Spareribs", "Wok-fried, bite-size pork ribs with seasoned salt", "$17.25"),
                ("Mongolian Baby Back Ribs", "Wok-fried with a peppery plum sauce", "$18.25"),
                ("Chicken In Lettuce Cup", "With Chinese pork sausage, celery, carrots, and pine nuts, served with hoisin and plum sauce", "$17.25"),
                ("Salt & Pepper Chicken", "Lightly battered tender strips of chicken breast, red and green bell peppers with spiced salt, pepper, and jalapenos", "$16.75"),
                ("Combination Platter", "A platter of everyone's favorites — yu kwok, salt and pepper chicken, spring rolls, and pot stickers", "$24.50"),
                ("Shrimp Purses", "Steamed dumplings of shrimp, celery, and carrot in a wonton wrap", "$15.50"),
            ],
            "Soups & Salad": [
                ("Hot And Sour Soup", "With shrimp, shredded pork, bean curd, and bamboo shoots (serves two)", "$14.50"),
                ("Frank's Wor Won Ton Soup", "Pork and shrimp dumplings with chicken, shrimp, barbecued pork, mushrooms, carrots, water chestnuts, snow peas, broccoli stalk and bok choy", "$18.25"),
                ("Chinese Chicken Salad", "Entree size — poached chicken breast with pickled cucumber, almonds, tomatoes, wonton crisps, and a house-made sesame soy vinaigrette", "$18.75"),
            ],
            "Chicken": [
                ("Singapore Curry Chicken", "Stir-fried chicken breast, onions, peppers and mushrooms in a spicy curry sauce", "$22.25"),
                ("Chicken Wingo", "Grilled boneless chicken wings with zucchini and peppers in black bean sauce — Wing Fat's favorite", "$23.25"),
                ("General Tsao's Chicken", "Fried chicken breast in a tangy sweet glaze over broccoli", "$23.25"),
                ("Fat's Brandy Fried Chicken", "Frank's recipe: a half chicken marinated with brandy, fresh ginger, garlic, and soy — a Frank Fat specialty", "$24.25"),
                ("Orange Chicken", "Chicken with chili and zesty orange sauce", "$23.25"),
                ("Kung Pao Chicken", "Stir-fried chicken breast, red and green peppers, broccoli stalk, water chestnuts, jalapenos and peanuts", "$22.75"),
                ("Saigon Crispy Chicken", "Sliced, battered, and deep fried, stir-fried in a spicy tangerine sauce with garlic and topped with green onions", "$22.25"),
                ("All Seasons Stir Fry", "Chicken, shrimp, pork, beef, Chinese broccoli, baby bok choy and carrots", "$23.25"),
            ],
            "Pork, Beef & Lamb": [
                ("Pineapple Sweet & Sour Pork", "With bell peppers and lychee in a sweet and sour sauce", "$22.25"),
                ("Mongolian Beef", "Sliced beef, green onions, mushrooms and chilies", "$23.50"),
                ("Szechuan Beef", "With broccoli, wood ear mushroom, onions, bell peppers, and broccoli stalk in a spicy Szechuan sauce", "$23.50"),
                ("Immigrant's Beef", "Medallions of marinated flank steak with brandy, garlic, ginger, soy and sesame oil, grilled and served over zucchini — a family signature item", "$23.50"),
                ("Curry Beef Short Ribs", "Boneless short ribs with onions, mushrooms and bell peppers in curry sauce", "$23.50"),
                ("Frank's Style New York Steak", "16-ounce NY steak smothered in sauteed onions and oyster sauce — a Frank Fat specialty", "$49.95"),
                ("Beef Short Rib Stew", "Cantonese style stewed short ribs with carrots, potatoes, dikon and ginger", "$23.25"),
                ("Stir-Fry Cumin Spiced Lamb", "Superior Farms' lamb stir-fried with onions, peppers & broccoli stem", "$28.25"),
                ("Curry Lamb", "Superior Farms' lamb with onions, mushrooms, and bell peppers in a curry sauce", "$28.25"),
            ],
            "Seafood": [
                ("Seafood Pot", "Clams, shrimp, calamari, scallops stir-fried in chili black bean sauce with mushrooms, peppers, fried tofu over broccoli", "$24.25"),
                ("Honey Walnut Prawns", "Lightly fried prawns glazed with honey sauce, walnuts, sesame seeds — an all-time Sacramento favorite", "$24.50"),
                ("Phoenix & Dragon", "Shrimp and grilled medallions of boneless chicken wings with straw mushrooms, broccoli stalk, and bell peppers", "$26.50"),
                ("Kung Pao Triple Crown", "Shrimp, chicken and beef stir-fried with red and green peppers and onion, broccoli stalk, and water chestnuts, garnished with roasted peanuts", "$24.25"),
                ("Honey & Soy Marinated Cod", "Served with Chinese mustard greens & mushrooms", "$24.25"),
                ("Pan Grilled Bacon Wrapped Scallops", "With green beans and oyster cream sauce", "$32.50"),
            ],
            "Noodles": [
                ("Vegetable Chow Fun", "With seasonal vegetables, mushrooms, and onions", "$19.25"),
                ("Chili Beef Chow Fun", "With chili peppers, onions, and bean sprouts", "$21.95"),
                ("Sang Gai Shee Chow Mein", "Egg noodles with chicken, black mushrooms, and snow peas — a Frank Fat specialty", "$22.25"),
                ("Hunan Chicken Chow Mein", "Chicken, red and green peppers and onions in a spicy black bean sauce, served over thin pan-fried noodles", "$22.25"),
                ("Imperial Chow Mein", "With barbecued pork, beef, chicken, shrimp, calamari and scallops, served over thin pan-fried noodles", "$23.25"),
                ("Hong Kong Sum-See Chow Mein", "Pork, chicken, shrimp, bean sprouts, snow peas, carrots and mushrooms served over thin pan-fried noodles", "$22.25"),
                ("Singapore Noodles", "Rice noodles tossed with barbecued pork, baby shrimp, onions, egg, bean sprouts and red and green bell peppers in a spicy curry sauce", "$22.25"),
                ("Spicy Beef Noodle Soup", "Choice of wheat or rice noodles with carrots, onions, bok choy and braised short ribs in Northern China spices", "$18.95"),
            ],
            "Fresh Vegetables": [
                ("Garlic Chili Green Beans", "Fat's own recipe, an all-time guest favorite", "$16.25"),
                ("Szechuan Eggplant", "Fried Chinese eggplant, crisped and served with a spicy Szechuan sauce, onions and peppers", "$15.25"),
                ("Baby Bok Choy Stir-Fried in Garlic Sauce", "", "$15.25"),
                ("Gai Lan", "Fresh, crisp Chinese broccoli, steamed and drizzled with oyster sauce", "$17.95"),
                ("Seasonal Mushrooms & Mustard Greens", "In garlic oyster sauce", "$16.25"),
                ("Ma Po Tofu", "With silken tofu in a spicy Szechuan sauce", "$15.25"),
                ("Braised Tofu & Mushroom", "Lightly fried silken tofu with fresh mushrooms & scallions", "$15.25"),
                ("Buddha's Delight", "Mixture of fresh vegetables, wok-tossed with tofu in garlic black bean sauce", "$15.25"),
            ],
            "Rice": [
                ("Vegetable Fried Rice", "With seasonal vegetables", "$16.25"),
                ("Chicken or Pork Fried Rice", "With peas, carrots and lettuce", "$18.95"),
                ("Young Shew Fried Rice", "With barbecued pork, Chinese sausage, baby shrimp, peas, carrots and lettuce", "$19.25"),
                ("Dried Scallop Fried Rice", "With white and green onions, green beans and egg whites", "$21.50"),
                ("Steamed White Rice", "", "$3.00"),
                ("Steamed Brown Rice", "", "$3.00"),
            ],
            "Dessert": [
                ("Banana Cream Pie", "The restaurant's legendary classic dessert", "$8.95"),
                ("Chocolate Cream Pie", "", "$8.95"),
            ],
        },
    },
    {
        "id": "firehouse",
        "name": "The Firehouse Restaurant",
        "cuisine": "New American · Old Sacramento",
        "price_range": "$$$$",
        "rating": "4.5",
        "address": "1112 2nd St, Sacramento, CA 95814",
        "walk_minutes": 10,
        "blurb": (
            "Housed in an 1853 firehouse in the Old Sacramento waterfront "
            "district — a romantic, historic setting with a courtyard patio."
        ),
        "reservation_platform": "tock",
        "reservation_url": "https://www.exploretock.com/the-firehouse-restaurant-sacramento",
        "menu": {
            "Starters": [
                ("Oysters on the Half Shell", "Half-dozen seasonal oysters, lemon, pink peppercorn mignonette", "$34"),
                ("Grilled Peach, Ricotta & Caviar", "Pistachio, honey, arugula, crostini", "$44"),
                ("Burrata Stuffed Heirloom Tomato", "Balsamic marinated cherry tomatoes, tomato gelée, micro basil", "$24"),
                ("Mushroom & Cheese Ravioli", "Leeks, black truffle butter sauce", "$24"),
                ("Potato Gnocchi", "Parmesan cream sauce, fried brussels, crispy prosciutto", "$22"),
                ("Grilled Calamari Steak", "White bean, fennel & leek salad, arugula, romesco, lemon vinaigrette", "$22"),
                ("Pan-Seared Diver Scallops", "Corn maque choux, tomatoes, blistered peppers", "$28 / $56"),
            ],
            "Soup & Salad": [
                ("Summer Corn Soup", "Butter poached shrimp & lobster", "$24"),
                ("Farmers Market Salad", "Baby lettuces, goat cheese, strawberries, fennel, almonds", "$18"),
                ("Caesar Salad", "Little gem lettuce, baby red romaine, parmesan crisps, pan-roasted croutons", "$18"),
                ("Belgian Endive Salad", "Watercress, pears, port glazed figs, blue cheese vinaigrette", "$18"),
            ],
            "Entrées": [
                ("Ora King Salmon", "Caramelized brussels sprouts, bacon, kohlrabi", "$58"),
                ("Grilled 14oz Niman Ranch Pork Chop", "Mushroom risotto, herb jus", "$54"),
                ("Grilled 16oz Prime Ribeye Steak", "Roasted fingerling potatoes, chimichurri sauce", "$88"),
                ("Braised Beef Short Rib", "Potato purée, baby carrots, red wine sauce", "$64"),
                ("Slow-Roasted Beef Filet", "Potato gratin, green beans, bordelaise sauce", "$76"),
                ("Rack of Lamb", "Grilled eggplant ratatouille, herb lamb jus", "$78"),
                ("Shellfish Bouillabaisse", "Butter poached half lobster, seared scallop, shrimp & halibut, potato purée, leeks, fennel, cherry tomatoes", "$89"),
                ("Steak & Lobster", "Slow-roasted beef filet, potato purée, bordelaise, butter-poached half lobster, truffle-risotto cake, spinach", "$108"),
            ],
        },
    },
]


def get_restaurant(restaurant_id: str) -> dict:
    for r in RESTAURANTS:
        if r["id"] == restaurant_id:
            return r
    raise KeyError(f"Unknown restaurant id: {restaurant_id}")
