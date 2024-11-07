from datetime import datetime, timedelta


class Court:
    def __init__(self, court_number):
        self.court_number = court_number
        self.free_times = []
        self.free_days = []

    def add_free_time(self, start_time_str, end_time_str, day):
        """Dodaj czas dostępności do listy, z uwzględnieniem dnia"""
        start_time = datetime.strptime(start_time_str, "%H:%M")
        end_time = datetime.strptime(end_time_str, "%H:%M")
        self.free_times.append((start_time, end_time, day))

    def has_free_time_longer_than_hour(self):
        """Sprawdź, czy kort jest wolny przez więcej niż godzinę w dowolnym dniu, bez przerw"""
        self.free_days = []  # Resetujemy listę dni

        # Grupa czasów według dnia
        free_times_by_day = {}
        for start_time, end_time, day in self.free_times:
            if day not in free_times_by_day:
                free_times_by_day[day] = []
            free_times_by_day[day].append((start_time, end_time))

        # Przejdź przez dni i sprawdź dostępność
        for day, times in free_times_by_day.items():
            # Sortowanie wolnych godzin dla danego dnia
            times.sort()
            current_start, current_end = times[0]

            for start, end in times[1:]:
                if start <= current_end:  # Sprawdzamy, czy godziny się łączą
                    current_end = max(current_end, end)  # Rozszerzamy czas
                else:
                    if current_end - current_start > timedelta(hours=1):  # Sprawdzamy, czy przerwa trwała dłużej niż godzinę
                        self.free_days.append(day)
                        break
                    current_start, current_end = start, end

            # Sprawdzamy ostatni okres
            if current_end - current_start > timedelta(hours=1):
                self.free_days.append(day)

        return self.free_days



