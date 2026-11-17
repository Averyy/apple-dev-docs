# Xcode 27.3 Beta 2 Release Notes

**Framework**: Xcode Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

Xcode 27.3 beta 2 includes Swift 6.4 and SDKs for iOS 27.3, iPadOS 27.3, tvOS 27.3, watchOS 27.3, macOS 27.3, and visionOS 27.3. Xcode 27.3 beta 2 supports on-device debugging in iOS 17 and later, tvOS 17 and later, watchOS 10 and later, and visionOS. Xcode 27.3 beta 2 requires a Mac running macOS Tahoe 26.6 or later.

See [Xcode Support](https://developer.apple.com/support/xcode/) to learn more about compatible platforms and deployment targets.

### Device Hub

#### Known Issues

- Device Hub support for CarPlay requires devices to be physically connected via USB cable (not over the network). iOS Simulator is not supported for CarPlay. (179494052) (FB23101450)
- When using Device Hub via Sidecar or a Mac with Touch, only two touches can be sent to the target device. Three or more touches are interpreted by macOS as a system gesture. (185140491)

  **Workaround:** Turn off touch gestures in Settings under Touch Display.

### Instruments

#### New Features

- A new Standard Input File option in Launch Options lets a process launched on your Mac read its standard input from a file, matching `xctrace record --target-stdin`. (73743507)
- The Source Viewer now has copy buttons for copying the current function or the entire file along with its cost annotations. (166028723)
- The Time Profiler and Display instruments now include summary views that show the average CPU usage and average frame time for the selected time range. (FB23507969) (181104725) (FB23507969)
- `xctrace record --recording-options` and `--show-recording-options` now support the Allocations, Leaks, and VM Tracker instruments, so their recording options can be configured from the command line. (FB23554683) (181351150) (FB23554683)
- The new `xctrace triage` subcommand generates a report of the hangs in your trace. It combines data from multiple instruments into a concise overview of each hang, along with the context you need to investigate it. (182217728)
- A new ‘Always import as this template’ checkbox in File → Import to Template… makes Instruments use the chosen template every time you open that type of file. You can change the template later under Templates for Import in Settings → General. (184136239)
- The `xctrace` command-line tool can now export call trees, summaries, lists, and cost-annotated source code from traces, in plain text or Markdown. Use the new filtering, sorting, and data mining options to narrow the output to what you need. (184951123)
- `xctrace list templates` and `xctrace list instruments` now print a description of each template or instrument when you add the `--verbose` (`-v`) flag. (188404842)
- The Recording Information panel now includes a Target CPU Cores row showing the CPU core layout of the target device, and `xctrace export --toc` includes the same data in a new `cpu-cores` element. (188637563)

#### Resolved Issues

- Fixed an issue where the Allocations instrument would show 0 bytes in the Self Bytes column for allocation functions like `malloc` when Invert Call Tree was enabled. (125683004)
- Fixed an issue where the Processor Trace instrument would occasionally show “-0.0000” in the Instructions Per Cycle column. (149570087)
- Fixed an issue where `xctrace symbolicate` would leave some symbols unresolved, even when other symbols from the same library were resolved successfully. (FB17511755) (150743344) (FB17511755)
- Fixed an issue where an app bundle couldn’t be chosen as a launch target, and dragging one from Finder could select a different copy of the app with the same bundle identifier. (161272736)
- Fixed: The Power Profiler instrument no longer reports a 0% battery drain rate while the device is connected to power, and shows the rate as unavailable instead. To measure battery drain, record a ‘Performance Trace’ on the iOS device and open the resulting .atrc file in Instruments. (163944448)
- Fixed an issue where `xctrace record --launch` would also start a second, suspended copy of the app, leaving an extra Dock icon and a lingering process after recording. (174176781)
- Fixed an issue where call trees could intermittently be missing a small number of samples. (184136318)
- Fixed: Improved the performance of processing SwiftUI instrument data, which could previously take a very long time or appear stuck after recording or importing a trace. (184293877)
- Fixed an issue where reopening a file that was still being imported would start a second import instead of bringing the existing import progress to the front. (185058492)
- Fixed an issue where pressing the arrow keys in the Call Tree could leave the selection and scroll position of the weight columns out of sync with the symbol names. (186292599)
- Fixed an issue where windowed mode was unavailable for the RealityKit Trace template. (186506854)
- Fixed an issue where Instruments would hang when resizing the inspector while viewing a call tree. (187518651)
- Fixed a crash that occurred when stopping a recording that included the Network Connections instrument. (188127762)
- Fixed a crash that occurred when recording with the CPU Counters instrument in the Discarded guided mode. (188841714)
- Fixed an issue where stopping a recording in immediate mode could discard the recorded data, causing the saved trace to open without any data. (FB25375680) (191979844)
- Fixed an issue where Instruments would hang when opening traces of processes that created a very large number of threads. (191997867)
- Fixed an issue where `xctrace import` could hang instead of reporting an error when the input file could not be accessed. (192011544)

#### Deprecations

- The View Body and View Properties instruments have been removed. To profile SwiftUI apps, use the SwiftUI instrument, which supports iOS 26, iPadOS 26, macOS 26, tvOS 26, watchOS 26, visionOS 26, and later. (188227249)

### Localization

#### New Features

- New tools allow coding agents to manipulate String Catalogs in the same ways that the String Catalog Editor does. For example, agents can add and remove strings, change state, and reference strings by Swift symbol. (184511781)
- A new skill in Xcode aids coding agents in writing localizable code and detecting common localization problems. (184951217)
- Translating projects with coding agents now uses fewer tokens. (190440819)

#### Resolved Issues

- Improved performance when compiling String Catalogs with many locales. (188024317) (FB24882338)
- Resolved a crash that could occur when viewing an xcstrings diff in the stash viewer. (188813700)
- Fixed an issue where running `xcstringstool sync` on the command line would use a different key order than the IDE. This also fixes key order when using String Catalog MCP tools outside of Xcode. This requires macOS 27.3 Beta 2. (190849755)

### Previews

#### Resolved Issues

- Previews now render correctly on iPhone Duo. (185995983)
- Fixed: Xcode could crash when a preview updated after its scheme was reloaded from disk. (187067572)
- Fixed: Previewing on a device could erase the app’s existing data. (190012895) (FB25185762)
- Fixed: Snapshots from the RenderPreview MCP tool could have the wrong resolution when the image was downscaled. (190043246)
- Fixed: The software keyboard did not work in previews running on an iOS device. (190043382)

### Simulator

#### Resolved Issues

- Simulator runtime authenticity validation has been improved. As part of this effort, Xcode now includes checks that protect simulator runtimes from modification. Users who have relaxed their filesystem permissions on `/Library`, `/Library/Developer`, or `/Library/Developer/CoreSimulator` might find that simulators are not discovered. To fix this, restore permissions and ownership back to shipping defaults (`root:wheel 755`). (187122954)
- Fixed: Standby mode might render fully blank. (192294186)

#### Known Issues

- A simulator device might be shut down without warning if its runtime was mounted as a disk image and subsequently remounted as a cryptex. (191574717) (FB25398296)

### Xcode

#### New Features

- Xcode now includes two Apple specialists for coding agents. The `xctrace` specialists helps agents use the tool’s new export and filtering options to navigate trace data. The hangs specialist helps agents find hangs in your traces and fix them. (187385971)

## Updates in Xcode 27.3 Beta

### Coding Intelligence

#### New Features in Xcode 27.3 Beta

- GitHub Copilot is now available in the coding assistant. (185837709)

### Device Hub

#### New Features in Xcode 27.3 Beta

- You can now drag items onto a device in Device Hub. Drop an app (`.app` or `.ipa`) to install it, or drop a link to open it on the device. On iOS simulators, drop any other file to save it with the Files app. (179246120) (FB23037189)

#### Resolved Issues in Xcode 27.3 Beta

- Device Hub now supports using option-drag to simulate two-finger touch gestures for iPhones and iPads. (169537162)

### Previews

#### New Features in Xcode 27.3 Beta

- RenderPreview MCP tool snapshot filenames and metadata now include the applied overrides. (176531615)
- RenderPreview MCP tool now supports interactive delayed snapshots for macOS previews. (181244878)

#### Resolved Issues in Xcode 27.3 Beta

- A clearer error is now shown when the sandbox blocks a library from loading in a preview. (147269145)
- macOS widget previews now fail with a clear error. (178635433)
- Fixed a crash that could occur when building a preview after the workspace closes. (183679367)
- Fixed excessive processing time for source files that contain long operator chains. (184132564)
- Fixed an issue where previews refreshed unnecessarily when an Xcode project or workspace had not changed. (187278576) (FB24753484)
- Previews now refresh when asset catalog contents change on disk. (187456273) (FB24785391)
- Fixed an issue where the RenderPreview MCP tool could report no previews before they finished loading. (188424749)
- Fixed an issue where the RenderPreview MCP tool could render a different preview than the one requested. (188817121)
- Fixed a crash that could occur when changing code while in the Resizable Canvas mode. (189463909)

### Simulator

#### Resolved Issues in Xcode 27.3 Beta

- Fixed: Simulator runtimes might be inaccessible to users who are in the `daemon` group. (User accounts should not be added to the `daemon` group.) (190649396)

### Swift Testing

#### New Features in Xcode 27.3 Beta

- Xcode now supports writing UI tests with Swift Testing and `XCUIAutomation`. (95593221)

### UI Automation

#### New Features in Xcode 27.3 Beta

- `XCUIAutomation` supports setting the hinge angle on iPhone Duo with a new `XCUIHinge` class. (187479559)

### Xcode AEA

#### New Features in Xcode 27.3 Beta

- Xcode is now available as an Apple Encrypted Archive (`.aea`). If you’re installing Xcode from the command line, use `archiveutil extractXcodeAEA` to extract the Xcode archive.

  Xcode 27.3 is the final release supporting the `.xip` format. (111337953)

## See Also

### Xcode 27
- [Xcode 27.2 Release Notes](./xcode-27_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27.1 Release Notes](./xcode-27_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27 Release Notes](./xcode-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes)*