class node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class CommandHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_command = None
        self.locked = False
        self.locked_by = None

    def add_command(self, command):
        if self.locked:
            print("L'historique est verrouillé. Impossible d'ajouter une commande.")
            return

        new_node = node(command)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.current_command = self.tail

    def last_command(self):
        if self.locked:
            print("L'historique est verrouillé. Impossible d'afficher la dernière commande.")
            return

        if self.current_command:
            return self.current_command.data
        return None

    def user_commands(self, user):
        if self.locked:
            print("L'historique est verrouillé. Impossible d'afficher les commandes d'un utilisateur.")
            return

        commands = []
        current = self.head

        while current:
            if current.data['user'] == user:
                commands.append(current.data['command'])
            current = current.next

        return commands

    def move_forward(self):
        if self.locked:
            print("L'historique est verrouillé. Impossible de se déplacer dans l'historique.")
            return

        if self.current_command and self.current_command.next:
            self.current_command = self.current_command.next

    def move_backward(self):
        if self.locked:
            print("L'historique est verrouillé. Impossible de se déplacer dans l'historique.")
            return

        if self.current_command and self.current_command.prev:
            self.current_command = self.current_command.prev

    def clear_history(self):
        if self.locked:
            print("L'historique est verrouillé. Impossible de vider l'historique.")
            return

        self.head = None
        self.tail = None
        self.current_command = None

    def lock_history(self, user):
        if self.locked:
            print("L'historique est déjà verrouillé.")
            return

        self.locked = True
        self.locked_by = user
        print(f"L'historique a été verrouillé par {user}.")

    def unlock_history(self, user):
        if not self.locked:
            print("L'historique n'est pas verrouillé.")
            return

        if self.locked_by != user:
            print("Vous n'êtes pas autorisé à déverrouiller l'historique.")
            return

        self.locked = False
        self.locked_by = None
        print("L'historique a été déverrouillé.")

