class TreeNode:
    def __init__(self, title, page_link):
        self.title = title
        self.page_link = page_link
        self.child_links = []

    def add_links(self, links):
        self.child_links = links
