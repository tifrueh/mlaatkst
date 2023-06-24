# MLA at KST

This application was specifically designed to help students of the KST get their footnotes right. The student can input all attributes of the work they want to quote into the input fields and the program spits out the correct footnote which can then be copied.

## Installation

I'm trying to make installation as easy as possible, but it is still far from perfect. So bear with me while I try to implement something better than this.
But in the moment there are three major ways for installation: 

1. [download as PKG](#download-pkg-macos) (macOS)
2. [use homebrew](#installation-with-homebrew-macos) (macOS)
4. [build from source by yourself](#manual-install-any-os) (any OS)

### Download PKG (macOS)

1. Go to the [latest release](https://github.com/tifrueh/mlaatkst/releases/latest) and download `MLAatKST-macOS-universal-(version).pkg`.

2. Right-click the PKG and click 'open'.

3. Follow the PKG-Installer's instructions.

4.  _Disclaimer: I do not yet have a developer certificate, so Gatekeeper won't let you open the app._
    But if you trust me, you can run the following command in your terminal:
    ~~~ shell
    xattr -d com.apple.quarantine /Applications/MLAatKST.app
    ~~~

5. You should then be able to open and use the app.

### Installation with homebrew (macOS)

1.  Tap my homebrew tap:

    ~~~ shell
    brew tap tifrueh/homebrew-mytap
    ~~~

2.  Install MLAatKST (with the `--no-quarantine` flag, because I don't have a developer certificate):

    ~~~ shell
    brew install mlaatkst --no-quarantine
    ~~~

### Manual install (any OS)

You can also download the source code from the [latest release](https://github.com/tifrueh/mlaatkst/releases/latest) and compile it manually.
Additional software components needed:
- [meson](https://mesonbuild.com/SimpleStart.html)
- [wxWidgets](https://www.wxwidgets.org/downloads/) 
