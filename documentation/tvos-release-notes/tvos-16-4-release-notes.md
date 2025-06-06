# tvOS 16.4 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 16.4 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 16.4. The SDK comes bundled with Xcode 14.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 14.3, see [`Xcode 14.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_3-release-notes).

##### Home

###### New Features

- Both manual and automatic Software Update support is now available for Matter Accessories. (102727759)

##### Swiftui

###### Resolved Issues

- Fixed: `ScrollView` has improved support for right to left languages by default. If you have a `ScrollView` that shouldn’t change its behavior in right to left languages, use the `.environment(\.layoutDirection, .leftToRight)` modifier to ensure the `ScrollView` always sees a left to right layout direction. (65108729)
- Fixed: Search scopes are now supported on tvOS. (84039097)
- Fixed: Presentations in SwiftUI using the ‘sheet’ or ‘fullScreenCover’ modifier can now be dynamically presented again while a dismiss animation is in progress. Previously, attempting to present again in this case would do nothing. Note: A data race in app code that was previously ignored might cause a sheet to be presented again with this change. If this happens, check that your state isn’t triggering a new presentation. (101487810)

## See Also

- [tvOS 16.6 Release Notes](tvos-16_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.5 Release Notes](tvos-16_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.3 Release Notes](tvos-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.2 Release Notes](tvos-16_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.1 Release Notes](tvos-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 16 Release Notes](tvos-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-16_4-release-notes)*