from conan import ConanFile

class Conversation(ConanFile):
    generators = ("CMakeToolchain", "CMakeDeps")
    settings = ("os", "build_type", "arch")

    def requirements(self):
        self.requires("freeimage/3.18.0")

    def build_requirements(self):
        self.tool_requires("cmake/[>=4.0.3]")

    def configure(self):
        self.options["freeimage/*"].shared = False

    def layout(self):
        self.folders.generators = ""
