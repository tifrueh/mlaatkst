# MLA at KST

This application was specifically designed to help students of the KST get their footnotes right. The student can input all attributes of the work they want to cite into the entry fields and the program spits out the correct footnote which then can be copied.
The program was originally in German, but since the release of v1.2.0 the user can change the language to English in the settings menu.

NOTE: The app is currently only tested on macOS 11, Apple Silicon.

## Installation

I'm trying to make installation as easy as possible, but it is still far from perfect. So bear with me while I try to implement something better than this.
But in the moment there are three major ways for installation: download from .zip, build from source with pyinstaller, build from source by yourself.
Downloading is probably the easiest for most, but there are also instructions for building with pyinstaller below.

### Download

1.  Go to the [latest release](https://github.com/Timo-Frueh/mlaatkst/releases/latest) and download the correct version for your system:
    
    - macOS: `MLAatKST-macOS-universal-(version).zip`
    
    - Windows: There is no version for Windows yet, but I'll add that in the future.

2.  Open the ZIP-archive and move the application to your Applications folder (usually `/Applications`)

3.  _Disclaimer: I do not have a developer certificate, so Gatekeeper won't let you open the app._
    But if you trust me, you can run the following command in your terminal:
    ~~~ shell
    xattr -d com.apple.quarantine /Applications/MLAatKST.app
    ~~~

4.  You should then be able to open and use the app.

### Installation with pyinstaller

I'm assuming that most students are not familiar with building python applications, which is why I will provide detailed instructions on how to do that here.

NOTE: I have not tried this on Windows yet, so I can't tell you how to do this whole thing there, but as soon as I have done my first build there I'll add instructions for that.

_If you already have python 3.9.7 installed, jump directly to 3.
If you already have python 3.9.7 and pyinstaller installed, jump directly to 5._

1.  Download python 3.9.7 for your OS. [Here](https://www.python.org/downloads/release/python-397) is a link to the official download page.
    You will need to scroll down until you see a table containing downloads and then choose the correct one for your system:

    - Mac with Intel architecture: macOS 64-bit Intel installer
    - Mac with Apple Silicon: macOS 64-bit universal2 installer
    - not sure: macOS 64-bit universal2 installer

2.  Open the installer and follow its instructions.

3.  Open Terminal.app, which is located in your Launchpad in "Other".

4.  Use pip to install pyinstaller and all needed requirements. Input the following command into your terminal and press enter:
    ``` bash
    pip3 install pyinstaller clipboard
    ```

5.  Download the source of the [latest release](https://github.com/Timo-Frueh/mlaatkst/releases/latest) by clicking on "Source Code (zip)".

6.  Unzip the archive and save the folder it contains to somewhere you have access to and will find it again later.

7.  Right-click the folder and select "New Terminal tab here".

8.  A terminal tab should open. Now input the following command and press enter:
    ``` bash
    bash install.sh
    ```

9.  You should now see a folder named "out". Open it.

10. Open its subfolder "dist".

11. Move "MLAatKST.app" into your Application directory.

### Manual install (macOS, Linux, Windows)

You can also just download the source code and always run the app directly or use some installer of your own to convert the source into an executable.

## Preview

![App preview](https://github.com/Timo-Frueh/mlaatkst/blob/17753bb75811a1b21cbc0a4d173e73666c924e0a/assets/preview_de.png "Preview")
