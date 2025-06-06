# Xcode 13.4 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 13.4 includes SDKs for iOS 15.5, iPadOS 15.5, tvOS 15.4, watchOS 8.5, and macOS Monterey 12.3. The Xcode 13.4 release supports on-device debugging for iOS 15.5, iPadOS 15.5, tvOS 15.4, watchOS 8.5, and later. Xcode 13.4 requires a Mac running macOS Monterey 12 or later.

##### Build System

###### Known Issues

- Swift Playgrounds app projects with package dependencies fail to build for Mac Catalyst when a package specifies `.iOS(...)` in its `platforms` array in the manifest, but doesn’t specify `.macCatalyst(...)`. (88726762) : Add `.macCatalyst(...)` to the `platforms` array with the same value as the `iOS(...)` entry.

##### Devices

###### Known Issues

- Xcode 13.4 is unable to prepare devices running iOS 15.6 beta for development. (93452791) : Use Xcode 13.3.1.

##### Localization

###### Resolved Issues

- Fixed an issue where Xcode was sometimes unable to build or close after failing to export localizations. (91161985)

##### Reality Composer

###### Known Issues

- Using the Reality Composer app or previewing Reality Composer projects in Xcode may lead to a crash on Mac systems with AMD GPU: MacBook Pro (15-inch, Late 2016), MacBook Pro (15-inch, 2019), iMac Pro (2017). (92637801) : Use Xcode 13.3.

##### Signing and Distribution

###### Resolved Issues

- Fixed an issue with generating symbols for Quick Look plug-ins during app distribution. (91361932)

##### Source Control

###### Known Issues

- Users can’t onboard with an Apple ID that hasn’t been upgraded to use two-factor authentication. (92041517) : Upgrade your Apple ID to use two-factor authentication.
- The workflow editor doesn’t show test plans for schemes that have been recently converted to test plans. (92053036) : Convert to test plans, commit and push your changes to your remote repository before onboarding.

##### Swift

###### Resolved Issues

- Fixed a compiler issue that caused a runtime crash in `NativeSet` when back deploying to iOS 15.3 or earlier. (90666260)
- The async version of `addTeardownBlock` method in `XCTestCase` is now available. (90665371)
- Closures that are guaranteed to run on the main actor are now permitted to reference local variables from their enclosing scopes that are also running on the main actor. ```swift
@MainActor
class MyController: UIViewController {
  var isExcited: Bool = false
  
  func doSomething() {
    var title = "Hello"

    Task { @MainActor in
      if isExcited { // okay, accessing main actor-isolated stored property
        title += "!" // okay, accessing main actor-isolated local variable
      }
    }
  }
}
```

(90665432)

##### Swift Packages

###### Resolved Issues

- Fixed a bug that prevented Swift Packages from finding a package plug-in tool if a target in a different package than the plug-in that requires it built the tool. (90650826)

##### Testing

###### Known Issues

- Xcode crashes if you attempt to run unit or UI tests for watchOS apps when the Run scheme action’s executable is set to None. (74928871) : Set the Run scheme action’s executable to a valid WatchKit app target built by the scheme.

## See Also

- [Xcode 13.4.1 Release Notes](xcode-13_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3.1 Release Notes](xcode-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3 Release Notes](xcode-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2.1 Release Notes](xcode-13_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2 Release Notes](xcode-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.1 Release Notes](xcode-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13 Release Notes](xcode-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_4-release-notes)*