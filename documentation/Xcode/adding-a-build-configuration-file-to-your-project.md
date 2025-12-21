# Adding a build configuration file to your project

**Framework**: Xcode

Specify your project’s build settings in plain-text files, and supply different settings for debug and release builds.

#### Overview

A build configuration file is a plain-text file you use to specify the build settings for a specific target or your entire project. Build configuration files make it easier to manage build settings yourself, and to change build settings automatically for different architectures and platforms. With a build configuration file, you place only the settings you want to modify in a text file. You can create multiple files, each with different combinations of build settings, and you can change the settings quickly for your target or project. Xcode layers your settings on top of other project-related settings to create the final build configuration.

Build configuration files are particularly useful in the following situations:

- You want different build settings based on the current platform, architecture, or build type.
- You want to store build settings in a way that is easier to inspect.
- You want to edit build settings outside of Xcode.

For more information about how build configuration files integrate with your project’s other settings values, see [`Configuring the build settings of a target`](configuring-the-build-settings-of-a-target.md).

##### Add a Build Configuration File to Your Project

A build configuration file is a text file with an `.xcconfig` filename extension that you add to your project. You can create as many build configuration files as you want, and you configure different settings in each one. For example, you might use one build configuration file for debug settings and another for release settings.

To create a build configuration file:

1. Select File > New File.
2. Select Configuration Settings File.
3. Click Next.
4. Enter a name and location for your build configuration file.
5. Deselect all targets to prevent Xcode from embedding the file as a resource in the target’s bundle.
6. Click Create to add it to your project.

