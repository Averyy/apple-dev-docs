# Xcode 15.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 15.1 includes SDKs for iOS 17.2, iPadOS 17.2, tvOS 17.2, watchOS 10.2, and macOS Sonoma 14.2. The Xcode 15.1 release supports on-device debugging in iOS 12 and later, tvOS 12 and later, and watchOS 4 and later. Xcode 15.1 requires a Mac running macOS Ventura 13.5 or later.

##### General

###### Resolved Issues

- Fixed: Executing Unit/UI tests from Xcode on the iOS Simulator takes an extended time to launch on first run of the suite. (115187363)  (110330776) (FB12237092)
- Fixed: Swift macro definitions from the macOS/iOS/tvOS/watchOS SDKs are not available in Swift Playgrounds.  (112122752) (FB12581131)
- Fixed: The simulator may crash when opening Settings or Action Button settings on iPhone 15 Pro devices.  (115388496)

##### App Intents

###### Resolved Issues

- Fixed: Apps that have adopted AppIntents features from iOS 17.0, watchOS 10.0, and macOS 14.0 or beyond but run on iOS 16.0, watchOS 9.0 or macOS 13.0 may crash.  (118082753)

##### Device Support

###### Known Issues

- Copying debug symbols from an Apple Watch running watchOS 10.3 Beta 2 may take longer than expected, approximately 10-20 minutes.  (120428859)

##### Devices

###### Resolved Issues

- Fixed an issue in which files would appear to be missing when downloading the contents of a data container from a device, or when getting the list of files in a container.  (101007362)
- Fixed: The ability to install apps using IPA files which was present in previous versions of Xcode has now been restored.  (112295481)
- Fixed an issue which caused `CoreDeviceService` to exhaust sandbox memory over time, resulting in Xcode being unable to install apps on a device.  (115682803)
- Fixed: The file transfer capability in Xcode previously could be used to access a container on the device for an app or app extension that was not yet installed. This access is now prevented. If this functionality has been previously used, it could prevent the installation of an app or app extension. To get out of this state, back up, erase, then restore the device.  (115949353) (FB13201417)
- Fixed: Xcode is unable to connect to a watch running watchOS 9 or earlier if it is paired to an iPhone running iOS 17 or later, and may cause excessive battery drain on any such watch in close proximity.  (116557139) (FB13239145)
- Fixed: Xcode may keep AppleTV display awake after developer is done working with it.  (117165859)

###### Known Issues

- In certain circumstances, an app can’t read the contents of its own data container after replacing the content of the data container using Xcode or devicectl.  (116698465) (FB13253099)
- Running a WatchApp that requires the companion iOS app to be installed will result in an error if the run destination is set to a Watch via iPhone Simulator pair.  (119640671)  Select a singular Watch Simulator run destination and then Run.

##### Instruments

###### Resolved Issues

- Fixed: Leaks instrument never detects leaks.  (115440742)

##### Interface Builder

###### Resolved Issues

- Fixed issue that caused Interface Builder documents using custom App fonts to load incorrect font at runtime.  (113624207) (FB12903371)

###### Deprecations

- `@IBDesignable` views are deprecated and will be removed in a future release.  (115873872)

##### Linking

###### Resolved Issues

- Fixed: Binaries using symbols with a weak definition crash at runtime on iOS 14/macOS 12 or older. This impacts primarily C++ projects due to their extensive use of weak symbols.  (114813650) (FB13097713)
- Fixed: Weak symbol imports are linked as non-weak imports, when used from LTO object files.  (115521975) (FB13171424)

##### Optic Id

###### Resolved Issues

- Fixed: Even though Optic ID appears in Simulator, it isn’t possible to simulate Optic ID enrollment.  (112460069)

##### Previews

###### Resolved Issues

- Fixed: AppKit previews in projects that have a deployment target less than macOS 14.0 will fail to compile.  (113047811)

##### Reality Composer Pro

###### Resolved Issues

