# macOS 27.2 Golden Gate Beta Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 27.2 SDK provides support to develop apps for Mac computers running macOS 27.2 Golden Gate beta. The SDK comes bundled with Xcode 27.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 27.2, see [`Xcode 27.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-27_2-release-notes).

##### Notifications

###### Known Issues

- Mac computers with a clean install of this build might not prompt you to allow notifications for some apps, such as Calendar, Maps, Find My, Home, and Weather. (187312007) **Workaround:** Go to System Settings > Notifications to manually turn on notifications for the affected apps.

##### Shortcuts

###### Known Issues

- Describe a Shortcut might fail with the error “Something went wrong. Try again later.” (187499433)

##### Storekit Testing in Xcode

###### Resolved Issues

- Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`. (183933307) (FB24137836)
- Fixed: Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`. (184155259)
- Fixed: Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to true. (184255116)

###### Known Issues

- Making a purchase in-app for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)

## See Also

- [macOS 27 Golden Gate Release Notes](macos-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes)*