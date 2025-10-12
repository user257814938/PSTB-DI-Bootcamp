import math   # pour arrondir le nombre total de pages

# etape 1: Create the Pagination class
class Pagination:
    def __init__(self, items=None, page_size=10):
        # initialise la liste d’éléments
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0                            # page courante (index 0-based)
        # nombre total de pages (arrondi vers le haut)
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # etape 3: méthode pour récupérer les éléments visibles de la page courante
    def get_visible_items(self):
        start = self.current_idx * self.page_size        # début du slice
        end = start + self.page_size                     # fin du slice
        return self.items[start:end]

    # etape 4: navigation
    def go_to_page(self, page_num):
        # vérifie que le numéro de page est valide
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Invalid page number: {page_num}")
        # ajuste l’index interne (0-based)
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # etape 5: méthode spéciale pour afficher les éléments visibles
    def __str__(self):
        visible = self.get_visible_items()
        return "\n".join(visible) if visible else "(no items)"
