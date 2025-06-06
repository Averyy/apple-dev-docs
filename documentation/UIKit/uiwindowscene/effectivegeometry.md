# effectiveGeometry

**Framework**: UIKit  
**Kind**: property

The current values for the window scene’s geometry in system space.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var effectiveGeometry: UIWindowScene.Geometry { get }
```

#### Discussion

This property is key-value observing (KVO) compliant. Observing [`effectiveGeometry`](uiwindowscene/effectivegeometry.md) is the recommended way to receive notifications of changes to the window scene’s geometry. These changes can occur because of user interaction or as a result of the system resolving a geometry request.

## See Also

- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](uiwindowscene/requestgeometryupdate(_:errorhandler:).md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](uiwindowscene/geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences](uiwindowscene/geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.iOS](uiwindowscene/geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Mac](uiwindowscene/geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](uiwindowscene/geometrypreferences/vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](uiproposedscenesizenopreference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/effectivegeometry)*