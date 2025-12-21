# Configuring command-line tools settings

**Framework**: Xcode

Select the version of Xcode you want to use for command-line tools, in either Xcode settings or Terminal.

#### Overview

If you have multiple versions of Xcode on your Mac, you can select a specific version of the app to use for command-line tools. For example, you might want to release your app with the latest version of Xcode, while using a beta version to try out new APIs.

You can do this by selecting a default Xcode version to use for command-line tools in Xcode settings, or you can set it from the command line. To apply the change to every user account on your Mac, use either Xcode settings or the command line. To apply the change to the current shell session only, use the command line.

> **Note**: To use the commands from the Command Line Tools for Xcode package, select the package after installing. For more information, see [`Installing the command-line tools`](installing-the-command-line-tools.md).

##### Check the Default Xcode App for Command Line Tools

To identify the default Xcode app for command-line tools, choose Xcode > Settings, and click Locations in the sidebar. The Command Line Tools section of the Locations pane displays both the Xcode version number and the location of the file. ![A screenshot of the Locations pane in Xcode settings, showing the Archives, Compilation Cache (Automatic size), Command Line Tools, and Custom Paths sections.](https://docs-assets.developer.apple.com/published/bc68aec7bdaba2c786d88b04b05f4cc1/configuring-command-line-tools-settings-01%402x.png)

Alternatively, you can identify the Xcode version from the command line. Enter `xcode-select` with the `--print-path` option in Terminal. This command returns the path of the active developer directory for Xcode. For example, the following command prints the path of the developer directory containing a version of Xcode:

```None
% xcode-select --print-path
/Applications/Xcode.app/Contents/Developer
```

If you install the Command Line Tools for Xcode package and set it as the active directory, the command `xcode-select --print-path` returns the package path, like in the following example:

```None
% xcode-select --print-path
/Library/Developer/CommandLineTools
```

If you have no active developer directory on your macOS computer, this command prints the following message:

```None
% xcode-select --print-path
xcode-select: error: Unable to get active developer directory. Use 
sudo `xcode-select --switch <path/to/>Xcode.app` to set one 
(or see man xcode-select)
```

> ❗ **Important**: The standard location of Xcode is `/Applications/Xcode.app`. If you install Xcode in a nonstandard location, such as `/Applications/Xcode26/Xcode.app`, use Xcode settings or `xcode-select` to select this location.

##### Select the Default Xcode App

To change the default Xcode app for the command-line tools in Xcode, choose a different version of the app from the pop-up menu in Locations settings, under Command Line Tools. The pop-up menu contains the name and build of every Xcode app installed on your Mac.

![A screenshot of Xcode settings with Locations selected, showing the Archives, Compilation Cache(Automatic size), Command Line Tools, and Custom Paths sections. Under Command Line tools,](https://docs-assets.developer.apple.com/published/3f5461a67c10c118ad784741be7abaa7/configuring-command-line-tools-settings-02%402x.png) Enter your administrator password when the system prompts you to confirm the change.

Alternatively, you can set the default Xcode app for command-line tools in Terminal, using the `xcode-select` command. Enter `xcode-select` with the `--switch` option in Terminal:

```None
% sudo xcode-select --switch <path>
```

In this command, `<path>` specifies a path to the developer directory of the Xcode app or to the Command Line Tools for Xcode package you want to use.

> **Note**: The `--switch` option requires superuser permissions. If necessary, enter your administrator password when the system prompts you to use the `--switch` option.

For example, the following command selects a beta version of Xcode:

```None
% sudo xcode-select --switch /Applications/Xcode-beta.app
```

To select the Command Line Tools for Xcode package, run the following command:

```None
% sudo xcode-select --switch /Library/Developer/CommandLineTools
```

##### Select the Default Xcode App Temporarily

If you want to keep the default Xcode app for the command-line tools and use a command from a different version of Xcode, set the `DEVELOPER_DIR` environment variable when you invoke the command in Terminal:

```None
% env DEVELOPER_DIR="<path>" <command>
```

The environment variable overrides the active developer directory and doesn’t require superuser permissions. It takes the path of the developer directory of the Xcode app or the Command Line Tools for Xcode package you want to use.

For example, the following command gathers a sysdiagnose from a connected device and saves it at a specific location:

```None
% env DEVELOPER_DIR="/Applications/Xcode-beta.app" xcrun devicectl device sysdiagnose --device "Work iPad" --destination ~/Downloads --gather-full-logs 

```

## See Also

- [Installing the command-line tools](installing-the-command-line-tools.md)
  Install command-line tools for Xcode using an installer package or the Terminal app.
- [Xcode command-line tool reference](xcode-command-line-tool-reference.md)
  Use command-line tools that require you to install Xcode and set the app as the active developer directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-command-line-tools-settings)*