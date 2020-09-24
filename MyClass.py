class MyClass:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = {'a' : file_name}

    def create_cpp(self):
        content = '#include "{a}.hpp"\n\n{a}::{a}()\n{{\n}}\n{a}::{a}({a} const& to_copy)\n{{\n\t*this = to_copy;\n}}\n{a}& {a}::operator=({a} const& to_copy)\n{{\n}}\n{a}::~{a}()\n{{\n}}\n'.format(**self.data)
        f = open('{}.cpp'.format(self.file_name), "w+")
        f.write(content)
        f.close()

    def create_hpp(self):
        content = 'class {a}\n{{\nprivate:\npublic:\n\t{a}();\n\t{a}({a} const& to_copy);\n\t~{a}();\n\t{a}& operator=({a} const& to_copy);\n}};\n'.format(**self.data)
        f = open('{}.hpp'.format(self.file_name), "w+")
        f.write(content)
        f.close()
