import argparse
import json
import relationships
import sys
"""Find the relationship between two people

Returns:
    str: A statement that indicates the relationship between two people
"""

class Person:
    """Creates a person object and methods for that object
    
    Attributes:
        name (str): The name of the person
        gender (str): The gender of the person
        parents (list of Person): A list of the person's parents. Default value is an empty list
        spouse (Person): A Person object that is the spouse of the person. Default value is None
        
    Methods:
        add_parent(Person): Takes in a Person object and adds it to the attribute parents
        set_spouse(Person): Takes in a Person object and sets it to be the spouse
        connections(): Create a dictionary of all the connections between the person and the rest of the family
        relation_to(Person): Takes in a Person object and names the relationship between self and the object
    """
    
    def __init__(self, name, gender):
        """Create a Person object

        Args:
            name (str): Name of the person
            gender (str): Gender of the person
            
        Side effects:
            Creates a Person object
        """
        self.name = name
        self.gender = gender
        self.parents = []
        self.spouse = None
        
    def add_parent(self, parent):
        """Adds a parent to the Person's parent attribute

        Args:
            parent (Person): A Person object that describes the parent
            
        Side effects:
            Changes the self.parents attribute
        """
        self.parents.append(parent)
        
    def set_spouse(self, spouse):
        """Adds a spouse to the Person's spouse attribute

        Args:
            spouse (Person): A Person object that describes the spouse    
        
        Side effects:
            Changes the self.spouse attribute
        """
        self.spouse = spouse
        
    def connections(self):
        """Create a dictionary of all the connections between the person and the rest of the family

        Returns:
            dictionary: A dictionary of all the relationships between self and the other family members
        """
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
            if ("S" not in personpath) and not(currentp.spouse == None) and (cdict.get(currentp.spouse, None) == None):
                spou = currentp.spouse
                cdict[spou] = personpath + "S"
                queue.append(spou)
        return cdict
    
    def relation_to(self, person):
        """Takes in a Person object and names the relationship between self and the object

        Args:
            person (Person): The other person who you are trying to determine a relationship to

        Returns:
            str: The relationship between self and the other Person object
        """
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
            #Uses Lambda key to sort the list of common people by length of their path and find the shortest
            close = min(common, key = lambda d: len(dictself[d] + ":" + dicto[d]))
            #Use KeyError exception to define a distant relative
            try:
                 # pull the dictionary of relationship to this person
                relation = relationships.relationships[dictself[close] + ":" + dicto[close]][self.gender]
                return relation
            except (KeyError):
                return "distant relative"

class Family:
    """Creates a Family object and methods for the object
    
    Attributes:
        people (dictionary of Person): A dictionary of all the family members
        
    Methods:
        relation(Person, Person): Finds the relationship between two people
    """
    
    def __init__(self, famdict):
        """Create a Family object

        Args:
            famdict (dictionary of Person): A dictionary of Person objects as the values for a dictionary of family members
            
        Side effects:
            Create a Family object
        """
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
            self.people[sp1].set_spouse(self.people[sp2])
            self.people[sp2].set_spouse(self.people[sp1])
            
    def relation(self, person1, person2):
        """Find the relationship between two people

        Args:
            person1 (Person): The first person in the relationship
            person2 (Person): The second person in the relationship

        Returns:
            str: A string describing the relationship between person1 and person2
        """
        return self.people[person1].relation_to(self.people[person2])
    
def main(filepath, name1, name2):
    """Completes a series of commands to create Family and Person objects, then find a relationship

    Args:
        filepath (str): The path to where the family data is stored
        name1 (str): The name of the first person in the relationship
        name2 (str): The name of the second person in the relationship
    
    Side effects:
        Prints statements that describe the relationship between the two people named
    """
    with open(filepath, "r", encoding="utf-8") as f:
        familydata = json.load(f)
        fam = Family(familydata)
        relative = fam.relation(name1, name2)
        if relative == None:
            print(f"{name1} is not related to {name2}")
        else:
            print(f"{name1} is {name2}'s {relative}")

def parse_args(comline):
    """Parses the command line argument

    Args:
        comline (list of str): A command line argument

    Returns:
        namespace: an object with three attributes, filepath, name1, and name2, all containing a string.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath",
                        help="the path to the file containing family data")
    parser.add_argument("name1",
                        help="the name of the first person who you are trying to determine a relationship for")
    parser.add_argument("name2",
                        help="the name of the second part who you are trying to determine a relationship for")
    parsed = parser.parse_args(comline)
    return parsed

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.name1, args.name2)