- Fixed: Reality Composer Pro now correctly export ACES OCIO names for color spaces to USD when they’re selected by the user in UI, otherwise the existing color space is used.  (106431182)
- Fixed: Statistics shown in bottom panel ignore Shader Graph Materials when counting Textures.  (109681637)
- Fixed: While in Selection Mode, Statistics shown in the bottom panel may count resources twice (e.g. same texture counted twice).  (110007062)
- Fixed: Copy and paste menu items may be disabled in the Edit menu when nothing is selected in the scene.  (110181840)
- Fixed: Some library assets can’t be downloaded by clicking on the download button or using Download menu item.   (110209688)
- Fixed: Some image formats are exported as-is when exporting a scene as a USDZ file from Reality Composer Pro resulting in an invalid USDZ.  (110538624)
- Fixed: Locked items in the scene hierarchy could still allow editing operations to be performed.  (110545827)
- Fixed: Audio asset “AtmosphereJungle” doesn’t load and will be removed in upcoming release.  (110725118)
- Fixed: Reality Composer Pro Acoustic Environment preview does not switch back to None.  (110876824)
- Fixed: Issue navigator may still display stale package dependency errors even after the error is fixed.  (110906050)
- Fixed: The Particle Emitter ‘Is Local’ property is renamed to: ‘Particles Inherit Transform’ which determines if the entity’s transform also affects the particles. This also adds a new ‘Fields Are Local’ property which is not functional.  (111410569)
- Fixed: Reconstructing an object with Object Capture Model can result in a crash on an Intel-based Mac.  (111645963)
- Fixed: Directly opening the .rkassets folder with Reality Composer Pro can overwrite parts of the project causing data loss.  (112414255)
- Fixed: Audio mix groups are not functional at runtime.  (113226910)

###### Known Issues

- Reality Composer Pro might quit unexpectedly after switching audio devices from a Studio Display to another device, such as AirPods or built-in speakers.  (109912081)  Save the project and quit Reality Composer Pro, switch the audio output device, then reload the project.
- Subsequent launches of app in Simulator might not play audio on launch  (113052899)  You can keep a reference to the AudioPlaybackController, either in a variable or a collection, replacing instances of `entity.playAudio(someAudioFileResource)` with `controller = entity.playAudio(someFileResource)` where the `controller` variable keeps a reference to the sound for the expected duration of playback. Keeping a reference to the controller should work around this issue until fix is available.

##### Signing Distribution

###### Resolved Issues

- Fixed: Resolved an issue that prevented `xcodebuild` from installing the Apple eWorldwide Developer Relations intermediate certificate into the keychain.  (81581660)

##### Simulator

###### Resolved Issues

- Fixed: Xcode isn’t offering the latest iOS simulator runtime for downloading when an older one exists.  (116372892)

##### Storekit

###### New Features

- New pricing properties `price`, `currency`, and `currencyCode` are now available on [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction). If an offer was applied to the transaction, a new property `offer` is available to see information about it (id, type, payment mode), as well as convenience properties `offerID`, `offerType`, and `offerPaymentMode`.  (106650768)

##### Storekit Testing in Xcode

###### New Features

- New testing functionality to send [`Purchase Intents`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/purchaseintent) to apps using StoreKit Testing in Xcode from the Transaction Manager.  (101034395)

###### Resolved Issues

- Fixed an issue causing the StoreKit transaction manager to sometimes display duplicate devices in the navigator after launching an app from Xcode.  (117541432)

##### Swift

###### Resolved Issues

- Fixed: Swift apps built with Xcode 15.0 crash on launch on macOS 10.13.  (114820860)

##### Swift Packages

###### Resolved Issues

- Fixed: If the `Package.swift` file of a Swift App Playground project has been hand-edited to include unit test targets, the app playground fails to build with an error about duplicate commands.  (113752456)

##### Test Report

###### Resolved Issues

- Fixed: Test Report may present a screenshot or screen recording attachment that is unaccessible  (112145122)
- Fixed: Test Report’s Gallery View may be missing screenshots in cases with one run destination and one test plan configuration  (117428402)

##### Testing

###### Resolved Issues

- Fixed: Unit test bundles hosted by extension-based WatchKit applications fail to run on device destinations when code coverage is enabled in the active test plan.  (118158060)

##### Visionos

###### Known Issues

- iOS apps with a deployment target set to 17.2 fail to run on Apple Vision Pro.  (117105090)  Set the iOS deployment target to 17.0 or earlier in the project or target’s build settings.

##### Xcode Cloud

###### New Features

- Xcode now supports configuring a new Manual start condition in Xcode Cloud workflows.  (112108570)

##### Xctest

###### Known Issues

- Test Action report logs may appear in less human readable form when os_log’s are output.  (118455129)  Set this User Default on your system by running the following command in terminal. `defaults write com.apple.dt.Xcode IDEDisableConsoleLibLogRedirectLoggingForTestActions -bool YES`

## See Also

- [Xcode 15.4 Release Notes](xcode-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.3 Release Notes](xcode-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.2 Release Notes](xcode-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.0.1 Release Notes](xcode-15_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15 Release Notes](xcode-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_1-release-notes)*