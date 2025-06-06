# macOS Sequoia 15.1 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 15.1 SDK provides support to develop apps for Mac computers running Sequoia 15.1. The SDK comes bundled with Xcode 16.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.1, see [`Xcode 16.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_1-release-notes).

##### Appkit

###### Resolved Issues

- Resolved an issue where menu item keyboard shortcuts in the Services menu would take precedence over shortcuts for application menu items.  (134539327)

##### Carbon

###### Resolved Issues

- Resolved an issue where iBooks Author quits unexpectedly when clicking Charts or Widgets in the toolbar.  (134693081)

##### Datadetection

###### Resolved Issues

- Resolved an issue where iPhone and iPad apps on Apple Silicon Macs might quit unexpectedly if DataDetection API is used.  (128080892)

##### Messages

###### Resolved Issues

- Fixed an issue preventing iMessage and other third-party notifications from being received while your device is connected on a VPN.  (136775545)

##### Mobile Device Management

###### New Features

- MDM profiles can use the new key ‘forceBypassScreenCaptureAlert’, which allows owners of managed devices to opt out of user notifications for content capture technologies.  (131327961)

##### Quick Look

###### Resolved Issues

- Fixed: Back-deploying apps that link QuickLookUI to macOS 11 or earlier might crash.  (133213738) (FB14667312)

##### Screencapturekit

###### New Features

- Applications using our deprecated content capture technologies now have enhanced user awareness policies. Users will see fewer dialogs if they regularly use apps in which they have already acknowledged and accepted the risks.  (133431080)

##### Siri

###### Resolved Issues

- Fixed: Some of the buttons on the macOS Siri snippets might be unresponsive when using Siri through Voice.  (133194038)

##### Storekit

###### Resolved Issues

- Fixed: In StoreKit Testing in Xcode, the offer identifier in the subscription renewal info might be reported incorrectly for offer codes.  (133774710)

##### Swift Charts

###### Resolved Issues

- Fixed: Any project that utilizes Swift Charts fails to build when targeting iOS, macOS, or visionOS.  (135905498)

##### Swiftui

###### Resolved Issues

- Fixed: Using `if #available` in @WidgetBundleBuilder and @SceneBuilder crashes on prior OS versions due to “unknown OS version.”  (136098106)

###### Known Issues

- macOS apps might crash with an exception related to duplicate toolbar items. This often happens when either (A) `NavigationSplitView`s are nested or (B) toolbars with `id`s are specified (`View.toolbar(id:...)`) and a new window is created with the same identified toolbar.  (134589426)  (A) Use apply `.toolbar(removing: .sidebarToggle)` within the sidebar column of the inner `NavigationSplitView`. (B) Temporarily stop using identified toolbars until this issue is addressed. Alternatively, sometimes it might be possible to workaround (B) by moving toolbar items around or rendering them after a short delay.
- On macOS 15.1, Tabs in TabViews that use the .sidebarAdaptable style might not be selected when the Tab label is clicked.  (137277517) (FB15383066)

##### System Integrity Protection

###### Resolved Issues

- Fixed: Users might be incorrectly prompted when an app that is distributed through TestFlight attempts to access an application group container.  (131606564) (FB14288230)

##### Uikit

###### Resolved Issues

- Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when loading UIReferenceLibraryViewController.  (79135995) (FB9153775)

## See Also

- [macOS Sequoia 15.5 Release Notes](macos-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.4 Release Notes](macos-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.3 Release Notes](macos-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.2 Release Notes](macos-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15 Release Notes](macos-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-15_1-release-notes)*