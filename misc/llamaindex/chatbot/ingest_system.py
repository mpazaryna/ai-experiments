from ingest import KnowledgeBaseConstructor


class MyClass:
    def __init__(self):
        # Constructor code here
        self.kb_constructor = KnowledgeBaseConstructor()

    def some_method(self):
        # Method code here
        self.kb_constructor.construct_base_from_directory("data")


# Create an instance of MyClass and call the desired method
my_object = MyClass()
my_object.some_method()
