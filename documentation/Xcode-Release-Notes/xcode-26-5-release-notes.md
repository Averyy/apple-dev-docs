# Xcode 26.5 Beta 2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.5 beta 2 includes Swift 6.3 and SDKs for iOS 26.5, iPadOS 26.5, tvOS 26.5, macOS 26.5, and visionOS 26.5. Xcode 26.5 beta 2 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.5 beta 2 requires a Mac running macOS Tahoe 26.2 or later.

##### General

###### Known Issues

- When streaming stdout and stderr from multiple processes at the same time (eg: in parallel testing scenarios), the results may be significantly delayed.  (165098287)

##### Background Assets

###### Known Issues

- The system may incorrectly determine an app’s eligibility for development overrides in simulator environments.  (173742496) **Workaround:** Test your app on a physical device.

##### Security

###### Resolved Issues

- Fixed: Mac (Designed for iPad) apps with pointer authentication are now compatible with macOS Tahoe 26.5 and newer. Add `LSMinimumSystemVersion` with value `26.5` to your app’s Info.plist to ensure the app only runs on Tahoe 26.5 and newer.  (171174887)

##### Simulator

###### Resolved Issues

- Fixed: Pasteboard Synchronization within Simulator.app is currently not functioning.  (173403967) (FB22340739)

##### Testing

###### Resolved Issues

- Fixed: Tests fail to run on iOS 15 simulators  (173337319) (FB22333623)

#### Updates in Xcode 265 Beta

##### Instruments

###### Resolved Issues in Xcode 265 Beta

- Fixed: Typing in the filter field at the bottom of the Symbols window would create a token for every character  (172423349)
- Fixed an issue where profiling using Metal System Trace with GPU Counters capture could cause memory footprint of Instruments to increase to tens of gigabytes.  (173195251)

##### Storekit Testing in Xcode

###### New Features in Xcode 265 Beta

- New billing plan APIs can be tested using [`StoreKit Testing in Xcode`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode). Configure a monthly with 12-month commitment billing plan for your auto-renewable subscriptions in the StoreKit Configuration, and simulate subscribing to the billing plan through the Transaction Manager in Xcode.  (168522699)

## See Also

- [Xcode 26.4.1 Release Notes](xcode-26_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.4 Release Notes](xcode-26_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.3 Release Notes](xcode-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.2 Release Notes](xcode-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.1.1 Release Notes](xcode-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.0.1 Release Notes](xcode-26_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26 Release Notes](xcode-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_5-release-notes)*