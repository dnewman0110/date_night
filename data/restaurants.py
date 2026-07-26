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
        "menu": {
            "Small Plates": [
                ("Steak Tartare", "Herb salad, fried capers, farm egg, garlic-parsley popovers", "$18"),
                ("Wood Fired Bone Marrow", "Caramelized onion butter, mushroom conserva", "$26"),
                ("Heirloom Tomatoes", "Roasted beets, balsamic, mint chimichurri", "$16"),
            ],
            "Soups & Salads": [
                ("Ella Caesar Salad", "Romaine, soft egg, white anchovy", "$22"),
                ("Zucchini Basil Soup", "Sumac pine nuts, farmer's cheese", "$16"),
                ("Baby Lettuces", "Strawberries, goat cheese, hazelnuts", "$16"),
            ],
            "Entrees": [
                ("Crispy Fried Half Chicken", "Roasted garlic, fried herbs, housemade hot sauce", "$35"),
                ("Pan Roasted King Salmon", "Confit squash, corn, avocado mousse", "$48"),
                ("Smoked Tomato Spaghetti", "Wood-fired tomato sauce, burrata, pesto", "$38"),
                ("Wood Fired Brandt Beef Tenderloin", "Salt-baked potato, porcini au poivre", "$83"),
            ],
            "From the Sea": [
                ("Oysters on the Half Shell", "Cocktail sauce, cucumber mignonette", "Half dozen $24"),
                ("Chilled Maine Lobster", "Grilled lemon, drawn butter, herb salad", "$90"),
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
        "menu": {
            "Appetizers": [
                ("Pork Pot Stickers", "Savory pork and fresh vegetables, pan-fried", "$15.95"),
                ("Salt and Pepper Calamari", "Crisp-fried, classic Frank Fat's seasoning", "$18.00"),
                ("Spring Rolls", "Garden-fresh vegetables, crispy wrapper", "$14.00"),
                ("Chinese Chicken Salad", "House specialty, a Sacramento classic", "$16.00"),
            ],
            "Entrees": [
                ("Honey Walnut Prawns", "Frank Fat's signature dish", "$26.95"),
                ("Orange Chicken", "Crispy chicken in tangy orange glaze", "$24.50"),
                ("Sang Gai Shee Chow Mein", "Shredded chicken pan-fried noodles", "$23.25"),
                ("Garlic Chili Green Beans", "Wok-charred, classic side", "$17.25"),
                ("Pork Fried Rice", "Wok-fried with egg and scallion", "$21.00"),
            ],
            "Dessert": [
                ("Banana Cream Pie", "The restaurant's legendary classic dessert", "$12.00"),
            ],
            "Cocktails": [
                ("Frank Fat's Mai Tai", "Handcrafted the same way for generations", "$14.00"),
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
        "menu": {
            "Starters": [
                ("Oysters on the Half Shell", "Half-dozen seasonal oysters, lemon, pink peppercorn mignonette", "$34"),
                ("Burrata Stuffed Heirloom Tomato", "Cherry tomatoes, tomato gelée, micro basil", "$24"),
                ("Potato Gnocchi", "Parmesan cream, fried Brussels sprouts, crispy prosciutto", "$22"),
            ],
            "Soup & Salad": [
                ("Farmers Market Salad", "Baby lettuces, goat cheese, strawberries, fennel, almonds", "$18"),
                ("Caesar Salad", "Little gem lettuce, baby red romaine, Parmesan crisps", "$18"),
                ("Summer Corn Soup", "Butter poached shrimp and lobster", "$24"),
            ],
            "Entrees": [
                ("Ora King Salmon", "Caramelized Brussels sprouts, bacon, kohlrabi", "$58"),
                ("Grilled Pork Chop", "14oz Niman Ranch, mushroom risotto, herb jus", "$54"),
                ("Prime Ribeye Steak", "16oz grilled, fingerling potatoes, chimichurri", "$88"),
                ("Rack of Lamb", "Grilled eggplant ratatouille, herb lamb jus", "$78"),
            ],
        },
    },
]


def get_restaurant(restaurant_id: str) -> dict:
    for r in RESTAURANTS:
        if r["id"] == restaurant_id:
            return r
    raise KeyError(f"Unknown restaurant id: {restaurant_id}")
