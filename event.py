import re

class Event:
    def __init__(self, title, description, start, end, location):
        """
            Hold all data for one lecture
        """
        self.title = self.sanitize(title)
        self.description = self.sanitize(description)
        self.start = start
        self.end = end
        self.location = self.sanitize(location)

        difference = end - start
        self.duration = int((difference.days * (24 * 60 * 60) + difference.seconds) / 3600) + 1

    def sanitize(self, text):
        """
            Special character lead to problems with tikz
        """
        text = re.sub(r'http[s]?:\/\/','', text)
        text = text.replace('/', '')
        text = text.replace('.', '')
        text = text.replace(')', '')
        text = text.replace('(', '')
        text = text.replace('ö', 'oe').replace('Ö', 'Oe')
        text = text.replace('ü', 'ue').replace('Ü', 'Ue')
        text = text.replace('ä', 'ae').replace('Ä', 'Ae')

        return text.strip()
