# MLA at KST

This application was specifically designed to help students of the KST get their footnotes right. The student can input all attributes of the work they want to cite into the entry fields and the program spits out the correct footnote which then can be copied.
The program was originally in German, but since the release of v1.2.0 the user can change the language to English in the settings menu.

NOTE: The app is currently only tested on macOS and the installer script as well as the direct downloads are only available on macOS (and Linux maybe). But I'll add support for Windows soon.

## Installation

The app can be installed in three different ways:

### Script install (macOS)

For installation from source use the installation script ([pyinstaller](https://www.pyinstaller.org/) needs to be installed for this). The bundle will be located at ./out/dist/ after the execution of the script.

### Download of .dmg or .zip (macOS)

Alternatively you can download the .dmg (or .zip) file directly from the latest release. The .dmg should show the app and a shortcut to the application's folder, so that you can drag it over, while the .zip only contains the app itself.

NOTE: I do not have any developer certificate, so macOS won't open the program if it is not built from source. But if you trust me, you can run:

``` Shell
xattr -d com.apple.quarantine /Applications/MLAatKST.app
```

This should resolve the issue. I might do something about that in the future, but until then you'll just have to go with that.

### Manual install (macOS, Linux, Windows)

Lastly you can also just download the source code and always run the app directly or use some installer of your own to convert the source into an executable.

## Preview

<img width="812" alt="App preview" src="https://user-images.githubusercontent.com/84284672/136099397-e57edd3b-f5a7-407c-be04-33a03d6d8a70.png">
