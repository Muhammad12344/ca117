class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{} {} {}".format(self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self, d={}):
        self.d = {}

    def add_contact(self, c):
        self.d[c.name] = c

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        try:
            return self.d[name]
        except:
            return None

    def __str__(self):
        slist = []
        for k, v in sorted(self.d.items()):
            slist.append("{}".format(v))

        return "Contact list" + "\n" + "-" * 12 + "\n" + "\n".join(slist)
