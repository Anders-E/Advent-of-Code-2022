from dataclasses import dataclass
from sys import stdin

# Day 07

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = {}
        self.dirs = {}
        self.parent = parent
        self.size = None

    def add_dir(self, name):
        self.dirs[name] = Directory(name, self)

    def get_size(self):
        self.size = self.size or sum(self.files.values()) + sum([dir.get_size() for dir in self.dirs.values()])
        return self.size

    def sum_all_below_size(self, n):
        if self.get_size() < n:
            return self.get_size() + sum([dir.sum_all_below_size(n) for dir in self.dirs.values()])
        else:
            return sum([dir.sum_all_below_size(n) for dir in self.dirs.values()])

    def smallest_geq_size(self, n):
        return min(
            [self.get_size(), 
            *[dir.smallest_geq_size(n) for dir in self.dirs.values() if dir.get_size() > n]]
        )

@dataclass
class Command:
    name: str
    arg: str | None

@dataclass
class File:
    name: str
    size: int

def star1(lines):
    root = build_file_system(lines)
    return root.sum_all_below_size(100001)

def star2(lines):
    TOTAL_DISK_SPACE = 70000000
    FREE_DISK_SPACE_NEEDED = 30000000
    root = build_file_system(lines)
    free_disk_space = TOTAL_DISK_SPACE - root.get_size() 
    disk_space_needed_to_free = FREE_DISK_SPACE_NEEDED - free_disk_space
    return root.smallest_geq_size(disk_space_needed_to_free)

def build_file_system(lines):
    first_dir_name = lines[0].split(" ")[-1]
    root = Directory(first_dir_name)
    wd = root
    lines = lines[1:]
    for line in lines:
        args = line.split(" ")
        if args[0] == "$":
            if args[1] == "cd":
                name = args[2]
                if name == "..":
                    wd = wd.parent or Directory("/", None)
                else:
                    wd.dirs[name] = wd.dirs.get(name, Directory(name, wd))
                    wd = wd.dirs[name]
        elif args[0].isnumeric():
            name = args[1]
            size = int(args[0])
            wd.files[name] = size
        else:
            name = args[1]
            wd.add_dir(name)
    return root

### Input etc.

lines = [line.rstrip() for line in stdin.readlines()]
print(f"07_1: {star1(lines)}")
print(f"07_2: {star2(lines)}")
