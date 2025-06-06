# Xcode 12.4 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 12.4 includes SDKs for iOS 14.4, iPadOS 14.4, tvOS 14.3, watchOS 7.2, and macOS Big Sur 11.1. The Xcode 12.4 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 12.4 requires a Mac running macOS 10.15.4 or later.

##### Debugging

###### Known Issues

- Xcode may hang if the host Mac is connected to an iOS device which has one or more companion watches. The hangs occur when the watches aren’t fully prepared for development, or if they are experiencing poor wireless connectivity. (72490921) (FB8945320) : Power off the watches, or unpair them from the iPhone.

You can force Xcode to freshly prepare a watch for development using these steps:

1. Force-quit Xcode.
2. Power-off and disconnect all iOS device from the Mac.
3. Reboot the Mac.
4. Launch Xcode, close all projects, and open the Devices and Simulators window.
5. Power-on and unlock an iOS device and its companion watchOS devices by entering the passcode as required.
6. Plug the iOS device into the Mac using USB cable.
7. Check each iOS device and each watch for any pairing request and approve the requests.
8. Monitor the status of device preparation in the Devices and Simulators window. If Xcode presents device-preparation errors, follow the guidance in the error message to resolve the error.

Once Xcode finishes preparing the iOS device and its companion watches for development, repeat steps 5 through 8 for each remaining iOS device and its companion watches until you verify that Xcode has prepared all devices for development. You may now open your Xcode projects and resume development.

##### Sanitizers

###### Resolved Issues

- Fixed a crash that could occur when launching an application with Thread Sanitizer enabled on a Mac with Apple silicon. (72129387, 72262222, 72449940) (FB8933994, FB8938284)

##### Simulator

###### Resolved Issues

- iOS simulated devices no longer display an incorrect yellow tint in translucent UI elements. Certain GPUs may continue to display the tint with some tvOS simulators. (71203015)
- Fixed an issue that could prevent iOS apps from launching on Macs with Apple silicon. (72360675)

##### Swift Packages

###### Known Issues

- If you use a Swift package with binary dependencies in an app with extensions, the build system incorrectly embeds the binary dependencies alongside the extension in the PlugIns directory, causing validation of the archived app to fail. (69834549) (FB8761306) : Add a scheme post-build action which removes the embedded binaries from the PlugIns directory after the build, e.g. `rm -rf "${TARGET_BUILD_DIR}/${TARGET_NAME}.app"/PlugIns/*.framework`.

## See Also

- [Xcode 12.5.1 Release Notes](xcode-12_5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.5 Release Notes](xcode-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.3 Release Notes](xcode-12_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.2 Release Notes](xcode-12_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.1 Release Notes](xcode-12_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.0.1 Release Notes](xcode-12_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12 Release Notes](xcode-12-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-12_4-release-notes)*