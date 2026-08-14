# macOS Monterey 12.1 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 12.1 SDK provides support to develop apps for Mac computers running macOS Monterey 12.1. The SDK comes bundled with Xcode 13.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 13.2, see [`Xcode 13.2 Release Notes`](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_2-release-notes).

##### App Store

###### New Features

- StoreKit APIs that present a refund request sheet can be tested with StoreKit Testing in Xcode. Use [`beginRefundRequest(in:)`](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(in:)-63bvd) or [`beginRefundRequest(for:in:)`](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)-9mscy) when working with AppKit or the `refundRequestSheet(for:isPresented:onDismiss:)` view modifier when working with SwiftUI. (70794860)

##### Displays

###### New Features

- You can now use graphics cards that integrate the AMD Radeon RX 6600 XT GPU. (82532062)

##### Icloud Mail

###### New Features

- iCloud+ subscribers can now access and use Hide My Email directly from the Mail app. (84956894)

##### Reminders

###### New Features

- Tags can now be bulk renamed and deleted. (82177979)

##### Swiftui

###### Resolved Issues

- Using [`alert(_:isPresented:actions:message:)`](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:message:)-6awwp) and `confirmationDialog(_:isPresented:titleVisibility:actions:)` now present. (83731075)

- Pushing a [`ScrollView`](https://developer.apple.com/documentation/swiftui/scrollview) that has a background applied while inside of a [`stack`](https://developer.apple.com/documentation/swiftui/navigationviewstyle/stack) style [`NavigationView`](https://developer.apple.com/documentation/swiftui/navigationview) when inside a [`TabView`](https://developer.apple.com/documentation/swiftui/tabview) is now correctly tracked by the [`navigationBar`](https://developer.apple.com/documentation/uikit/uinavigationcontroller/navigationbar) and [`tabBar`](https://developer.apple.com/documentation/uikit/uitabbarcontroller/tabbar). (83686857)

- [`List`](https://developer.apple.com/documentation/swiftui/list) correctly respects safe area insets. (83312573)
- The unnecessary New Document button in the Open Panel has been removed from document-based viewer apps. (84931806)

## See Also

- [macOS Monterey 12.5 Release Notes](macos-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.4 Release Notes](macos-12_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.3 Release Notes](macos-12_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.2 Release Notes](macos-12_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.0.1 Release Notes](macos-12_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-12_1-release-notes)*