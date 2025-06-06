# Xcode 11.3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes

#### Overview

Xcode 11.3 supports developing apps for iOS 13.3, iPadOS 13.3, tvOS 13.3, watchOS 6.1, and macOS Catalina 10.15.2. Xcode 11.3 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 11.3 requires a Mac running macOS Mojave 10.14.4 or later.

##### General

###### New Features

- You can configure the Touch Bar simulator to simulate either 1st generation or 2nd generation Touch Bars. (53885368)

###### Known Issues

- When you create an Objective-C category file by choosing File > New > File…, the newly created file includes an import of the AppKit framework. This causes a compilation error for iOS, tvOS, and watchOS. (55977950) (FB7346800) : Remove the import of AppKit from the source file.

##### Create Ml

###### New Features

- A Recommender template is available in Create ML, joining the Image, Sound, Activity, Text and Tabular Classification, Object Detection, Word Tagging and Tabular Regression templates. (56912822)

##### Interface Builder

###### Known Issues

- The color picker panel does not respond to choosing a color while a text field in the inspector has insertion focus. (56067005) (FB7358220) : Click the Interface Builder canvas to remove focus from the text field, then choose a color in the panel.

###### Resolved Issues

- Setting the Selected Segment Tint Color of a segmented control in Interface Builder to a named color doesn’t cause a failure when the view loads on iOS 12 and earlier. (55254963, 55951374)
- Fixed rendering issues for scenes with large simulated metric free-form sizes. (56920189)

##### Previews

###### New Features

- Xcode Previews now use a platform-provided scroll view for the canvas content when running on macOS Catalina 10.15.2 or newer. This change makes it possible to scroll through the canvas using a scroll wheel on a mouse, as well as by dragging horizontal and vertical scrollbars. (53962570)

##### Simulator

###### Known Issues

- Third party “endpoint security” software may cause slow simulators, system freezes, or prevent debug processes from running in simulators reliably. This sometimes manifests as `debugserver` disconnections, or sends simulator applications a `SIGKILL` signal. (55853555) : Uninstall the third party software.
- Under certain network conditions, GateKeeper may block simulators from booting, and show error code 60 `"launchd` failed to respond.” (55878667) : Try to boot the simulator again. Disabling WiFi or disconnecting from any active VPNs may resolve the problem.
- When a new Mac Pro has multiple GPUs, Simulator assigns each booted simulator to one of the available GPUs. (56488185)

##### Swift Packages

###### Resolved Issues

- You can now submit iOS, tvOS, or watchOS apps with a Swift Package that builds a dynamic library. (55564324) (FB7303066)

## See Also

- [Xcode 11.7 Release Notes](xcode-11_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.6 Release Notes](xcode-11_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.5 Release Notes](xcode-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4.1 Release Notes](xcode-11_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4 Release Notes](xcode-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.3.1 Release Notes](xcode-11_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
- [Xcode 11.2.1 Release Notes](xcode-11_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.2 Release Notes](xcode-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.1 Release Notes](xcode-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11 Release Notes](xcode-11-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-11_3-release-notes)*