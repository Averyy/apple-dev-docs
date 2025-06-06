# UIWindowScene.GeometryPreferences.iOS

**Framework**: UIKit  
**Kind**: class

An object that represents the geometry preferences for a window scene in an iOS app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class iOS
```

#### Overview

Use this class to express iOS-specific geometry preferences when you call [`requestGeometryUpdate(_:errorHandler:)`](uiwindowscene/requestgeometryupdate(_:errorhandler:).md).

## Topics

### Creating a geometry preferences object
- [convenience init(interfaceOrientations: UIInterfaceOrientationMask)](uiwindowscene/geometrypreferences/ios/init(interfaceorientations:).md)
  Initializes a new window scene geometry preferences object with the specified interface orientations.
- [init()](uiwindowscene/geometrypreferences/ios/init.md)
  Initializes a new window scene geometry preferences object.
### Requesting preferred interface orientations
- [var interfaceOrientations: UIInterfaceOrientationMask?](uiwindowscene/geometrypreferences/ios/interfaceorientations.md)
  The preferred interface orientations for the scene.

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
- [var effectiveGeometry: UIWindowScene.Geometry](uiwindowscene/effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](uiwindowscene/requestgeometryupdate(_:errorhandler:).md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](uiwindowscene/geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences](uiwindowscene/geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.Mac](uiwindowscene/geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](uiwindowscene/geometrypreferences/vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](uiproposedscenesizenopreference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/ios)*