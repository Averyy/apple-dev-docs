# UIWindowScene.GeometryPreferences

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An abstract superclass for representing window scene geometry preferences.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class GeometryPreferences
```

```objc
@interface UIWindowSceneGeometryPreferences : NSObject
```

## Topics

### Geometry preferences
- [UIWindowScene.GeometryPreferences.Mac](./geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.iOS](./geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
### Classes
- [UIWindowScene.GeometryPreferences.Vision](./geometrypreferences/vision.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIWindowScene.GeometryPreferences.Mac](./geometrypreferences/mac.md)
- [UIWindowScene.GeometryPreferences.Vision](./geometrypreferences/vision.md)
- [UIWindowScene.GeometryPreferences.iOS](./geometrypreferences/ios.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with window geometry
- [var effectiveGeometry: UIWindowScene.Geometry](./effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](./requestgeometryupdate%28_,errorhandler%29.md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](./geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences.iOS](./geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Mac](./geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](./geometrypreferences/vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](../uiproposedscenesizenopreference.md)
  Used as the value for a dimension of a size related preference when wanting to leave it unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences)*