from conan import ConanFile

class Conversation(ConanFile):
    generators = ("CMakeToolchain", "CMakeDeps")
    settings = ("os", "build_type", "arch", "compiler")

    def requirements(self):
        self.requires("freeimage/3.18.0")

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.4]")

    def layout(self):
        self.folders.generators = ""