![A figure that shows the selection of the Configuration Settings File template in Xcode’s file template chooser.](https://docs-assets.developer.apple.com/published/2644ce60d016773eec58777b20fa0216/build-configuration-creation%402x.png)

##### Map Build Settings to a Build Configuration

You can specify different build configuration files for debug and release builds, and you can layer configuration files on top of other settings. To specify build configuration files:

1. Select your project in the project editor.
2. Click the Info tab.
3. Click the disclosure triangles to expand the Debug and Release build configurations in the Configurations area.
4. Choose configuration settings files for your Debug and Release builds from the pop-up menus. You can also select a file that applies to both build types.

![A figure that shows the Info tab of the project editor. The Configurations section shows build configuration files assigned to the debug and release builds of a target and its project.](https://docs-assets.developer.apple.com/published/0923c1e0e0a76674a2cbdd81ca108379/build-configuration-mapping%402x.png)

Xcode applies settings from a build configuration file before the corresponding settings from the project’s or target’s Build Settings tab. For example, if you provide a build configuration file for your target, Xcode applies the project settings, then the build configuration settings, then the target settings.

For more information about the order in which Xcode applies settings, see [`Configuring the build settings of a target`](configuring-the-build-settings-of-a-target.md).

##### Assign a Value to a Setting

To specify a new value for a setting, add that setting to your configuration file using the following format:

```None
<SettingName> = <SettingValue>
```

Place each setting on a separate line, and include only the settings you want to change in your build configuration file. Xcode ignores leading and trailing spaces, so you can indent settings as needed. If you add the same setting multiple times, Xcode uses the last instance of the setting and ignores previous instances.

Many value types are possible for settings, but the following table lists the most common ones:

| Value type | Description |
| --- | --- |
| `Boolean` | A value of `YES` or `NO`. |
| `string` | A text string. |
| `enumeration (string)` | A predefined text string. See the settings reference for a list of valid values. |
| `string list` | A space-separated list of `string` values. If a string within the list contains spaces, surround that string with quotes. |
| `path` | A file or directory path, in POSIX form. |
| `path list` | A space-separated list of `path` values. If a path within the list contains spaces, surround the path with quotes. |

Some examples of settings include:

```None
ONLY_ACTIVE_ARCH = YES
MACOSX_DEPLOYMENT_TARGET = 11.0
OTHER_LDFLAGS = -lncurses
```

For a list of build settings, see [`Build settings reference`](build-settings-reference.md).

##### Augment a Setting with Additional Values

In some cases, you might want to extend a setting rather than overwrite its current value. For example, you might want to add more flags to a compiler instead of replacing the existing flags. To extend a setting’s existing value, add the `$(inherited)` keyword to the value of your setting, as shown in the following example:

```None
OTHER_SWIFT_FLAGS = $(inherited) -v
```

##### Refer to the Value of Another Setting

To reuse an existing build setting’s value, place the name of the setting in a string of the form `$(SettingName)`. When evaluating your build settings, Xcode replaces these references with the values of the corresponding settings. For example, the following definition assigns the value of the `SYMROOT` build setting to the `OBJROOT` setting:

```None
OBJROOT = $(SYMROOT)
```

When replacing references, Xcode inserts the setting’s value at the same location as the original reference. You can insert references in the middle of a new value, or you can define a setting using multiple other values, as shown in the following examples:

```None
DSTROOT = /tmp/$(PROJECT_NAME).dst
CONFIGURATION_BUILD_DIR = $(BUILD_DIR)/$(CONFIGURATION)$(EFFECTIVE_PLATFORM_NAME)
```

##### Apply a Setting Conditionally to a Platform or Architecture

Add a conditional expression after a build setting to apply that setting only when a specific platform or architecture is active. To specify a conditional expression, enclose it in square brackets after the build setting name, as shown in the following example:

```None
OTHER_LDFLAGS[arch=x86_64] = -lncurses
```

Xcode applies a build setting only when the setting’s conditional expression evaluates to true. Xcode supports the following conditions:

| Condition | Values |
| --- | --- |
| `sdk` | An SDK, such as `macosx12.0` or `iphoneos15.0`. To match all versions of a specific platform, replace the version number with an asterisk (*). For example, specify `macosx*` to match any macOS SDK. |
| `arch` | A CPU architecture, such as `arm64` or `x86_64`. |
| `config` | The build configuration, such as `Debug` or `Release`. |

To add multiple conditions to the same build setting, place each condition in separate brackets after that setting’s name, as shown in the following example:

```None
OTHER_LDFLAGS[sdk=macos*][arch=x86_64] = -lncurses
```

##### Include Settings From Other Build Configuration Files

When you specify the build configuration file for your target, you must select only one file, but that file can include settings from other configuration files. To import the settings from a different configuration file, add an `#include` statement:

```None
#include "MyOtherConfigFile.xcconfig"
```

If Xcode can’t find an included build configuration file, it generates build warnings. To suppress these warnings, add a question mark (?) to the `#include` command, as shown in the following example:

```None
#include? "MyOtherConfigFile.xcconfig"
```

Xcode looks for included build configuration files in the same directory as the current file. If your build configuration file is in a different directory, specify a relative path or an absolute path, as shown in the following examples:

```None
#include "../MyOtherConfigFile.xcconfig"    // In the parent directory.
#include "/Users/MyUserName/Desktop/MyOtherConfigFile.xcconfig" // At the specific path.
```

##### Add Comments to Your Settings

Add comments to your build configuration files to include notes or other information that’s relevant to you. Specify your comments on a single line preceded by two forward slashes (`//`). The build system ignores everything from the comment delimiter to the end of the current line. For example:

```None
//
//  Base Settings.xcconfig
//  Base Settings
//
//  Created by Johnny Appleseed on 7/21/21.
//
```

You can also place a comment at the end of a line that contains a build setting definition, as in the following example:

```None
ASSETCATALOG_COMPILER_APPICON_NAME = MyAppIcon // This is a comment. 
```

## See Also

- [Configuring the build settings of a target](configuring-the-build-settings-of-a-target.md)
  Specify the options you use to compile, link, and produce a product from a target, and identify settings inherited from your project or the system.
- [Build settings reference](build-settings-reference.md)
  A detailed list of individual Xcode build settings that control or change the way a target is built.
- [Identifying and addressing framework module issues](identifying-and-addressing-framework-module-issues.md)
  Detect and fix common problems found in framework modules with the module verifier.
- [Understanding build product layout changes in Xcode](understanding-build-product-layout-changes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-a-build-configuration-file-to-your-project)*