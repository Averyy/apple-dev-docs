# Xcode 15.4 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 15.4 includes SDKs for iOS 17.5, iPadOS 17.5, tvOS 17.5, watchOS 10.5, macOS Sonoma 14.5, and visionOS 1.2. The Xcode 15.4 release supports on-device debugging in iOS 12 and later, tvOS 12 and later, watchOS 4 and later, and visionOS. Xcode 15.4 requires a Mac running macOS Sonoma 14 or later.

##### General

###### New Features

- Xcode 15.4 supports simulating web distribution while running or testing your app. Enable the “Alternative Distribution - Web” build setting in your app target or project, then select “Website” in your scheme or test plan in the `Distribution` option. When you run or test your app, it will receive the `AppDistributor.web` value when querying `MarketplaceKit` for its current `AppDistributor`.  (124230395)

###### Resolved Issues

- Fixed: watchOS Apps do not install on Series 3 and earlier.  (118490442) (FB13378667)

###### Known Issues

- Some Macs recently received a macOS system update which disabled the simulator runtimes used by Xcode, including the simulators for iOS, tvOS, watchOS, and visionOS. If your Mac received this update, you will receive the following error message and will be unable to use the simulator: ```None
 The com.apple.CoreSimulator.SimRuntime.iOS-17-2 simulator runtime is not available.
 Domain: com.apple.CoreSimulator.SimError
 Code: 401
 Failure Reason: runtime profile not found using "System" match policy
 Recovery Suggestion: Download the com.apple.CoreSimulator.SimRuntime.iOS-17-2 simulator runtime from the Xcode 
``` (127498625)  To resume using the simulator, please reboot your Mac.  After rebooting, check Xcode Settings → Platforms to ensure that the simulator runtime you would like to use is still installed.  If it is missing, use the Get button to download it again.

##### App Shortcuts Preview

###### Known Issues

- Enabled App Shortcuts preview, but the app’s base locale might fail.  (125556990)

##### Asset Catalogs

###### Resolved Issues

- Fixed an issue where generated asset symbols emitted warnings with Swift strict concurrency checking enabled.  (124156187)

##### Devices

###### Resolved Issues

- Fixed: In certain circumstances, an app can’t read the contents of its own data container after replacing the content of the data container using Xcode or devicectl.  (116698465) (FB13253099)

##### Simulator

###### Resolved Issues

- Fixed: When attempting to boot a simulator device shortly after installing its runtime or updating to a new version of macOS, Gatekeeper scanning may temporarily prevent boot.  This can appear as an “Unable to boot the Simulator” or “-308” error.  (118038020)
- Fixed: When attempting to boot a simulator device after an XProtect update is installed, Gatekeeper scanning may temporarily prevent boot.  This can appear as an “Unable to boot the Simulator” or “-308” error.  (124502668)

##### Testing

###### Resolved Issues

- Fixed: Using `XCTestCase.fulfillment(of:)` in an actor-isolated test method produces a warning.  (124112256)

##### Xcode Previews

###### Known Issues

- Previews may fail in projects or targets that use special characters such as curly quotes, Phi, etc.  (125490102) (FB13699939)  Rename project and/or target to no longer use special characters.

## See Also

- [Xcode 15.3 Release Notes](xcode-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.2 Release Notes](xcode-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.1 Release Notes](xcode-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.0.1 Release Notes](xcode-15_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15 Release Notes](xcode-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_4-release-notes)*