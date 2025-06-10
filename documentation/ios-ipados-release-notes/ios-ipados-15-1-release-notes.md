# iOS & iPadOS 15.1 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 15 SDK provides support to develop apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 15.1. The SDK comes bundled with Xcode 13, available from the Mac App Store. For information on the compatibility requirements for Xcode 13, see [`Xcode 13 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13-release-notes).

##### Coredata

###### Known Issues

- `NSExpression` immediately forbids certain operations that have significant side effects, like creating and destroying objects. Additionally, casting string class names into Class objects with `NSConstantValueExpression` is deprecated. (84017178)  Pass temporary objects to `NSExpression` in the context parameter of [`expressionValue(with:context:)`](https://developer.apple.com/documentation/Foundation/NSExpression/expressionValue(with:context:)), or with `NSPredicate` as the `substitutionVariables` parameter of [`evaluate(with:substitutionVariables:)`](https://developer.apple.com/documentation/Foundation/NSPredicate/evaluate(with:substitutionVariables:)). You can create a derived predicate with all the substitution variables replaced (bound), using [`withSubstitutionVariables(_:)`](https://developer.apple.com/documentation/Foundation/NSPredicate/withSubstitutionVariables(_:)) on an existing `NSPredicate` so that code using the object can continue to use a simple `evaluate(with object: Any?)` invocation.

##### Home

###### Known Issues

- The query for the connected admin list isn’t supported by Matter accessories. (82398328)
- Matter accessory notifications don’t work. (82634464)  Relaunch the Home app to force a refresh of the Matter accessory state.

##### Shareplay

###### New Features

- SharePlay is now available in iOS 15.1, iPadOS 15.1, and tvOS 15.1. You can submit your apps that support SharePlay now. It’s also enabled in macOS 12.1 beta, so you can build SharePlay experiences across Apple platforms using the  [`Group Activities`](https://developer.apple.com/documentation/GroupActivities) entitlement, without the need for the SharePlay Development Profile.

##### Swiftui

###### Known Issues

- The [`BorderedButtonStyle`](https://developer.apple.com/documentation/SwiftUI/BorderedButtonStyle) no longer has a default hover effect.  Use the [`HoverEffect`](https://developer.apple.com/documentation/SwiftUI/HoverEffect) modifier on the [`Button`](https://developer.apple.com/documentation/SwiftUI/Button). (81759097)

##### Telephony

###### Known Issues

- Users might experience loss of audio during calls, followed by the call being dropped in some conditions. (83381816)  Toggle Airplane Mode on and off, or reboot.

##### Voiceover

###### Resolved Issues

- Alarms now activate correctly in the Clock app. (82968832)

## See Also

- [iOS & iPadOS 15.6 Release Notes](ios-ipados-15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.5 Release Notes](ios-ipados-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.4 Release Notes](ios-ipados-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.3 Release Notes](ios-ipados-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.2 Release Notes](ios-ipados-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15 Release Notes](ios-ipados-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15_1-release-notes)*