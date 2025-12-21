# Downloading and installing additional Xcode components

**Framework**: Xcode

Add more Simulator runtimes, optional features, and support for additional platforms.

#### Overview

Xcode lets you manage optional components yourself so that you can install only the components you use and remove the ones you don’t. For example, install the Simulator runtimes for the devices and operating systems your app runs on, or add support for platforms that you target. You download and install Xcode components in Xcode settings or using the command line.

> **Note**: Developing for visionOS requires a Mac with Apple silicon.

##### Manage Xcode Components in Settings

To manage your components, choose Xcode > Settings and click Components in the toolbar. Xcode shows the installed and enabled components along with the amount of storage you can recover if you remove them.

![A screenshot of Xcode settings with Components selected, showing the Platform Support, Other Components, and Other Installed Platforms sections. The rows contain the downloads for each section. The downloads that aren’t installed appear in gray text with a Get button on the right.](https://docs-assets.developer.apple.com/published/9e9659719f20c4f19b2a48c92af93049/downloading-and-installing-components%402x.png)

There are three types of components:

To download and install a component in any of these sections, click the Get button next to the component.

To remove or disable components you no longer use and recover their storage space, click the Info button next to the component. In the dialog that appears, click Delete or Turn Off depending on the component.

You can also install platform support when you create a project by selecting a template and clicking the Get button that appears for platforms that aren’t installed. For more information, see [`Creating an Xcode project for an app`](creating-an-xcode-project-for-an-app.md).

> **Note**: You can create a new Xcode project or work with an existing Xcode project on a platform that Xcode is installing, but you can’t run or build the project until Xcode finishes downloading and installing the files.

##### Install Previously Released Simulator Runtimes in Settings

You can get previously released Simulator runtimes in the Components settings. Click the Add button (+) in the lower-left corner, then select a platform to view a list of its available versions. In the dialog that appears, select one or more versions, and click Download & Install.

##### Install Simulator Runtimes From the Xcode Run Destination

When you open an Xcode project for a platform that doesn’t have any installed Simulator runtimes, Xcode displays a Get button next to the run destination. Click the Get button to download and install the most recent Simulator runtime for that platform.

The run destination in your Xcode project indicates when Xcode is downloading a Simulator runtime. You can select a run destination when Xcode completes the download and installation.

##### Download Xcode Components From the Command Line

You can also download components in Terminal using the `xcodebuild` command. For example, use the command line to download Xcode components once and then install them across multiple Mac computers.

To download Simulator runtimes for a specific platform, use this syntax:

```None
xcodebuild -downloadPlatform <iOS|watchOS|tvOS|visionOS>  [-exportPath <destinationpath> -buildVersion <osversion> -architectureVariant <universal|arm64>]
```

For example:

```None
xcodebuild -downloadPlatform iOS -exportPath ~/Downloads
```

To specify an OS version, add the `-buildVersion` option:

```None
xcodebuild -downloadPlatform iOS -exportPath ~/Downloads -buildVersion 18.0 
```

To download all the supported platforms for the version of Xcode you select, use this syntax with the `-downloadAllPlatforms` option:

```None
xcodebuild -downloadAllPlatforms [-exportPath <path>]
```

By default, Xcode downloads a variant based on your Mac computer’s architecture and whether you use Rosetta run destinations. Xcode downloads a universal variant for Intel-based Mac computers and when you use Rosetta run destinations. Otherwise, Xcode downloads an Apple silicon variant to save disk space for the platform you specify.

To download the universal variant that works on both Apple silicon and Intel-based Mac computers, use the `-architectureVariant` option:

```None
xcodebuild -downloadPlatform iOS -architectureVariant universal
```

##### Install Downloaded Packages From the Command Line

After you download component packages, you can install them in Terminal with the `xcodebuild` command.

First, select the version of Xcode you want to use with the `xcode-select -s <path-to-Xcode>` command. Next, run `xcodebuild -runFirstLaunch` to install any required system components, including the `simctl` utility. Then, run `xcodebuild` with the `-importPlatform <simruntime.dmg>` option to install the component.

```None
xcode-select -s /Applications/Xcode-beta.app
xcodebuild -runFirstLaunch
xcodebuild -importPlatform "~/Downloads/watchOS 9 beta Simulator Runtime.dmg"
```

##### Download and Install New Hardware Support in Between Xcode Releases

To download and install hardware support updates in between Xcode releases, use `xcodebuild` with the `-runFirstLaunch` and `-checkForNewerComponents` options. Before running this command, select the version of Xcode you want to use with the `xcode-select -s <path-to-Xcode>` command.

```None
xcode-select -s /Applications/Xcode.app
xcodebuild -runFirstLaunch -checkForNewerComponents
```

If new components exist, the `-checkForNewerComponents` option stores the files in the `~/Library/Developer/Packages/` directory and installs the components for the Xcode version you select.

##### Download and Install the Metal Toolchain

To build your Metal apps, download and install the optional Metal Toolchain for the platforms your app targets.

If a sheet appears when you first launch Xcode that lets you select components, select the app’s platforms, select Metal Toolchain under Additional Components, and click Install.

Otherwise, you can manage all your downloads, including the Metal Toolchain, using the Components settings in Xcode. Choose Xcode > Settings, click Components in the toolbar, and then click the Get button next to Metal Toolchain under Other Components.

If you attempt to build an app that requires the Metal Toolchain before downloading the toolchain, a dialog appears. Click Download to download the Metal Toolchain.

Alternatively, to download and install the toolchain from the command line, run this command from Terminal:

```None
xcodebuild -downloadComponent metalToolchain
```

To download and install the toolchain separately, first download and export it to a file:

```None
xcodebuild -downloadComponent metalToolchain -exportPath ~/Downloads
```

Then, install the toolchain into Xcode:

```None
xcodebuild -importComponent metalToolchain ~/Downloads/metalToolchain.dmg
```

## See Also

- [Installing your app in many Simulator platforms and versions](installing-your-app-in-many-simulator-platforms-and-versions.md)
  Set up your app in multiple Simulator platforms and versions without the build-and-run cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/downloading-and-installing-additional-xcode-components)*