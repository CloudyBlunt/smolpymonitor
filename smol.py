import psutil
import os
import time
import platform
import socket

def main():
    while True:
        ram = psutil.virtual_memory()
        ram_used = ram.total - ram.available
        ram_percent = 100 * float(ram_used)/float(ram.total)
        swap = psutil.swap_memory()
        
        swap_total = swap.total
        swap_used = swap.used
        swap_free = swap.free
        swap_percent = swap.percent

        cpu = psutil.cpu_percent()
        cpu_freqs = psutil.cpu_freq()
        freq_current = cpu_freqs.current
        freq_minimum = cpu_freqs.min
        freq_maximum = cpu_freqs.max
        cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)

        if cpu < 5:
            cpu_tab = "[                  ]"
        elif cpu < 15:
            cpu_tab = "[|                 ]"
        elif cpu < 35:
            cpu_tab = "[|||||             ]"
        elif cpu < 50:
            cpu_tab = "[|||||||||         ]"
        elif cpu < 80:
            cpu_tab = "[|||||||||||||     ]"
        else:
            cpu_tab = "[||||||||||||||||||]"

        if ram_percent < 5:
            ram_tab = "[                  ]"
        elif ram_percent < 15:
            ram_tab = "[|                 ]"
        elif ram_percent < 35:
            ram_tab = "[|||||             ]"
        elif ram_percent < 50:
            ram_tab = "[|||||||||         ]"
        elif ram_percent < 80:
            ram_tab = "[|||||||||||||     ]"
        else:
            ram_tab = "[||||||||||||||||||]"

        if swap_percent < 5:
            swap_tab = "[                  ]"
        elif swap_percent < 15:
            swap_tab = "[|                 ]"
        elif swap_percent < 35:
            swap_tab = "[|||||             ]"
        elif swap_percent < 50:
            swap_tab = "[|||||||||         ]"
        elif swap_percent < 80:
            swap_tab = "[|||||||||||||     ]"
        else:
            swap_tab = "[||||||||||||||||||]"



        os.system("clear")
        print(f'CPU: {cpu}%\n{cpu_tab}')
        print(f'    Current: {freq_current:.1f}MHz\n    Minimum: {freq_minimum:.2f}MHz \n    Maximum: {freq_maximum:.2f}MHz\n')
        print(f'RAM: {ram_percent:.1f}% \n{ram_tab}\n    Used: {ram_used / 1024 / 1024 / 1024:.2f} GB \n    Available: {ram.available / 1024 / 1024 / 1024:.2f} GB \n    Total {ram.total / 1024 / 1024 / 1024:.4} GB')
        print(f'\nSWAP: {swap_percent}% \n{swap_tab}\n    Used: {swap_used / 1024 / 1024 / 1024:.2f} GB \n    Available: {swap_free / 1024 / 1024 / 1024:.2f} GB \n    Total {swap_total / 1024 / 1024 / 1024:.4} GB')
        time.sleep(1)
if __name__ == "__main__":
    main()
