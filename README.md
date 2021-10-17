# MLA at KST

This application was specifically designed to help students of the KST get their footnotes right. The student can input all attributes of the work they want to cite into the entry fields and the program spits out the correct footnote which then can be copied.
The program was originally in German, but since the release of v1.2.0 the user can change the language to English in the settings menu.

NOTE: The app is currently only tested on macOS 11, Apple Silicon.

## Installation

I'm assuming that most students are not familiar with building python applications, which is why I will provide detailed instructions on how to do that here.

NOTE: I have not tried this on Windows yet, so I won't tell you how to do that, but as soon as I have done my first build on Windows I'll add instructions for that.

### Installation with pyinstaller

_This is the main option for installing the app in the moment.
If you already have python 3.9.7 installed, jump directly to 3.
If you already have python 3.9.7 and pyinstaller installed, jump directly to 5._

1.  Download python 3.9.7 for your OS. [Here](https://www.python.org/downloads/release/python-397) is a link to the official download page.
    You will need to scroll down until you see a table containing downloads and then choose the correct one for your system:

    - Mac with Intel architecture: macOS 64-bit Intel installer
    - Mac with Apple Silicon: macOS 64-bit universal2 installer
    - not sure: macOS 64-bit universal2 installer

2.  Open the installer and follow its instructions.

3.  Open Terminal.app, which is located in your Launchpad in "Other" (open CMD in Windows).

4.  Use pip to install pyinstaller and all needed requirements. Input the following command into your terminal:
    ``` bash
    pip3 install pyinstaller clipboard
    ```

5.  Download the source of the [latest release](https://github.com/Timo-Frueh/mlaatkst/releases/latest) by clicking on (Source Code (zip)).

6.  Unzip the archive and save the folder it contains to somewhere you have access to and will find it again later.

7.  Open the folder prevously unzipped and run "install.sh" by double clicking it.

8.  You should now see a folder named "out". Open it.

9.  Open its subfolder "dist".

10. Move "MLAatKST.app" into your Application directory.

### Manual install (macOS, Linux, Windows)

You can also just download the source code and always run the app directly or use some installer of your own to convert the source into an executable.

## Preview

<img width="812" alt="App preview" src="https://user-images.githubusercontent.com/84284672/136099397-e57edd3b-f5a7-407c-be04-33a03d6d8a70.png">
