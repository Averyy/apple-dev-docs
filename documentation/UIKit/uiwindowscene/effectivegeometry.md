# effectiveGeometry

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current values for the window scene’s geometry in system space.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var effectiveGeometry: UIWindowScene.Geometry { get }
```

```objc
@property (nonatomic, readonly) UIWindowSceneGeometry * effectiveGeometry;
```

#### Discussion

This property is key-value observing (KVO) compliant. Observing [`effectiveGeometry`](./effectivegeometry.md) is the recommended way to receive notifications of changes to the window scene’s geometry. These changes can occur because of user interaction or as a result of the system resolving a geometry request.

## See Also

### Working with window geometry
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](./requestgeometryupdate%28_,errorhandler%29.md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](./geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences](./geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.iOS](./geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Mac](./geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](./geometrypreferences/vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](../uiproposedscenesizenopreference.md)
  Used as the value for a dimension of a size related preference when wanting to leave it unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/effectivegeometry)*