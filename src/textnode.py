class TextNode:
    # text = the text content of the node
    # text_type = the type of text this node contains, which is just a string like "bold" or "italic"
    # url = the URL of the link or image, if the text is a link, defaulted to None if nothing is passed in 
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url