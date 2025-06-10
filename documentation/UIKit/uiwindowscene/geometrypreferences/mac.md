# UIWindowScene.GeometryPreferences.Mac

**Framework**: UIKit  
**Kind**: class

An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 16.0+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class Mac
```

#### Overview

Use this class to express macOS-specific geometry preferences when you call [`requestGeometryUpdate(_:errorHandler:)`](uiwindowscene/requestgeometryupdate(_:errorhandler:).md).

## Topics

### Creating a geometry preferences object
- [convenience init(systemFrame: CGRect)](uiwindowscene/geometrypreferences/mac/init(systemframe:).md)
  Initializes a new window scene geometry preferences object with the specified window frame.
- [init()](uiwindowscene/geometrypreferences/mac/init.md)
  Initializes a new window scene geometry preferences object.
### Accessing geometry information
- [var systemFrame: CGRect?](uiwindowscene/geometrypreferences/mac/systemframe.md)
  The preferred frame of the scene, in system coordinates.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [UIWindowScene.GeometryPreferences.iOS](uiwindowscene/geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Vision](uiwindowscene/geometrypreferences/vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](uiproposedscenesizenopreference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/mac)*