from conans import ConanFile


class RxcppConan(ConanFile):
    name = "rxcpp"
    version = "0.0.2"
    license = "MIT"
    url = "https://github.com/vthiery/conan-rxcpp.git"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    settings = None

    def source(self):
        self.run("git clone --recursive https://github.com/Reactive-Extensions/RxCpp.git")

    def build(self):
        del self

    def package(self):
        self.copy("*.hpp", dst="include", src="RxCpp/Rx/v2/src/rxcpp", keep_path=True)
        self.copy("*.hpp", dst="include", src="RxCpp/Rx/v2/src/rxcpp/operators", keep_path=True)
