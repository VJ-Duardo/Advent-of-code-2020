import re

fields = {}
tickets = []
own_ticket = []
with open("tickets.txt") as file:
    parts = re.split("\n\nyour ticket:\n", file.read())
    for field in parts[0].split("\n"):
        matches = re.findall(".+(?=:)|\d+-\d+", field)
        fields[matches[0]] = [tuple(map(int, match.split('-'))) for match in matches[1:]]

    ticket_parts = re.split("\n\nnearby tickets:\n", parts[1])
    own_ticket = list(map(int, ticket_parts[0].split(',')))
    tickets = [list(map(int, nearby_ticket.split(','))) for nearby_ticket in ticket_parts[1].split("\n") if nearby_ticket != '']


    
def check_to_fields(number):
    for field in fields.values():
        for f_range in field:
            if f_range[0] <= number <= f_range[1]:
                return True
    return False


def get_tser():
    invalid = []
    for i in range(len(tickets)-1, -1, -1):
        for number in tickets[i]:
            if not check_to_fields(number):
                invalid.append(number)
                tickets.pop(i)
    return sum(invalid)



def find_field_positions():
    fitting_positions = {}
    f_ranges = list(fields.values())
    for i in range(len(own_ticket)):
        fitting_positions[i] = []
        for j in range(len(f_ranges)):
            found = True
            for ticket in tickets:
                if not (f_ranges[j][0][0] <= ticket[i] <= f_ranges[j][0][1]
                        or f_ranges[j][1][0] <= ticket[i] <= f_ranges[j][1][1]):
                    found = False
                    break
            if found:
                fitting_positions[i].append(j)

    fitting_positions = dict(sorted(fitting_positions.items(), key=lambda item: len(item[1]), reverse=True))

    field_positions = [-1]*len(own_ticket)
    curr_claims = {}
    while field_positions.count(-1) > 1:
        for i in fitting_positions.keys():
            while fitting_positions[i][0] in field_positions:
                fitting_positions[i].pop(0)
            curr_claims[fitting_positions[i].pop(0)] = i
        for win in curr_claims.keys():
            field_positions[curr_claims[win]] = win
            del fitting_positions[curr_claims[win]]
        curr_claims = {}

    return field_positions


def get_departure_product():
    departure_indexes = [field[0] for field in enumerate(fields.keys()) if re.search("departure", field[1])]
    field_indexes = find_field_positions()
    dep_indexes_ticket = [index[0] for index in enumerate(field_indexes) if index[1] in departure_indexes]

    product = 1
    for i in dep_indexes_ticket:
        product = product * own_ticket[i]

    return product
        
            
                    
print(get_tser())
print(get_departure_product())
