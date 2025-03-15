from textnode import TextNode, TextType



def main():
    dummy = "This is a dummy test line"
    ital = TextType.ITALIC
    node = TextNode(dummy, ital, None)
    print(node)

main()
