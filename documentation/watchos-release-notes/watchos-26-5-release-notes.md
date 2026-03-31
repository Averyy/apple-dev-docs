# watchOS 26.5 Beta Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 26.5 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 26.5 beta. The SDK comes bundled with Xcode 26.5, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.5, see [`Xcode 26.5 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_5-release-notes).

##### Storekittest

###### Known Issues

- `SKTestSession` cannot use the selected StoreKit configuration during unit tests, resulting in failed test actions.  (172583218) (FB22237318) **Workaround:** To use `SKTestSession` in 26.3 and 26.4, build and run the app on device using the same StoreKit configuration as the test. Then close the app and run the unit test using `SKTestSession` without changing any configuration settings in the test environment. This allows the configuration to be saved on device before the test begins and maintain your selected configuration settings through the test session.

## See Also

- [watchOS 26.4 Release Notes](watchos-26_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.3 Release Notes](watchos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.2 Release Notes](watchos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.1 Release Notes](watchos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26 Release Notes](watchos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-26_5-release-notes)*