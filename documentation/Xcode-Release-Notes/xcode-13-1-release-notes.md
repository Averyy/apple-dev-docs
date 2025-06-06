# Xcode 13.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 13.1 includes SDKs for iOS 15, iPadOS 15, tvOS 15, watchOS 8, and macOS Monterey 12. The Xcode 13.1 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 13.1 requires a Mac running macOS 11.3 or later.

##### Debugging

###### Known Issues

- Console, Xcode, `lldb`, and debugging tools can’t symbolicate crash logs that macOS transfers from connected devices running iOS 15, watchOS 8, or tvOS 15. (78124467, 83760462, 84048036, 84048399) (FB9669482) : Use Xcode’s Devices & Simulators window > View Device Logs to import log files from connected devices, and transform them into a human-readable form. You can also access crash logs directly on iOS devices using the Settings app under Privacy > Analytics > Analytics Data and use the share sheet to transfer them to a Mac without any loss of information. Open the resulting log files using Console, or by dragging and dropping them onto Xcode in the Dock.

##### Interface Builder

###### Resolved Issues

- Fixed rendering issues that affected [`UITableView`](https://developer.apple.com/documentation/UIKit/UITableView) for some iOS storyboards. (82731572, 83465487)
- Fixed an issue where iPhone 13 mini wouldn’t rotate to landscape orientation. (83465491)

##### Source Control

###### Known Issues

- Adding commits to a pull request in Xcode may not update the Changes navigator until you re-launch Xcode. (70398244) : Re-launch Xcode.
- The Recent Branches section may continue to display an Upstream Arrow on a branch after you push changes on that branch. (80597226) : Restart Xcode to update the status.
- Xcode may not correctly format code in pull request comments. (82143328)
- Xcode may forget or reject credentials for GitLab Self-Hosted accounts. (82501314)
- Repositories Navigator may sometimes display the current branch indicator on multiple branches. (82629835) : Re-launch Xcode or wait for the status of these files to update.
- In Flat view mode, the Commit sheet may sometimes present without selecting a file. (83417116)

##### Swiftui

###### Known Issues

- In Previews and in simulated iOS 15 devices, [`Button`](https://developer.apple.com/documentation/SwiftUI/Button) elements support the iPad cursor hover states by default, but in iOS 15.1 [`BorderedButtonStyle`](https://developer.apple.com/documentation/SwiftUI/BorderedButtonStyle) no longer has a default hover effect. Use the [`HoverEffect`](https://developer.apple.com/documentation/SwiftUI/HoverEffect) modifier on the `Button` to add a default hover effect when running in iOS 15.1. (83516916)

## See Also

- [Xcode 13.4.1 Release Notes](xcode-13_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.4 Release Notes](xcode-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3.1 Release Notes](xcode-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3 Release Notes](xcode-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2.1 Release Notes](xcode-13_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2 Release Notes](xcode-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13 Release Notes](xcode-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_1-release-notes)*