# iOS & iPadOS 17.1 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 17 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 17.1. The SDK comes bundled with Xcode 15, available from the Mac App Store. For information on the compatibility requirements for Xcode 15, see [`Xcode 15 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15-release-notes).

##### App Intents

###### Resolved Issues

- Fixed issue whre `SiriTipView` might not render the correct name for an application that uses alternate app names.  (110718562)
- Fixed issues where a single `AppEntity` might not be behave properly when used across multiple `OptionsCollections` within a single `AppShortcut`.  (111712115)
- Fixed issue where running App Intents from Live Activities might incorrectly cause the Shortcuts app to launch.  (111820333) (FB12528352)
- Fixed issue where `SiriTipUIView` wouldn’t render correctly with Dynamic Text.  (112781776)
- Fixed issue where App Shortcuts using `AppEnums` might not appear correctly in the Shortcuts app or in Spotlight.  (115353694) (FB13157399)

##### Automatic Assessment Configuration

###### Resolved Issues

- Fixes an issue that can result in a crash when tapping on a text field. This is also fixed for Autonomous Single App Mode.  (115862218) (FB13195697)

##### Camera

###### Resolved Issues

- Fixed: Repeatedly entering Cinematic mode or switching between front facing and rear facing captures in Cinematic mode on iPhone 15 and iPhone 15 Pro might cause the preview to freeze for a couple of seconds.  (116128057)

##### Power

###### Resolved Issues

- Fixed: Increased power consumption might occur when an Apple watch running watchOS10.1 is paired with an iPhone with iOS 17.0 (or watchOS10.0 is paired with iOS17.1).   (116348186)

##### Remote Widgets

###### Resolved Issues

- Fixed: Remote Widgets might render blank on mismatched iOS and macOS releases.  (115436466)

##### Skadnetwork

###### Resolved Issues

- Fixed: Calling the deprecated SKAdNetwork registerAppForAdNetworkAttribution API will not reset the conversion value to 0 in SKAdNetwork 4.0 postbacks.  (113371209)

##### Storekit

###### Resolved Issues

- Fixed issue where the `completionBlock` in `loadProduct(withParameters:completionBlock:)` would return success for an invalid product identifier.  (114389619) (FB13048488)

##### Wallet Apple Pay

###### Known Issues

- Wallet might crash on launch for some users who connect cards to bank accounts on on iOS 17.1 Beta 1 & 2 once Beta 3 is released.  (116694764)  Update device to iOS 17.1 Beta 3.
- The connection between a card and bank account might unexpectedly revoke.  (116738732)  Follow the instructions in the “Update Your Connection” repair flow.
- If the connection between a card and bank account is revoked, some users might encounter an error when completing the “Update Your Connection” repair flow.  (116738863)  Opening Settings and navigate to Apple Pay & Wallet > Connections. Remove the connection to your institution, and re-connect your card again.

##### Iphone 12 in France

###### Notes

- Updates the iPhone 12 for users in France to accommodate a test protocol for Specific Absorption Rate (SAR) testing. For more information, visit this website: [`https://support.apple.com/kb/HT213923`](https://developer.apple.comhttps://support.apple.com/kb/HT213923)  (116601274)

## See Also

- [iOS & iPadOS 17.6 Release Notes](ios-ipados-17_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.5 Release Notes](ios-ipados-17_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.4 Release Notes](ios-ipados-17_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.3 Release Notes](ios-ipados-17_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.2 Release Notes](ios-ipados-17_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17 Release Notes](ios-ipados-17-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-17_1-release-notes)*