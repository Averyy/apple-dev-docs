# macOS Mojave 10.14.6 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 10.14.6 SDK provides support for developing apps for Macs running macOS Mojave 10.14.6. The SDK comes bundled with Xcode 10.3 available from the Mac App Store. For information on the compatibility requirements for Xcode 10.3, see [`Xcode 10.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-10_3-release-notes).

##### Security

###### Resolved Issues

- The system now registers tickets stapled to installer packages that aren’t scanned by Gatekeeper. As a result, newly installed kernel extensions load properly when internet access is unavailable, which can occur if a user launches installation from a local folder or an enterprise uses automated tools to deploy an installer. If you’re deploying an app to macOS Mojave 10.14.5, follow the workaround listed in the  section of [`macOS Mojave 10.14.5 Release Notes`](macos-mojave-10_14_5-release-notes.md). (50205533)

## See Also

- [macOS Mojave 10.14.5 Release Notes](macos-mojave-10_14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.4 Release Notes](macos-mojave_10_14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.3 Release Notes](macos-mojave-10_14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.2 Release Notes](macos-mojave-10_14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14 Release Notes](macos-mojave-10_14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-mojave-10_14_6-release-notes)*