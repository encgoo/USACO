#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_non_constrains(all_cows, constraints):
    no_contraints = []
    for cow in all_cows:
        no_in_contraints = True
        for constraint in constraints:
            if cow in constraint:
                no_in_contraints = False

        if no_in_contraints:
            no_contraints.append(cow)
    return no_contraints


def combine_contraints(constraints):
    combined = []
    for constraint in constraints:
        added = False
        for c in combined:
            if c[0] == constraint[0]:
                c.insert(0, constraint[1])
                added = True
            elif c[0] == constraint[1]:
                c.insert(0, constraint[0])
                added = True
            elif c[-1] == constraint[0]:
                c.append(constraint[1])
                added = True
            elif c[-1] == constraint[1]:
                c.append(constraint[0])
                added = True
            if c[0] > c[-1]:
                c.reverse()

        if not added:
            if constraint[0] > constraint[-1]:
                constraint.reverse()
            combined.append(constraint)

    return combined


def get_sequence(all_cows, constraints):
    sequence = []

    no_contraints = get_non_constrains(all_cows, constraints)
    no_contraints.sort()

    print("no constrainted: {}".format(no_contraints))

    combined = combine_contraints(constraints)
    combined.sort(key=lambda u: u[0])

    print("Combined: {}".format(combined))

    pCow = 0
    pConstraint = 0
    while pCow < len(no_contraints) and pConstraint < len(combined):
        if no_contraints[pCow] < combined[pConstraint][0]:
            sequence.append(no_contraints[pCow])
            pCow += 1
        else:
            sequence.extend(combined[pConstraint])
            pConstraint += 1

    sequence.extend(no_contraints[pCow:])
    for pc in range(pConstraint, len(combined)):
        sequence.extend(combined[pc])

    return sequence


if __name__ == "__main__":
    all_cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Betsy", "Sue"]

    constraints = [["Buttercup", "Bella"],
                   ["Blue", "Bella"],
                   ["Sue", "Beatrice"]]

    sequence = get_sequence(all_cows, constraints)
    for cow in sequence:
        print(cow)
