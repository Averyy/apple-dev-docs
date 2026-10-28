# tvOS 13 Release Notes

**Framework**: tvOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The tvOS 13 SDK provides support for developing tvOS apps for Apple TV devices running tvOS 13. The SDK comes bundled with Xcode 11. For information on the compatibility requirements for Xcode 11, see [Xcode 11 Release Notes](../Xcode-Release-Notes/xcode-11-release-notes.md).

### AuthenticationServices

#### Known Issues

- Passing both [`ASAuthorizationAppleIDProvider`](../AuthenticationServices/asauthorizationappleidprovider.md) and [`ASAuthorizationPasswordProvider`](../AuthenticationServices/asauthorizationpasswordprovider.md) to [`ASAuthorizationController`](../AuthenticationServices/asauthorizationcontroller.md) is not currently supported on tvOS. (50897359)

### AVFoundation

#### New Features

- [AVFoundation](../AVFoundation/AVFoundation.md) now supports encoding video with alpha channels using HEVC. Videos encoded in this manner are broadly supported in AVFoundation APIs, and by Safari within web pages. Technical details of the format can be found in the Interoperability Profile specification. (8045917)

### MapKit

#### Known Issues

- [`MKMarkerAnnotationView`](../MapKit/mkmarkerannotationview.md) doesn’t render the default glyph image. (52143655)

  **Workaround:** Set the [`glyphImage`](../MapKit/mkmarkerannotationview/glyphimage.md) property on [`MKMarkerAnnotationView`](../MapKit/mkmarkerannotationview.md) instances.
- [`MKMarkerAnnotationView`](../MapKit/mkmarkerannotationview.md) doesn’t render the markers for annotations using the default tint color. (51908728)

  **Workaround:** Set the [`markerTintColor`](../MapKit/mkmarkerannotationview/markertintcolor.md) property on [`MKMarkerAnnotationView`](../MapKit/mkmarkerannotationview.md) instances.

### Networking

#### Known Issues

- The [`urlSession(_:taskIsWaitingForConnectivity:)`](../Foundation/urlsessiontaskdelegate/urlsession%28_,taskiswaitingforconnectivity%29.md) delegate callback might not function as expected. (54309264)

#### Deprecations

- Removed support for FTP and File URL schemes for Proxy Automatic Configuration (PAC). HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including, but not limited to, configurations set using Settings, System Preferences, Profiles, and [`URLSession`](../Foundation/urlsession.md) APIs such as [`connectionProxyDictionary`](../Foundation/urlsessionconfiguration/connectionproxydictionary.md) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](../CFNetwork/cfnetworkexecuteproxyautoconfigurationurl%28_,_,_,_%29.md). (28578280)
- The `URLSession` and [`NSURLConnection`](../Foundation/nsurlconnection.md) APIs no longer support SPDY. Servers should use HTTP 2 or HTTP 1.1. (43391641)

### SwiftUI

#### New Features

