class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.time = [hours, minutes, seconds]
        self._normalize()
    def __str__(self):
        time_peices = []
        for index, element in enumerate(self.time):
            element_str = f"0{str(element)}" if element < 10 else str(element)
            if index <= 1:
                time_peices.append(f"{element_str}:")
            else:
                time_peices.append(element_str)
        return str().join(time_peices)
    
    def _normalize(self):
        # Normalize minutes/seconds and wrap hours into 0..23
        h, m, s = self.time
        m %= 60
        h += s // 60 // 60  # not needed if s < 60, kept for safety if init is messy
        m += (s // 60) % 60
        s %= 60
        # Re-normalize m in case s pushed it past 59
        h += m // 60
        m %= 60
        self.time = [h % 24, m, s]

    def _to_total_seconds(self):
        h, m, s = self.time
        return h * 3600 + m * 60 + s

    def _from_total_seconds(self, total):
        total %= 24 * 3600
        h, rem = divmod(total, 3600)
        m, s = divmod(rem, 60)
        self.time = [h, m, s]
        
    def next_second(self):
        self._from_total_seconds(self._to_total_seconds() + 1)
        return self  

    def prev_second(self):
        self._from_total_seconds(self._to_total_seconds() - 1)
        return self

if __name__ == "__main__":  
    timer = Timer(23, 59, 59)

    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
