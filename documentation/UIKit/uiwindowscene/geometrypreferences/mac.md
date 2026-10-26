# UIWindowScene.GeometryPreferences.Mac

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst 16.0+
- tvOS
- visionOS

## Declaration

```swift
class Mac
```

```objc
@interface UIWindowSceneGeometryPreferencesMac : UIWindowSceneGeometryPreferences
```

#### Overview

Use this class to express macOS-specific geometry preferences when you call [`requestGeometryUpdate(_:errorHandler:)`](../requestgeometryupdate%28_,errorhandler%29.md).

## Topics

### Creating a geometry preferences object
- [convenience init(systemFrame: CGRect)](./mac/init%28systemframe%29.md)
  Initializes a new window scene geometry preferences object with the specified window frame.
- [init()](./mac/init%28%29.md)
  Initializes a new window scene geometry preferences object.
### Accessing geometry information
- [var systemFrame: CGRect?](./mac/systemframe.md)
  The preferred frame of the scene, in system coordinates.
- [systemFrame](../../uiwindowscenegeometrypreferencesmac/systemframe.md)
  The preferred frame of the scene, in system coordinates.

## Relationships

### Inherits From
- [UIWindowScene.GeometryPreferences](../geometrypreferences.md)
### Conforms To
- [CVarArg](../../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [NSObjectProtocol](../../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [var effectiveGeometry: UIWindowScene.Geometry](../effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](../requestgeometryupdate%28_,errorhandler%29.md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [systemFrame](../../uiwindowscenegeometrypreferencesmac/systemframe.md)
  The preferred frame of the scene, in system coordinates.
### Working with window geometry
- [var effectiveGeometry: UIWindowScene.Geometry](../effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](../requestgeometryupdate%28_,errorhandler%29.md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](../geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences](../geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.iOS](./ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Vision](./vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](../../uiproposedscenesizenopreference.md)
  Used as the value for a dimension of a size related preference when wanting to leave it unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/mac)*