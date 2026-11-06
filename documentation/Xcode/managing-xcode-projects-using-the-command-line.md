# Managing Xcode projects using command-line tools

**Framework**: Xcode  
**Role**: Article

Edit build settings, targets, build phases, groups, and Swift package dependencies.

## Overview

Use the `xcodeproj` command-line tool to modify an existing Xcode project configuration in Terminal.

The `xcrun xcodeproj` commands apply to a single Xcode project file with a `.xcodeproj` extension in the current folder or the enclosing project folder by default. To use another Xcode project file from anywhere in the system, add the `--project <path.xcodeproj>` option to most of the `xcrun xcodeproj` commands.

For complete `xcrun xcodeproj` documentation, enter `xcrun xcodeproj help` or `xcrun xcodeproj help <subcommand>` in Terminal.

## Manage build settings

Use the `setting` subcommand to get and set build settings in a project. The command uses the setting name as it appears in the Xcode project file, not the human-readable name that appears in Xcode.

To set build settings on a specific target, add the `--target` option; otherwise, the command applies to the project. Similarly, to modify a specific configuration, use the `--config` option; otherwise, the command applies to all configurations.

To see the value for a specific build setting, such as the bundle ID for a target, use the `setting get` subcommand:

```shell
% xcrun xcodeproj setting get PRODUCT_BUNDLE_IDENTIFIER --target Landmarks
```

To get a list of all the build settings for a target, use the `setting list` subcommand.

For keys with a single string value, use the `setting set` subcommand to change build setting values. For keys with multiple string values, use the `setting set-multi` subcommand. To remove a build setting, use the `setting unset` subcommand.

To list the fully evaluated build settings for targets in a project, enter `xcodebuild -showBuildSettings` in Terminal. For more information on build settings, see [Build settings reference](./build-settings-reference.md).

## Manage targets

Use the `target` subcommand to inspect and modify targets in your project and their build phases.

```shell
% xcrun xcodeproj target --target <target>
```

Some `target` subcommands require the `--target <target>` option. Optionally, specify the project too using the `--project <path.xcodeproj>` option.

To get information about a target in a project, including the kind and product type, use the `target info` subcommand:

```shell
% xcrun xcodeproj target info --target Landmarks
```

To add a target to a project, use the `target add` subcommand:

```shell
% xcrun xcodeproj target add LandmarkModels --product-type framework
```

You can omit the `com.apple.product-type.` prefix for the `--product-type` values and pass `framework`, `tool`, or `application` instead. The command adds targets without schemes, because Xcode creates schemes automatically for you.

To remove a target, use the `target remove` subcommand.

To learn about a specific subcommand, enter `xcrun xcodeproj help target <subcommand>` in Terminal. For more information on targets, see [Configuring a new target in your project](./configuring-a-new-target-in-your-project.md).

## Manage build phases

Use the `target phase` subcommand to manage build phases for a target.

```shell
 % xcrun xcodeproj target phase add --target <target> <kind>
```

For example, to add an AppleScript-type build phase to a target, use the `target phase` subcommand with `apple-script` as the `kind` argument:

```shell
% xcrun xcodeproj target phase add --target Landmarks apple-script
```

To specify where to insert the build phase, include the optional `--position`, `--before`, and `--after` options. To remove a build phase, use the `target phase remove` subcommand.

To learn about all `target phase` subcommands, enter `xcrun xcodeproj help target phase` in Terminal. For more information on build phases, see [Customizing the build phases of a target](./customizing-the-build-phases-of-a-target.md).

## Manage files and folders

Use the `group` subcommand to create files and folders, or rearrange them, as they appear in the Project navigator in Xcode.

For the `path` argument that’s common to many `group` subcommands, you can use the system file path, the folder path as it appears in the Project navigator, or the identifier that the `xcrun xcodeproj group ls` command returns. Use the identifier if two files or folders have the same name.

To add a new folder, use the `group add` subcommand. To add a new file, use the `group add-file` subcommand, as in:

```shell
% xcrun xcodeproj group add-file <path> --group <group-path>
```

To remove files and folders, use the `group remove` and `group remove-file` subcommands.

For more information on using Xcode to perform these actions, see [Managing files and folders in your Xcode project](./managing-files-and-folders-in-your-xcode-project.md).

## Manage Swift packages

Use the `pkg` subcommand to list, add, and remove Swift package dependencies in a project.

To add a remote package dependency, use `pkg add`. To add a local package dependency, use `pkg add-local`. To remove a package dependency, use `pkg remove` and pass the package name.

```shell
% xcrun xcodeproj pkg add <url>
% xcrun xcodeproj pkg add-local <path>
% xcrun xcodeproj pkg remove <package>
```

To get the `<package>` value, enter `xcrun xcodeproj pkg list` in Terminal.

To add and remove package product links for a target, use the `pkg link` and `pkg unlink` subcommands.

```shell
% xcrun xcodeproj pkg link <product> --package <package> --target <target>
% xcrun xcodeproj pkg unlink <product> --target <target>
```

To start or stop running a package build-tool plugin, use the `pkg link-plugin` and `pkg unlink-plugin` subcommands.

To learn more about `pkg` subcommands, including more options, enter `xcrun xcodeproj help pkg <subcommand>` in Terminal. For more information on Swift packages, see [Swift packages](./swift-packages.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/managing-xcode-projects-using-the-command-line)*