- The [`EnvironmentValues`](../SwiftUI/environmentvalues.md) structure has four new properties for reading accessibility values from the environment: [`accessibilityDifferentiateWithoutColor`](../SwiftUI/environmentvalues/accessibilitydifferentiatewithoutcolor.md), [`accessibilityReduceTransparency`](../SwiftUI/environmentvalues/accessibilityreducetransparency.md), [`accessibilityReduceMotion`](../SwiftUI/environmentvalues/accessibilityreducemotion.md), and [`accessibilityInvertColors`](../SwiftUI/environmentvalues/accessibilityinvertcolors.md). (51712481)
- The `color(_:)` modifier for [`Text`](../SwiftUI/text.md) is renamed [`foregroundColor(_:)`](../SwiftUI/text/foregroundcolor%28_%29.md) for consistency with the more general [`foregroundColor(_:)`](../SwiftUI/view/foregroundcolor%28_%29.md) view modifier. (50391847)
- The `BindableObject` protocol’s requirement is now `willChange` instead of `didChange`, and should now be sent before the object changes rather than after it changes. This change allows for improved coalescing of change notifications. (51580731)
- The [`RangeReplaceableCollection`](../Swift/rangereplaceablecollection.md) protocol is extended to include a [`remove(atOffsets:)`](../Swift/rangereplaceablecollection/remove%28atoffsets%29.md) method and the [`MutableCollection`](../Swift/mutablecollection.md) protocol is extended to include a [`move(fromOffsets:toOffset:)`](../Swift/mutablecollection/move%28fromoffsets,tooffset%29.md) method. Each new method takes [`IndexSet`](../Foundation/indexset.md) instances that you use with the `onMove(perform:)` and `onDelete(perform:)` modifiers on [`ForEach`](../SwiftUI/foreach.md) views. (51991601)
- Added improved presentation modifiers: [`sheet(isPresented:onDismiss:content:)`](../SwiftUI/view/sheet%28ispresented,ondismiss,content%29.md), [`actionSheet(isPresented:content:)`](../SwiftUI/view/actionsheet%28ispresented,content%29.md), and [`alert(isPresented:content:)`](../SwiftUI/view/alert%28ispresented,content%29.md) — along with `isPresented` in the environment — replace the existing `presentation(_:)`, `Sheet`, `Modal`, and `PresentationLink` types. (52075730)
- Updated the APIs for creating animations. The basic animations are now named after the curve type — such as [`linear`](../SwiftUI/animation/linear.md) and [`easeInOut`](../SwiftUI/animation/easeinout.md). The interpolation-based `spring(mass:stiffness:damping:initialVelocity:)` animation is now [`interpolatingSpring(mass:stiffness:damping:initialVelocity:)`](../SwiftUI/animation/interpolatingspring%28mass,stiffness,damping,initialvelocity%29.md), and `fluidSpring(stiffness:dampingFraction:blendDuration:timestep:idleThreshold:)` is now [`spring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/spring%28response,dampingfraction,blendduration%29.md) or [`interactiveSpring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/interactivespring%28response,dampingfraction,blendduration%29.md), depending on whether or not the animation is driven interactively. (50280375)
- Added an initializer for creating a [`Font`](../SwiftUI/font.md) from a [`CTFont`](../CoreText/ctfont.md). (51849885)

#### Known Issues

- [`Image`](../SwiftUI/image.md) instances don’t use resizing information configured in asset catalogs. Configure the size of an image using the [`resizable(capInsets:resizingMode:)`](../SwiftUI/image/resizable%28capinsets,resizingmode%29.md) modifier instead. (49114577)

#### Deprecations

- The `identified(by:)` method on the [`Collection`](../Swift/collection.md) protocol is deprecated in favor of dedicated `init(_:id:selection:rowContent:)` and `init(_:id:content:)` initializers. (52976883)
- The `relativeWidth(_:)`, `relativeHeight(_:)`, and `relativeSize(width:height:)` modifiers are deprecated. Use other modifiers like [`frame(width:height:alignment:)`](../SwiftUI/view/frame%28width,height,alignment%29.md) instead. (51494692)

### UIKit

#### Known Issues

- Except for [`selectionIndicatorTintColor`](../UIKit/uitabbarappearance/selectionindicatortintcolor.md), properties in the new tab bar appearance API aren’t reflected on the screen. (49792597)

### Xcode

#### New Features

- [`CAMetalLayer`](../QuartzCore/cametallayer.md) is now available in the Simulator. (45101325)

## See Also

### tvOS 13
- [tvOS 13.4.8 Release Notes](./tvos-13_4_8-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.4.5 Release Notes](./tvos-13_4_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.4 Release Notes](./tvos-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.3.1 Release Notes](./tvos-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.3 Release Notes](./tvos-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.2 Release Notes](./tvos-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-13-release-notes)*