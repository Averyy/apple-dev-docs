# watchOS 27.3 Beta Release Notes

**Framework**: watchOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The watchOS 27.3 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 27.3 beta. The SDK comes bundled with Xcode 27.3. For information on the compatibility requirements for Xcode 27.3, see [Xcode 27.3 Release Notes](../Xcode-Release-Notes/xcode-27_3-release-notes.md).

### StoreKit Testing in Xcode

#### Resolved Issues

- Fixed: Making an in-app purchase for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)

#### Known Issues

- When you launch an app that uses `SKTestSession` for the first time, some StoreKit Test API calls might hang. (186670057) (FB24651858)

  **Workaround:** Set a StoreKit configuration file in your scheme’s run options, then rerun the tests.

## See Also

### watchOS 27
- [watchOS 27.2 Release Notes](./watchos-27_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 27 Release Notes](./watchos-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-27_3-release-notes)*