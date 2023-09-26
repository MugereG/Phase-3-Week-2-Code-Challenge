class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set([review.restaurant() for review in self.reviews]))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews])
        return total_ratings / len(self.reviews)


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant


