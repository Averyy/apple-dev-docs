# tvOS 13 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 13 SDK provides support for developing tvOS apps for Apple TV devices running tvOS 13. The SDK comes bundled with Xcode 11 available from the Mac App Store. For information on the compatibility requirements for Xcode 11, see [`Xcode 11 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-11-release-notes).

##### Authenticationservices

###### Known Issues

- Passing both [`ASAuthorizationAppleIDProvider`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider) and [`ASAuthorizationPasswordProvider`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationPasswordProvider) to [`ASAuthorizationController`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationController) is not currently supported on tvOS. (50897359)

##### Avfoundation

###### New Features

- [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) now supports encoding video with alpha channels using HEVC. Videos encoded in this manner are broadly supported in AVFoundation APIs, and by Safari within web pages. Technical details of the format can be found in the Interoperability Profile specification. (8045917)

##### Mapkit

###### Known Issues

- [`MKMarkerAnnotationView`](https://developer.apple.com/documentation/MapKit/MKMarkerAnnotationView) doesn’t render the default glyph image. (52143655)  Set the [`glyphImage`](https://developer.apple.com/documentation/MapKit/MKMarkerAnnotationView/glyphImage) property on [`MKMarkerAnnotationView`](https://developer.apple.com/documentation/MapKit/MKMarkerAnnotationView) instances.
- [`MKMarkerAnnotationView`](https://developer.apple.com/documentation/MapKit/MKMarkerAnnotationView) doesn’t render the markers for annotations using the default tint color. (51908728)  Set the [`markerTintColor`](https://developer.apple.com/documentation/MapKit/MKMarkerAnnotationView/markerTintColor) property on [`MKMarkerAnnotationView`](https://developer.apple.com/documentation/MapKit/MKMarkerAnnotationView) instances.

##### Networking

###### Known Issues

- The [`urlSession(_:taskIsWaitingForConnectivity:)`](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/2908819-urlsession) delegate callback might not function as expected. (54309264)

###### Deprecations

- Removed support for FTP and File URL schemes for Proxy Automatic Configuration (PAC). HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including, but not limited to, configurations set using Settings, System Preferences, Profiles, and [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411499-connectionproxydictionary) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/CFNetwork/CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)). (28578280)
- The `URLSession` and [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) APIs no longer support SPDY. Servers should use HTTP 2 or HTTP 1.1. (43391641)

##### Swiftui

###### New Features

- The [`EnvironmentValues`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues) structure has four new properties for reading accessibility values from the environment: [`accessibilityDifferentiateWithoutColor`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityDifferentiateWithoutColor), [`accessibilityReduceTransparency`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityReduceTransparency), [`accessibilityReduceMotion`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityReduceMotion), and [`accessibilityInvertColors`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityInvertColors). (51712481)
- The `color(_:)` modifier for [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) is renamed [`foregroundColor(_:)`](https://developer.apple.com/documentation/SwiftUI/Text/foregroundColor(_:)) for consistency with the more general [`foregroundColor(_:)`](https://developer.apple.com/documentation/SwiftUI/View/foregroundColor(_:)) view modifier. (50391847)
- The `BindableObject` protocol’s requirement is now `willChange` instead of `didChange`, and should now be sent before the object changes rather than after it changes. This change allows for improved coalescing of change notifications. (51580731)
- The [`RangeReplaceableCollection`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection) protocol is extended to include a [`remove(atOffsets:)`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection/remove(atOffsets:)) method and the [`MutableCollection`](https://developer.apple.com/documentation/Swift/MutableCollection) protocol is extended to include a [`move(fromOffsets:toOffset:)`](https://developer.apple.com/documentation/Swift/MutableCollection/move(fromOffsets:toOffset:)) method. Each new method takes [`IndexSet`](https://developer.apple.com/documentation/Foundation/IndexSet) instances that you use with the doc://com.apple.documentation/documentation/swiftui/foreach/onmove(perform:) and doc://com.apple.documentation/documentation/swiftui/foreach/ondelete(perform:) modifiers on [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) views. (51991601)
- Added improved presentation modifiers: [`sheet(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/sheet(isPresented:onDismiss:content:)), [`actionSheet(isPresented:content:)`](https://developer.apple.com/documentation/SwiftUI/View/actionSheet(isPresented:content:)), and [`alert(isPresented:content:)`](https://developer.apple.com/documentation/SwiftUI/View/alert(isPresented:content:)) — along with `isPresented` in the environment — replace the existing `presentation(_:)`, `Sheet`, `Modal`, and `PresentationLink` types. (52075730)
- Updated the APIs for creating animations. The basic animations are now named after the curve type — such as [`linear`](https://developer.apple.com/documentation/SwiftUI/Animation/linear) and [`easeInOut`](https://developer.apple.com/documentation/SwiftUI/Animation/easeInOut). The interpolation-based `spring(mass:stiffness:damping:initialVelocity:)` animation is now [`interpolatingSpring(mass:stiffness:damping:initialVelocity:)`](https://developer.apple.com/documentation/SwiftUI/Animation/interpolatingSpring(mass:stiffness:damping:initialVelocity:)), and `fluidSpring(stiffness:dampingFraction:blendDuration:timestep:idleThreshold:)` is now [`spring(response:dampingFraction:blendDuration:)`](https://developer.apple.com/documentation/SwiftUI/Animation/spring(response:dampingFraction:blendDuration:)) or [`interactiveSpring(response:dampingFraction:blendDuration:)`](https://developer.apple.com/documentation/SwiftUI/Animation/interactiveSpring(response:dampingFraction:blendDuration:)), depending on whether or not the animation is driven interactively. (50280375)
- Added an initializer for creating a [`Font`](https://developer.apple.com/documentation/SwiftUI/Font) from a [`CTFont`](https://developer.apple.com/documentation/CoreText/CTFont). (51849885)

###### Known Issues

- [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) instances don’t use resizing information configured in asset catalogs. Configure the size of an image using the [`resizable(capInsets:resizingMode:)`](https://developer.apple.com/documentation/SwiftUI/Image/resizable(capInsets:resizingMode:)) modifier instead. (49114577)

###### Deprecations

- The `identified(by:)` method on the [`Collection`](https://developer.apple.com/documentation/Swift/Collection) protocol is deprecated in favor of dedicated `init(_:id:selection:rowContent:)` and `init(_:id:content:)` initializers. (52976883)
- The `relativeWidth(_:)`, `relativeHeight(_:)`, and `relativeSize(width:height:)` modifiers are deprecated. Use other modifiers like [`frame(width:height:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/frame(width:height:alignment:)) instead. (51494692)

##### Uikit

###### Known Issues

- Except for [`selectionIndicatorTintColor`](https://developer.apple.com/documentation/UIKit/UITabBarAppearance/selectionIndicatorTintColor), properties in the new tab bar appearance API aren’t reflected on the screen. (49792597)

##### Xcode

###### New Features

- [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) is now available in the Simulator. (45101325)

## See Also

- [tvOS 13.4.8 Release Notes](tvos-13_4_8-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.4.5 Release Notes](tvos-13_4_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.4 Release Notes](tvos-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.3.1 Release Notes](tvos-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.3 Release Notes](tvos-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.2 Release Notes](tvos-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-13-release-notes)*