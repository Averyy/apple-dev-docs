# iOS & iPadOS 14.3 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 14.3 SDK provides support to develop apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 14.3. The SDK comes bundled with Xcode 12.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 12.3, see [`Xcode 12.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-12_3-release-notes).

##### App Clips

###### New Features

- You can now launch an App Clip by scanning App Clip Codes designed by Apple, by using Camera or from Control Center. (71991284)

##### Skadnetwork

###### Known Issues

- To receive a postback from devices running iOS 14 or later, generate signatures using signature version 2.0 or later. Version 1.0 signatures don’t result in a postback on iOS 14 and later, even if the advertised app is installed and launched. (71474331)

##### Weather

###### New Features

- Air-quality health recommendations are now provided at specific air-quality levels for the United States, UK, Germany, India, and Mexico. Air-quality data is now provided by BreezoMeter. (61549519, 69005714)
- Air-quality data is now available for specific locations in China mainland, and is provided by QWeather. (69005588)
- Air-quality data for Germany now reflects the updated UBA scale. (66450687)
- Air-quality data for Mexico now uses the ICARS scale. (66450687)

##### Web Clips

###### Deprecations

The `TargetApplicationBundleIdentifier` in [`WebClip`](https://developer.apple.com/documentation/DeviceManagement/WebClip) is intended for enterprise customers to launch a custom URL in a third-party browser, rather than to provide theming options. Beginning in iOS & iPadOS 14.3, pointing `TargetApplicationBundleIdentifier` to an app made by Apple is no longer supported. A Web Clip already installed via a configuration profile will continue to work; however, the `TargetApplicationBundleIdentifier` property will be ignored in newly installed Web Clips unless the configuration profile is deployed via MDM. For devices not enrolled in MDM, create a single-step shortcut with the Open App action, then add the shortcut to the Home screen. (71422092)

## See Also

- [iOS & iPadOS 14.7 Release Notes](ios-ipados-14_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.6 Release Notes](ios-ipados-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5.1 Release Notes](ios-ipados-14_5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5 Release Notes](ios-ipados-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.4 Release Notes](ios-ipados-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.2 Release Notes](ios-ipados-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14 Release Notes](ios-ipados-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-14_3-release-notes)*