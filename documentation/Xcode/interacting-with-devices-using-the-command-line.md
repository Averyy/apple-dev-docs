# Interacting with devices using the command line

**Framework**: Xcode

Manage simulated and physical devices from the command line.

#### Overview

You can manage physical and simulated devices using the `devicectl` command-line tool in Terminal without running Xcode. For example, use the `devicectl` command-line tool to automate common tasks when managing multiple test devices.

If you use `devicectl` in scripts or to automate managing devices, you can use the `--json-output` option with subcommands that create a JSON file with the command results. The JSON file format is versioned and backward compatible with previous releases, although some fields may appear deprecated in the file. In contrast, don’t rely on or parse the Terminal output from these commands, because the output may not be consistent in each release.

For complete `devicectl` documentation, enter `devicectl help` or `devicectl help <subcommand>` in Terminal (optionally, `devicectl --help`). For example, for descriptions of the `device copy to` subcommand options, enter:

```shell
% devicectl help device copy to
```

Before using `devicectl`, start the simulated devices and pair the physical devices you want to use.

#### Start Simulated Devices

To start simulated devices, use the `simctl` command. To install `simctl` and other command-line tools, see [`Installing the command-line tools`](installing-the-command-line-tools.md). After you install `simctl`, enter `xcrun simctl help` in Terminal to learn more.

Alternatively, use Device Hub to start simulators. Select the simulated device you want to use in the sidebar and click Start in the canvas.

#### Pair Physical Devices

To pair physical devices that you connect to your Mac with a cable, enter this command:

```shell
% devicectl manage pair
```

To use Device Hub to pair physical devices with your Mac, either wirelessly or with a cable, see [`Managing your simulated and physical devices in Device Hub`](managing-your-simulated-and-physical-devices-in-device-hub.md).

Whether you use the command line or Device Hub to pair physical devices, unlock the device before entering `devicectl` commands.

#### Specify Devices in Subcommands

You pass the device to subcommands by adding the `--device` option followed by the UUID, ECID, UDID, or name for the device.

To get devices and identifiers you use in subsequent commands, enter the `devicectl list devices` or `devicectl device info details` command in Terminal.

Alternatively, you can find most of these properties in the Device Hub inspector. Select the physical device in the sidebar, click the Info button in the far right of the toolbar, and then click the Info tab below. If the identifier doesn’t appear below, click Edit Visibility to see more properties.

To find device identifiers using other methods, see [`Locating device identifiers`](locating-device-identifiers.md).

#### Get Information About Devices

Use the `devicectl device info` command and subcommands to get additional information about devices. For example, use this command to find out whether a device is locked:

```shell
% devicectl device info lockState --device <uuid|ecid|udid|name>
```

Use this command to get more hardware details and metadata about a device:

```shell
% devicectl device info details --device <uuid|ecid|udid|name>
```

#### Install Apps on Devices

Use the `devicectl device install app` subcommand to install your app on the device:

```shell
% devicectl device install app --device <uuid|ecid|udid|name> <path>
```

If you build your app in Xcode, you can get the path to your app using the Project navigator. Under Products, Control-click the app and choose Show in Finder, or, as a shortcut, choose Open Terminal at Location from the contextual menu.

#### Launch Apps on Devices

You can launch an app on a simulated or physical device using its bundle ID or using the path to the app:

```shell
% devicectl device process launch --device <uuid|ecid|udid|name> <bundle-identifier-or-path>
```

For example, pass `com.example.MyApp` as the bundle ID or `.../MyApp.app` with the `.app` extension as the path.

For other ways to launch apps, enter `devicectl help device process launch` in Terminal. For example, use the `--environment-variables` option to pass environment variables to the app.

#### Pass File Locations to Subcommands

You provide file locations to subcommands that access the file system, such as `devicectl device info files` and `devicectl device copy`, as described below.

You can only read or write in domains (preset file locations) where you have permissions on the device. You specify the domain where files reside by adding the `--domain-type` option followed by one of these values: `appDataContainer`, `appGroupDataContainer`, `systemCrashLogs`, or `temporary`.

If necessary, provide a domain-specific identifier by adding the `--domain-identifier` option. For example, if you pass `appDataContainer` as the `--domain-type` value, pass the app’s bundle ID as the `--domain-identifier` value:

```shell
--domain-type appDataContainer --domain-identifier <bundle ID>
```

For the `temporary` domain, the identifier can be any nonempty string that allows you to disambiguate your temporary files from those of another client.

In addition, you may need to pass credentials using the `--user` option.

#### List Files on Devices

Use the `devicectl device info files` subcommand to return a list of files in a location on a device:

```shell
% devicectl device info files --device <uuid|ecid|udid|name> --domain-type <domain>
```

For example, to list all the crash reports, pass `systemCrashLogs` as the `--domain-type` parameter:

```shell
% devicectl device info files --device <uuid|ecid|udid|name> --domain-type systemCrashLogs
```

Then, use the `devicectl device copy from` command below to copy a crash log in the output to your Mac.

#### Transfer Files to and From Devices

Use the `devicectl device copy` subcommand to transfer files to and from physical devices that you pair with your Mac. You transfer files to and from specific file system locations where you have permissions.

To transfer files from your Mac to a device, use the `devicectl device copy to` subcommand, and to transfer files from a device to your Mac, use the `devicectl device copy from` subcommand. To specify the source and destination file paths, use the `--source` and `--destination` options.

For example, this command copies a file on your Mac to a location on the device:

```shell
% devicectl device copy to --device <uuid|ecid|udid|name> --source <filename> --destination <filename> --domain-type <domain>
```

This command copies a file on the device to your Mac:

```shell
% devicectl device copy from --device <uuid|ecid|udid|name> --source <filename> --destination <filename> --domain-type <domain> --domain-identifier <identifier>
```

#### Mount Devices on Your Mac

Instead of transferring files, you can browse the files of all physical and started simulated devices that your Mac knows about on a single shared volume or mount point, or get the mount point for a single device using `devicectl`.

The path to the default single mount point for all devices is `~/Library/Developer/CoreDevice/DeviceFS` (which appears as `Devices` in Finder). To get the path to a specific device folder, use the `devicectl device info mountpoint` subcommand:

```shell
% devicectl device info mountpoint --device <uuid|ecid|udid|name>
```

A device mount point contains one or more of these domain-specific subfolders: `AppDataContainers`, `AppGroupContainers`, `DiagnosticReports`, and `Temporary`. The device files are mostly read-only with limited write access depending on the subfolder, such as `AppDataContainers` and `AppGroupContainers`.

> **Note**: Physical device mount points also appear in Finder under Locations in the sidebar with the device name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/interacting-with-devices-using-the-command-line)*