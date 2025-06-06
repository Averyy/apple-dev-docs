# UIWindowScene.GeometryPreferences.Vision

**Framework**: UIKit  
**Kind**: class

**Availability**:
- visionOS 1.0+

## Declaration

```swift
class Vision
```

## Topics

### Initializers
- [init()](uiwindowscene/geometrypreferences/vision/init.md)
- [convenience init(size: CGSize?, minimumSize: CGSize?, maximumSize: CGSize?, resizingRestrictions: UIWindowScene.ResizingRestrictions?)](uiwindowscene/geometrypreferences/vision/init(size:minimumsize:maximumsize:resizingrestrictions:).md)
### Instance Properties
- [var maximumSize: CGSize?](uiwindowscene/geometrypreferences/vision/maximumsize.md)
- [var minimumSize: CGSize?](uiwindowscene/geometrypreferences/vision/minimumsize.md)
- [var resizingRestrictions: UIWindowScene.ResizingRestrictions?](uiwindowscene/geometrypreferences/vision/resizingrestrictions.md)
- [var size: CGSize?](uiwindowscene/geometrypreferences/vision/size.md)

## Relationships

### Inherits From
- [UIWindowScene.GeometryPreferences](uiwindowscene/geometrypreferences.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var effectiveGeometry: UIWindowScene.Geometry](uiwindowscene/effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
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
- [let UIProposedSceneSizeNoPreference: CGFloat](uiproposedscenesizenopreference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/vision)*