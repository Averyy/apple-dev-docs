# macOS Mojave 10.14.5 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 10.14.4 SDK provides support for developing apps for Macs running macOS Mojave 10.14.5. The SDK comes bundled with Xcode 10.2.1 available from the Mac App Store. For information on the compatibility requirements for Xcode 10.2.1, see [`Xcode 10.2.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-10_2_1-release-notes).

##### Accessibility

###### Resolved Issues

- The Accessibility Events switch was removed, because related aspects of the W3C AOM effort are no longer applicable. (49784417)

##### Date and Time

###### New Features

- Support for the Reiwa (令和) era of the Japanese calendar, which began on May 1, 2019, is now available. The first year of Japanese-calendar era is represented as  “元年” (“Gannen”) instead of “1年”, except in the shorter numeric-style formats which typically also use the narrow era name; for example: “R1/05/01”. (27323929)

##### Security

###### New Features

- Kernel extensions signed after April 7, 2019 must be notarized in order to load on macOS 10.14.5. (50016570)

###### Known Issues

- The system fails to register tickets stapled to installer packages not scanned by Gatekeeper, which causes newly installed kernel extensions to fail to load if Internet access isn’t available. This can occur if a user launches installation from a local folder or an enterprise uses automated tools to deploy an installer. This issue doesn’t affect stapled disk images, apps, or kext bundles. (50205533)  In a new folder, create a shell script named `preinstall` to register the stapled ticket during install: ```bash
#!/bin/sh
if [[ `/usr/bin/sw_vers -productVersion` == 10.14.5 ]]; then
    /usr/sbin/spctl -a -vvv -t install "$PACKAGE_PATH"; fi
``` Then, when creating the flat package installer using either the `pkgbuild` or `productbuild` tool, pass the `--scripts <path to folder containing preinstall>` option to embed the preinstall script into the finalized installer.

## See Also

- [macOS Mojave 10.14.6 Release Notes](macos-mojave-10_14_6-release-notes.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-mojave-10_14_5-release-notes)*