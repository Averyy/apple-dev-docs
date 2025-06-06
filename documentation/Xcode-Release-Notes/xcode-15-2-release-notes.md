# Xcode 15.2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 15.2 includes SDKs for iOS 17.2, iPadOS 17.2, tvOS 17.2, watchOS 10.2, macOS Sonoma 14.2, and visionOS. The Xcode 15.2 release supports on-device debugging in iOS 12 and later, tvOS 12 and later, and watchOS 4 and later. Xcode 15.2 requires a Mac running macOS Ventura 13.5 or later.

##### General

###### Notes

- Developing for visionOS requires a Mac with Apple silicon.  (114799042)

###### Resolved Issues

- Fixed: Creating a new visionOS App target sets the Application Scene Manifest (Generation) target build setting to Yes by default. Changing to Application Scene Manifest using the Info dictionary editor doesn’t remove the build setting “Application Scene Manifest (Generation)” as expected, which will override changes with the default value.   (109428090)
- Fixed: When building with the visionOS SDK, `TargetConditionals.h` incorrectly sets TARGET_OS_IOS to 1 instead of 0.  (112716373)
- Fixes an issue with the “Get” button not showing for the visionOS simulator in the Settings > Platforms panel.  (115675177)

###### Known Issues

- visionOS App Icons don’t receive visual effects (depth, animation, edge textures) in Home View if any layer is smaller than 1024x1024px. Xcode doesn’t provide a warning or error for this behavior.  (107568059)  Make all layers of a visionOS App Icon 1024x1024px (@2x), and keep “Center in Canvas” and “Match Content Image” enabled in the Asset Catalog inspector for each layer.
- When the Base SDK Build Setting is set to iOS, the “Any visionOS Device” run destination will incorrectly display as “Any visionOS Device (Designed for iPad)” and will build using the iOS SDK.  (112633577) (FB12695059)  Change the Base SDK Build Setting to visionOS to use the “Any visionOS Device” run destination (FB12695059)

##### Asset Catalogs

###### Resolved Issues

- Fixed: Xcode crashes when attempting to view a visionOS asset catalog. This fix also requires macOS Sonoma beta 5 or later.  (110739616)

##### Device Support

###### Resolved Issues

- Fixed: Copying debug symbols from an Apple Watch running watchOS 10.3 Beta 2 may take longer than expected, approximately 10-20 minutes.  (120428859)

##### Devices

###### Known Issues

- In certain circumstances, an app can’t read the contents of its own data container after replacing the content of the data container using Xcode or devicectl.  (116698465) (FB13253099)
- Running a WatchApp that requires the companion iOS app to be installed will result in the error “An application bundle was not found at the provided path” when the run destination is set to a Watch via iPhone Simulator pair.  (119640671)  Select a singular Watch Simulator run destination and then Run.

##### Distribution

###### Resolved Issues

- Fixed: Xcode crashes when uploading visionOS apps using Xcode in Beta 2.  (111827403)

##### Organizer

###### Known Issues

- iOS app crashes from a TestFlight build on visionOS may not appear in the Crashes section of the Organizer.   (107965403)  From the “Pricing and Availability” section of your app’s App Store page in App Store Connect, enable the checkbox to allow your app to run on visionOS.

##### Playgrounds

###### Known Issues

- iOS App Playground projects are missing Apple Vision (Designed for iPad) run destinations.  (112795077)

##### Reality Composer Pro

###### Resolved Issues

- Fixed: Capturing screen recordings from Vision Pro devices always fails.  (114209977)

##### Simulator

###### Resolved Issues

- Fixed: iOS apps using the `#Preview` macro might quit unexpectedly when targeting `Apple Vision Pro (Designed for iPad)`.  (110801867)

##### Swiftdata

###### Resolved Issues

- Fixed: visionOS projects that use the `@Observable` property wrapper will fail to build in Xcode 15 beta 3.  (111494849)
- Fixed: SwiftData models don’t build with the visionOS SDK included in Xcode 15 beta 7.  (114106802)

##### Ui Automation

###### Known Issues

- visionOS doesn’t have any visual indication when UI automation is running.  Devices with a passcode still need to enter their passcode to start UI automation.  (85512012)

##### Visionos Simulator

###### Resolved Issues

- Fixed: There is no UI for simulating Apple Vision Pro’s immersion crown.  (109429267)
- Fixed: Showing immersive content always presents the safe area warning.  (112407012)

###### Known Issues

- On some configurations, the first install of an app will fail.  (115968389)  Build & run again.

##### Visionos Swiftui Previews

###### Resolved Issues

- Fixed issue where SwiftUI `#Preview` of a view containing `TabView` as top level element would crash preview.  (111229511) (FB12429863)

##### Xcode

###### Resolved Issues

- Fixed: The “Apple Vision (Designed for iPad)” run destination will disappear from the available destinations after adding or removing any device from General > Supported Destinations. The “Show Apple Vision (Designed for iPhone & iPad) Destination” build setting is automatically set to No, but Apple Vision (Designed for iPhone & iPad) remains in the Supported Destinations list. Designed for iPad destinations may be added automatically when adding or removing other device types from the list.   (110810619)

##### Xcode Cloud

###### Resolved Issues

- Fixed: visionOS Products may not show up in Xcode Cloud onboarding screens from within Xcode.  (111536280)

###### Known Issues

- HelloGlobe visionOS sample project does not build in Xcode Cloud.  (114666832)

##### Xcode Previews for Visionos

###### Resolved Issues

- Fixed: Textures often fail to load when viewing visionOS Previews in static mode.  (114044001)
- Fixed: Some 2D content may not be visible in Xcode Previews static mode.  (114220358)

## See Also

- [Xcode 15.4 Release Notes](xcode-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.3 Release Notes](xcode-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.1 Release Notes](xcode-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.0.1 Release Notes](xcode-15_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15 Release Notes](xcode-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_2-release-notes)*