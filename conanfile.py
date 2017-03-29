from conans import ConanFile


class RxcppConan(ConanFile):
    name = "rxcpp"
    version = "0.0.1"
    license = "MIT"
    url = "https://github.com/vthiery/rxcpp.git"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    settings = None

    def source(self):
        self.run("git clone --recursive https://github.com/Reactive-Extensions/RxCpp.git")

    def build(self):
        del self

    def package(self):
        self.copy("*.hpp", dst="include", src="RxCpp/Rx/v2/src/rxcpp", keep_path=True)
