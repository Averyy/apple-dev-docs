# Xcode 11.5 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 11.5 is available in the Mac App Store and includes SDKs for iOS 13.5, iPadOS 13.5, tvOS 13.4, watchOS 6.2, and macOS Catalina 10.15.4. The Xcode 11.5 release supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 11.5 requires a Mac running macOS Catalina 10.15.2 or later.

##### Apple Clang Compiler

###### Resolved Issues

- Fixed an issue with incorrect code generation when targeting armv7 devices. (61901594)

##### Asset Catalog

###### Known Issues

- watchOS and tvOS apps with asset catalogs built with Xcode 11.4 or later may experience slower image-loading performance on devices running on watchOS 6.1 or earlier, or when in Dark Mode on tvOS 13.3 or earlier. (62328605 : Add a symbol glyph to the app’s asset catalog.

###### Resolved Issues

- Restored image-loading performance for apps in Dark Mode on devices running iOS 13.3 or earlier. (61200701) (FB7648891)

##### Debugging

###### Resolved Issues

- Symbol names are no longer printed in stack frames in the console by default, as this combination can result in deadlocks when running Thread Sanitizer on simulated devices. For schemes that don’t have the option to gather code coverage enabled, you can re-enable symbol names and source locations by adding a `TSAN_OPTIONS` environment variable with the value `symbolize=1` in the scheme editor. (61840387)

##### Interface Builder

###### Resolved Issues

- Fixed a crash that could occur with connect-to-source when Control-dragging an object over a class with an `@end` keyword that shares a line with the previous item. (61957256)

##### Localization

###### Resolved Issues

- `genstrings` continues to look for additional instances of a localization token, such as “Text”, after finding it as part of an identifier. (61903372)
- When performing string extraction, `genstrings` only interprets SwiftUI constructs within Swift files. (60440513, 61903448)

##### Playgrounds

###### Resolved Issues

- Restored disclosure triangles for revealing the contents of playground books in Xcode’s project navigator. (61902475)

##### Signing and Distribution

###### Known Issues

- In a Mac app or an app built with Mac Catalyst, Xcode sometimes does not require a provisioning profile or include the Game Center entitlement. As a result, your app may fail to communicate with Game Center services at runtime. (62903631) : Add the following entitlement to your app’s entitlements plist: ```text
<key>com.apple.developer.game-center</key>
<true/>
```

###### Resolved Issues

- Fixed an issue that prevented automatic signing from making changes if the app IDs used a seed prefix and not a team ID prefix. (59672760) (FB7593038)

##### Simulator

###### Resolved Issues

- Fixed some issues where Xcode would sometimes fail to run an app in a simulated device, with an error “Timed out waiting for Simulator.app to become ready”. (57050823, 62542482) (FB7437899)
- Fixed a crash that could occur when invoking Siri in a simulated device. (62333338)

##### Swift

###### Resolved Issues

- Fixed a crash that could occur when using an opaque result type whose underlying type was not public. (60951353, 61902210) (FB7641416)
- Fixed a crash that occurred when declaring a property with an attached property wrapper that had the same name as another property in the same scope. (61902377)

## See Also

- [Xcode 11.7 Release Notes](xcode-11_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.6 Release Notes](xcode-11_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4.1 Release Notes](xcode-11_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4 Release Notes](xcode-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.3.1 Release Notes](xcode-11_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-11_5-release-notes)*