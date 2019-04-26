from conans import ConanFile, tools
import os

class NanoSVGConan(ConanFile):
    name = "NanoSVG"
    version = "master"
    license = "Zlib"
    author = "Mikko Mononen"
    url = "https://github.com/qno/conan-nanosvg"
    description = "Simple stupid SVG parser."

    no_copy_source = True

    _pkg_name = "nanosvg-master"

    def source(self):
        url = "https://github.com/memononen/nanosvg/archive/master.zip"
        self.output.info("Downloading {}".format(url))
        tools.get(url)

    def package(self):
        self.copy("*.h", dst="include", src="{}{}src".format(self._pkg_name, os.sep))

    def package_id(self):
        self.info.header_only()
