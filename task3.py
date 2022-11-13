postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}
lost_postcards = {
    "Petra": "Paris",
    "Ivan": "Moscow"
}
postcards.update(lost_postcards)
print(postcards)

postcards["Oleg"] = "Sydney"
print(postcards)

postcards_values = list(postcards.values())
print(set(postcards_values))
print(len(set(postcards_values)))
