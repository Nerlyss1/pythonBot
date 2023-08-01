class Node:
    def __init__(self, question, answers=None, next_nodes=None):
        self.question = question
        self.answers = answers or []
        self.next_nodes = next_nodes or {}

    def add_answer(self, answer, next_node):
        self.answers.append(answer)
        self.next_nodes[answer] = next_node

class Tree:
    def __init__(self, root_node):
        self.current_node = root_node

    def ask_question(self):
        return self.current_node.question

    def handle_answer(self, answer):
        if answer in self.current_node.next_nodes:
            self.current_node = self.current_node.next_nodes[answer]
            return self.ask_question()
        else:
            return "Je n'ai pas compris votre réponse. Pouvez-vous réessayer ?"

    def reset(self):
        self.current_node = root_node

    def speak_about(self, topic):
        queue = [self.current_node]
        visited = set()

        while queue:
            node = queue.pop(0)
            visited.add(node)

            if topic in node.question.lower():
                return True

            queue += [next_node for next_node in node.next_nodes.values() if next_node not in visited]

        return False


root_node = Node("Bonjour, comment puis-je vous aider ?")
topic_node = Node("Parlons de Python. Que voulez-vous savoir sur ce sujet ?", ["Les boucles", "Les fonctions"])
loop_node = Node("Les boucles en Python. Quel type de boucle voulez-vous apprendre ?", ["For", "While"])
for_node = Node("La boucle for en Python permet de répéter une opération sur chaque élément d'une séquence. Parlez-vous de la syntaxe ou de son fonctionnement ?", ["Syntaxe", "Fonctionnement"])

root_node.add_answer("Parlons de Python", topic_node)
topic_node.add_answer("Les boucles", loop_node)
loop_node.add_answer("For", for_node)


tree = Tree(root_node)

while True:
    user_input = input(tree.ask_question() + " ")

    if user_input.lower() == "help":
        print("Je suis là pour vous aider. Posez-moi vos questions sur Python ou demandez-moi de parler d'un sujet en particulier en disant 'speak about X'. Si vous voulez recommencer la discussion, dites 'reset'.")
        continue

    if user_input.lower() == "reset":
        tree.reset()
        continue

    if user_input.lower().startswith("speak about "):
        topic = user_input.split("speak about ")[1]
        if tree.speak_about(topic):
            print("Oui, je peux vous parler de", topic)
        else:
            print("Désolé, je ne peux pas vous parler de", topic)
        continue

    response = tree.handle_answer(user_input)
    print(response)
