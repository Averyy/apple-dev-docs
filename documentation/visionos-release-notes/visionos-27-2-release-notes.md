# visionOS 27.2 Beta 2 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 27.2 SDK provides support to develop apps for Apple Vision Pro devices running visionOS 27.2 beta 2. The SDK comes bundled with Xcode 27.2. For information on the compatibility requirements for Xcode 27.2, see [`Xcode 27.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-27_2-release-notes).

##### Quick Look

###### Known Issues

- 3D objects opened from Safari might reposition unexpectedly when you move them. (187035825)

##### Storekit Testing in Xcode

###### Resolved Issues

- Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`. (183933307) (FB24137836)
- Fixed: Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`. (184155259)
- Fixed: Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to true. (184255116)

###### Known Issues

- Making a purchase in-app for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)

## See Also

- [visionOS 27 Release Notes](visionos-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-27_2-release-notes)*