# Xcode 11.3.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes

#### Overview

Xcode 11.3.1 supports developing apps for iOS 13.3, iPadOS 13.3, tvOS 13.3, watchOS 6.1, and macOS Catalina 10.15.2. Xcode 11.3.1 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 11.3.1 requires a Mac running macOS Mojave 10.14.4 or later.

##### General

###### Known Issues

- When you create an Objective-C category file by choosing File > New > File, the newly created file includes an import of the AppKit framework. This causes a compilation error for iOS, tvOS, and watchOS. (55977950) (FB7346800)  Remove the import of AppKit from the source file.

##### Debugging

###### Resolved Issues

- Inspection of global variables in Swift and Objective-C works properly in `lldb`. (57884467)

##### Interface Builder

###### Resolved Issues

- Fixed a crash that could occur when using an attributed string in a [`UILabel`](https://developer.apple.com/documentation/UIKit/UILabel). (55737956, 57990674)
- Fixed a crash that could occur after dragging a toolbar item out of the Allowed set in the canvas. (18133890, 57982132)

##### Simulator

###### Resolved Issues

- Fixed an issue that would cause Xcode to time out waiting for Simulator.app to become ready, when multiple copies of Xcode are installed. (57050823, 57676897)
- Resolved an issue that prevented Xcode from launching processes with Thread Sanitizer enabled on macOS Catalina 10.15.2. (57822138)

##### Source Editor

###### Resolved Issues

- Fixed a crash that could occur when typing a doc comment after invoking undo. (56522994, 57762965)

##### Swift

###### Resolved Issues

- Reduced the size of dependency files (`.d`) produced by the Swift compiler, which can improve incremental build times and disk usage for targets with many source files. (57361722, 57865813)

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
- [Xcode 11.3 Release Notes](xcode-11_3-release-notes.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-11_3_1-release-notes)*