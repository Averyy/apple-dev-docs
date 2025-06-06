# macOS Monterey 12.0.1 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 12 SDK provides support to develop apps for Mac computers running macOS Monterey 12.0.1. The SDK comes bundled with Xcode 13.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 13.1, see [`Xcode 13.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13_1-release-notes).

##### Appkit

- See [`AppKit Release Notes for macOS Monterey 12`](appkit-release-notes-for-macos-12.md).

##### Displays Preferences

###### Known Issues

- There might be issues with wakeup when dual monitors are connected. (79839446)  Connect the power adapter that came with the Mac.

##### Coredata

###### Known Issues

- `NSExpression` immediately forbids certain operations that have significant side effects, like creating and destroying objects. Additionally, casting string class names into Class objects with `NSConstantValueExpression` is deprecated. (84017178)  Pass temporary objects to `NSExpression` in the context parameter of [`expressionValueWithObject:context:`](https://developer.apple.com/documentation/foundation/nsexpression/1410363-expressionvaluewithobject), or with `NSPredicate` as the `substitutionVariables` parameter of [`evaluateWithObject:substitutionVariables:`](https://developer.apple.com/documentation/foundation/nspredicate/1407759-evaluatewithobject). You can create a derived predicate with all the substitution variables replaced (bound), using [`withSubstitutionVariables(_:)`](https://developer.apple.com/documentation/foundation/nspredicate/1413227-withsubstitutionvariables) on an existing `NSPredicate` so that code using the object can continue to use a simple `evaluate(with object: Any?)` invocation.

##### Icloud

###### Known Issues

- Legacy Contacts has been removed from macOS Monterey 12 beta 5 and will return in a future release. (81292890)

- Custom Email Domain addresses that are associated with a separate iTunes account can’t be configured. (82358431)

##### Mac Catalyst

###### Known Issues

- Setting the title color of a [`UIButton`](https://developer.apple.com/documentation/UIKit/UIButton) doesn’t work regardless of whether you use [`baseForegroundColor`](https://developer.apple.com/documentation/UIKit/UIButton/Configuration-swift.struct/baseForegroundColor) or [`titleColor(for:)`](https://developer.apple.com/documentation/UIKit/UIButton/titleColor(for:)). (76566253)

##### Maps

###### Deprecations

- [`MKPinAnnotationView`](https://developer.apple.com/documentation/MapKit/MKPinAnnotationView) and [`MapPin`](https://developer.apple.com/documentation/MapKit/MapPin) are deprecated in this beta. (78536295)

###### Known Issues

- Rounded building corners might disappear. (80468151)

##### Networking

###### Deprecations

- Support for cleartext HTTP URL schemes for Proxy Automatic Configuration (PAC) is now deprecated. Use only HTTPS URL schemes for PAC. This affects all PAC configurations, including, but not limited to, configurations set via Settings, System Preferences, profiles, and `URLSession` APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411499-connectionproxydictionary) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/CFNetwork/CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)). If you configure a cleartext HTTP PAC URL, the system may upgrade it to HTTPS during PAC file loads. Web Proxy Auto-Discovery (WPAD) Protocol via DNS isn’t affected. Dynamic Host Configuration Protocol (DHCP) Option 252 WPAD may attempt to upgrade cleartext HTTP URLs to HTTPS during PAC file loads. (61981845)

##### Python

###### Deprecations

- If an app uses Python 2.7, macOS now triggers an alert indicating that the developer must update the app to ensure it will work in future versions of macOS. (80221011)

##### Realitykit

###### Known Issues

- The `StreamingInput` init on [`PhotogrammetrySession`](https://developer.apple.com/documentation/RealityKit/PhotogrammetrySession) isn’t supported. (78838906)

##### Shareplay

###### Deprecations

- SharePlay development in macOS Monterey beta 6 and upcoming beta releases requires the installation of an updated [`SharePlay Development Profile`](https://developer.apple.comhttps://developer.apple.com/download/). This profile enables successful creation and reception of GroupSessions via the Group Activities API in iOS 15, iPadOS 15, and tvOS 15 beta 7, as well as macOS Monterey beta 6. (81900143)

##### Swift

###### Known Issues

- Applications linking to RealityKit with the iOS 15 or macOS 12 SDKs will fail to launch on a previous OS. (79584511)  Add `OTHER_LD_FLAGS = -weak_framework RealityFoundation` to your Xcode Project settings to allow running RealityKit apps on an older OS.

##### Swiftui

###### Deprecations

- `controlProminence` is deprecated. Use the new `.borderedProminent` [`ButtonStyle`](https://developer.apple.com/documentation/SwiftUI/ButtonStyle) instead. (78908460)

- `Fn` (`Function`) shortcut modifier is deprecated and reserved for system usage. (78627099)

## See Also

- [macOS Monterey 12.5 Release Notes](macos-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.4 Release Notes](macos-12_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.3 Release Notes](macos-12_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.2 Release Notes](macos-12_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.1 Release Notes](macos-12_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-12_0_1-release-notes)*