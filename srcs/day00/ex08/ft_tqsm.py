import sys
import time
from tqdm import tqdm

class ProgressMeter:
    def __init__(self, total, length=40, prefix='', suffix='', decimals=1, update_interval=0.1):
        self.total = total
        self.length = length
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.update_interval = update_interval
        self.start_time = time.time()
        self.last_update = 0
        self.current = 0

    def _format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def _print_bar(self, iteration):
        elapsed = time.time() - self.start_time
        percent = 100 * (iteration / float(self.total))
        filled_length = int(self.length * iteration // self.total)
        bar = '█' * filled_length + '-' * (self.length - filled_length)
        eta = elapsed / iteration * (self.total - iteration) if iteration > 0 else 0

        progress = f'\r{self.prefix} |{bar}| {iteration}/{self.total} {self.suffix} '

        progress += f'Elapsed: {self._format_time(elapsed)}, ETA: {self._format_time(eta)}'

        sys.stdout.write(progress)
        sys.stdout.flush()

    def update(self, step=1):
        self.current += step
        if time.time() - self.last_update >= self.update_interval or self.current == self.total:
            self._print_bar(self.current)
            self.last_update = time.time()
        if self.current == self.total:
            print()

    def iter(self, iterable):
        for item in iterable:
            yield item
            self.update()

# Example usage
if __name__ == "__main__":
    import time

    total = 100
    meter = ProgressMeter(total, prefix='100%', suffix='Complete', length=50)

    for i in range(total):
        time.sleep(0.05)
        meter.update()

    for i in tqdm(range(10000)):
        pass
