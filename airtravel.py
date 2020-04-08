class Flight:
    """
    A flight with a particular passenger aircraft
    """

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in {number}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code")
        if not number[2:].isdigit() and int(number) <= 9999:
            raise ValueError(f"Invalid route number")

        self._number = number
        self._aircraft = aircraft
        rows, seats = aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def model(self):
        return self._aircraft.model()

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """
        Allocates a seat to a passenger

        args:
            seat: a seat of designator such as 12C or 21F
            passenger: the passenger'sname

        :raises
            ValueError: if seat is unavailable
        """
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied")
        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        """
        validation function for allocate seat
        :param seat:
        :return seat:
        """
        rows, seating_letter = self._aircraft.seating_plan()
        letter = seat[-1]

        if letter not in seating_letter:
            raise ValueError(f"Invalid seat letter {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat number {row_text}")
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")
        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """
        relocates a passenger from a seat to another seat
        :param from_seat: the original seat designator
        :param to_seat: the new seat designator
        :return:
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if (self._seating[from_row][from_letter]) is None:
            raise ValueError(f"No passenger to relocate from {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if (self._seating[to_row][to_letter]) is not None:
            raise ValueError(f"The seat {to_seat} to move passenger is already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][to_letter]
        self._seating[from_row][to_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self._number, self.model())

    def _passenger_seats(self):
        """
        An iterable series of passenger seating locations
        :return:
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self.num_rows = num_rows
        self.num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self.num_rows + 1), "ABCDEFGHJK"[:self.num_seats_per_row])


def make_flight():
    flight = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    flight.allocate_seat("12A", "Guido Van Rossum")
    flight.allocate_seat("15F", "Bjarne Stroustrup")
    flight.allocate_seat("1D", "Rasmus Lordorf")
    flight.allocate_seat("3C", "James Gosling")
    flight.allocate_seat("4A", "Dennis Ritchie")
    return flight


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}" \
             f" Flight: {flight_number}" \
             f" Seat: {seat}" \
             f" Aircraft: {aircraft} |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def main():
    from pprint import pprint as pp
    flight = make_flight()
    print(flight.model())
    pp(flight._seating)
    flight.relocate_passenger("3C", "5D")
    pp(flight._seating)
    flight.make_boarding_cards(console_card_printer)
    #print(flight.num_available_seats())


if __name__ == '__main__':
    main()
