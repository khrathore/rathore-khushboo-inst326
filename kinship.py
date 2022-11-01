import argparse
import json
import relationships
import sys

class Person:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.parents = []
        self.spouse = None
        
    def add_parent(self, parent):
        self.parents.append(parent)
        
    def set_spouse(self, spouse):
        self.spouse = spouse
        
    def connections(self):
        # Instantiate the cdict and queue
        cdict = {self:""}
        queue = [self]
        # While loop for the queue
        while len(queue) > 0:
            # Pop the first person off the queue
            currentp = queue.pop(0)
            personpath = cdict[currentp]
            # Look up the parents of the current person
            for par in currentp.parents:
                if cdict.get(par,0) == 0:
                    # Edit the parent's path
                    cdict[par] = personpath + "P"
                    queue.append(par)
            # Look up the spouse of the current person and see if certain conditions are fulfilled
            if currentp.spouse and not("S" in personpath) and (cdict.get(currentp.spouse, 0) == 0):
                spou = currentp.spouse
                cdict[spou] = personpath + "S"
                queue.append[spou]
        return cdict
    
    def relation_to(self, person):
        # Pull and create the dictionaries
        dictself = self.connections()
        dicto = person.connections()
        # Convert the dictionaries to sets
        setsel = set(dictself)
        seto = set(dicto)
        # Intersection of both sets
        common = seto & setsel
        # If the set common is empty, return None
        if not(common):
            return None
        # If it is not empty, proceed
        else:
            #Lambda key to sort the list of common people by length of their path
            sorted(common, key = lambda d: len(dictself[d] + ":" + dicto[d]))
            # grab the common person with the shortest length
            closest = list(common)[0]
            # pull the dictionary of relationship to this person
            relation = relationships.relationships[dictself[closest] + ":" + dicto[closest]][self.gender]
            # if there is no relationship, return distant relative
            if relation == None:
                return "distant relative"
            #return the relationship if it does exist
            return relation

class Family:
    
    def __init__(self, famdict):
        # Create an empty dictionary of people
        self.people = {}
        # Loop through the given dictionary's individuals key and create object for each individual
        for ind in famdict["individuals"]:
            person = Person(ind, famdict["individuals"][ind])
            self.people[ind] = person
        # Loop through the given dictionary's parents key and add parents for each individual
        for perpar in famdict["parents"]:
            (p1, p2) = famdict["parents"][perpar]
            self.people[perpar].add_parent(self.people[p1])
            self.people[perpar].add_parent(self.people[p2])
        # Loop through the given dictionary's couples key and set spouses for each individual
        for coup in famdict["couples"]:
            (sp1, sp2) = coup
            self.people[sp1].set_spouse(self.people[sp1])
            self.people[sp2].set_spouse(self.people[sp1])
            
    def relation(self, person1, person2):
        return self.people[person1].relation_to(self.people[person2])
    
def main(filepath, name1, name2):
    with open(filepath, "r", encoding="utf-8") as f:
        familydata = json.load(f)
        fam = Family(familydata)
        relative = fam.relation(name1, name2)
        if relative == None:
            print(f"{name1} is not related to {name2}")
        else:
            print(f"{name1} is {name2}'s {relative}")

def parse_args(comline):
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path",
                        help="the path to the file containing family data")
    parser.add_argument("name1",
                        help="the name of the first person who you are trying to determine a relationship for")
    parser.add_argument("name2",
                        help="the name of the second part who you are trying to determine a relationship for")
    parsed = parser.parse_args(comline)
    return parsed

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file_path, args.name1, args.name2)