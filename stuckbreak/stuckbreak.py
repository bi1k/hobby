#!/usr/bin/python3

import argparse
import csv
import os
import random
import time


class Activity:
    def __init__(self, name, category, load, dependent=""):
        self.name = name
        self.category = category
        self.load = load
        self.dependent = dependent


parser = argparse.ArgumentParser()
parser.add_argument('-c', metavar='<category>', type=str.lower,
                    help='the category or categories of activities to include in the selection process', nargs='+')
parser.add_argument('-f', metavar='<filename>', type=str,
                    help='the location of the csv file containing the activities')
parser.add_argument('-t', metavar='<template>', type=str.lower,
                    help='the template to use for importing activities to randomize. "1" uses a specific csv template. '
                         '"2" will prompt you to enter activities manually. "3" uses a csv where activities are '
                         'populated in the first column (without a header).')


def handle_error(line, error, num):
    num += 1
    print("Issue reading line. '{}' - {}".format(line, error))
    return "\nNote: One or more activities were omitted due to errors.\n" \
           "Total number of errors: {}\n" \
           "Last error that occurred: '{}' - {}".format(num, line, error), num


csv_location = ''  # default file location if none is specified

pool = []  # list containing randomized Activity objects
pool_size = 100  # number of Activity objects in the pool
error_count = 0  # tally of errors that will be displayed at the end of the program
line_error = ""  # variable for errors that will be displayed at the end of the program
arrow_position = 5  # how far down the arrow sits when an Activity is selected
default_template = 1  # if a template isn't specified with -t, use this
args = parser.parse_args()  # used for accessing program options
rand_spin_duration = random.randint(9, 11)  # minimum and maximum seconds for a roll to occur

if not args.t:
    args.t = str(default_template)  # set default template if none is specified
if args.t != "1" and args.t != "2" and args.t != "3":
    print("Invalid template entered: '{}'. Use the -h option to see templates that can be used.".format(args.t))
    exit()
if os.name == "nt":
    clear_screen = "cls"
else:
    clear_screen = "clear"

if args.t != "2":  # try and import activities from the specified csv file.
    if args.f:
        csv_location = args.f
    try:
        with open(csv_location) as fi:
            csv_file = csv.reader(fi)
            next(csv_file, None)    # skip headers
            if args.t == "1":       # attempt to convert the csv rows into Activity objects
                activities = {}
                for row in csv_file:
                    try:
                        if not args.c or row[1].lower() in args.c:
                            activities[row[0]] = Activity(row[0], row[1].lower(), int(row[2]), row[3])
                    except Exception as e:
                        line_error, error_count = handle_error(row, e, error_count)
                # prevents activities that have active dependencies from being added to the pool
                for act_key, act_val in activities.items():
                    if act_val.dependent not in activities.keys():
                        for x in range(activities[act_key].load):
                            pool.append(activities[act_key])
            else:  # add csv rows into pool
                for row in csv_file:
                    try:
                        pool.append(row[0])
                    except Exception as e:
                        line_error, error_count = handle_error(row, e, error_count)
    except Exception as e:
        print("Issue reading file. {}".format(e))
        exit()
else:  # manually add activities into the pool
    options = input(
        "Enter the options you want to pick from. Ensure they are separated by commas e.g., option a,"
        "option b,option c\n")
    pool = options.split(",")

if len(set(pool)) < 2:  # if there aren't enough options to choose from, exit the program
    print("Either only one or no options were available for selection.\n")
    exit()

if pool:
    # if the number of elements in the pool is less than "pool size", the while loop will duplicate elements in the pool
    while len(pool) < pool_size:
        for x in range(len(pool)):
            pool.append(pool[x])
    random.shuffle(pool)
    for x in range(0, pool_size):  # start the selection process
        os.system(clear_screen)
        print("Picking your next activity...\n")
        for y in range(1, 11):
            if args.t == "1":
                pool_item = pool[(x + y % pool_size) % pool_size].name
            else:
                pool_item = pool[(x + y % pool_size) % pool_size]
            if y != arrow_position:
                print("     {}".format(pool_item))
            else:
                print("---> {}".format(pool_item))
        time.sleep((x / 100) ** rand_spin_duration + 0.02)  # time delay to simulate a spinning wheel effect
    time.sleep(3)  # time delay before chosen option is shown
    os.system(clear_screen)
    if args.t == "1":
        print("Activity selected!\n\n{}\n{}"
              .format(pool[arrow_position - 1].name, line_error))
    else:
        print("Activity selected!\n\n{}\n{}"
              .format(pool[arrow_position - 1], line_error))
elif args.t == "1" and args.c:
    print("The category entered didn't match any activity categories.\n")
else:
    print("Error importing activities.\n")
