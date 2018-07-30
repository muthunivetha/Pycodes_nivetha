name = raw_input("enter a name: ")

animal = raw_input("enter an animal: ")
adj1 = raw_input("enter an adjective: ")
verb1 = raw_input("enter a verb: ")
adj2 = raw_input("enter 2nd adjective: ")
adj3 = raw_input("enter 3rd adjective: ")

fruit = raw_input("enter a fruit: ")
country = raw_input("Enter a country")


story = "One day a small brown %s named %s was %s slowly through the woods. He was %s because he had lost his soft teddy.He lost it yesterday when he was %s quickly through the dark wood. He had been %s over small stones, big logs and wet puddles. he likes %s a lot.He lives in %s. "

print story % (animal,name,adj1,verb1,adj2,adj3,fruit,country)

