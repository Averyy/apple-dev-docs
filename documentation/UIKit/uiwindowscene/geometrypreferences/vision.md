# UIWindowScene.GeometryPreferences.Vision

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

**Availability**:
- visionOS 1.0+

## Declaration

```swift
class Vision
```

```objc
@interface UIWindowSceneGeometryPreferencesVision : UIWindowSceneGeometryPreferences
```

## Topics

### Initializers
- [init()](./vision/init%28%29.md)
  Creates a geometry preference with no changes. Update the properties who’s preference should change
- [convenience init(size: CGSize?, minimumSize: CGSize?, maximumSize: CGSize?, resizingRestrictions: UIWindowScene.ResizingRestrictions?)](./vision/init%28size,minimumsize,maximumsize,resizingrestrictions%29.md)
### Instance Properties
- [var maximumSize: CGSize?](./vision/maximumsize.md)
- [var minimumSize: CGSize?](./vision/minimumsize.md)
- [var resizingRestrictions: UIWindowScene.ResizingRestrictions?](./vision/resizingrestrictions.md)
- [var size: CGSize?](./vision/size.md)

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
- [UIWindowScene.GeometryPreferences.Mac](./mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [let UIProposedSceneSizeNoPreference: CGFloat](../../uiproposedscenesizenopreference.md)
  Used as the value for a dimension of a size related preference when wanting to leave it unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/vision)*