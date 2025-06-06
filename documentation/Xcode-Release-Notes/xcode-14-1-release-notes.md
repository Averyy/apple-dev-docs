# Xcode 14.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 14.1 includes Swift 5.7 and SDKs for iOS 16.1, iPadOS 16.1, tvOS 16.1, watchOS 9.1, and macOS Ventura. The Xcode 14.1 release supports on-device debugging in iOS 11 and later, tvOS 11 and later, and watchOS 4 and later. Xcode 14.1 requires a Mac running macOS Monterey 12.5 or later.

##### General

###### Resolved Issues

- Fixed: The `ActivityAuthorizationInfo.activityEnablementUpdates` AsyncSream doesn’t send a new update when it’s changed in Settings.app (96630169)
- Fixed: iOS simulators may stop showing Live Activities and Dynamic Island features. (99108857)
- Fixed: Building a Matter Extension template results in a compiler error: `Cannot find type 'HMMatterRequestHandler' in scope` (99751983)

###### Known Issues

- After Running a widget extension, users will need to manually start the debugging session with Debug -> Attach to Process. (99285608)
- RealityKit’s FromToByAnimation may cause an app built with iOS 16 or macOS 13 SDKs to fail to launch on iOS 15 or macOS 12. (100228035) : Use the non-deprecated FromToByAnimation initializer which takes a `bindTarget:` parameter. If you encounter an ambiguous use error with the OrbitAnimation, using a `bindTarget:` parameter will resolve the ambiguity.
- App Shortcuts don’t support the use of compiler directives such as `#if` within the definition of the `appShortcuts` list. (100468932) : Avoid the use of compiler directives in App Shortcuts definitions. Consider having a AppShortcutProvider unique to each platform if there are differences in App Shortcuts between platforms.

##### Build System

###### Known Issues

- When removing a condition from the variant editor, the value won’t be persisted. (98149034) : Use the Build Settings Editor to remove the condition.

##### Interface Builder

###### New Features

- Interface Builder shows iPhone 14 and Apple Watch Ultra size models in the device bar. (99504634)

##### Simulator

###### Resolved Issues

- Starting in iPadOS 16.1, developers can turn on Stage Manager in the Simulator by using the appropriate setting in the Home Screen & Multitasking section of the Settings app. (95712631)

###### Known Issues

- Previously released simulators may not appear in Platforms pane after logging out and back in. (100815609) : Rebooting the system restores the list of previously released simulators.

##### Source Control

###### Resolved Issues

- Fixed: Onboarding a product to Xcode Cloud may get stuck after selecting a product in the onboarding sheet. (100432349)

###### Known Issues

- WatchOS apps can’t be onboarded to Xcode Cloud from Xcode. (96313262)

##### Source Editor

###### Resolved Issues

- Fixed an issue that affected reliability of dragging the program counter when debugging. (99465275)

##### Storekit

###### Resolved Issues

- Fixed: Using the following StoreKit properties and methods on apps with a minimum deployment target below iOS 16, macOS 13, watchOS 9, and tvOS 16 will cause the app to crash at launch when running on systems earlier than iOS 16, macOS 13, watchOS 9 and tvOS 16: - `priceFormatStyle` and `subscriptionPeriodFormatStyle` on `Product` values
- `environmentStringRepresentation` and `recentSubscriptionStartDate` on `Product.SubscriptionInfo.RenewalInfo` values
- `environmentStringRepresentation` on `Transaction` values
- `dateRange(referenceDate:)` and `formatted(_:referenceDate:)` on `Product.SubscriptionPeriod` values (99962885) (FB11516463)

## See Also

- [Xcode 14.3.1 Release Notes](xcode-14_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.3 Release Notes](xcode-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.2 Release Notes](xcode-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.0.1 Release Notes](xcode-14_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14 Release Notes](xcode-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-14_1-release-notes)*