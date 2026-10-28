# UIWindowScene.GeometryPreferences.iOS

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIWindowSceneGeometryPreferencesIOS : UIWindowSceneGeometryPreferences
```

## Overview

Use this class to express iOS-specific geometry preferences when you call [`requestGeometryUpdate(_:errorHandler:)`](../requestgeometryupdate%28_,errorhandler%29.md).

## Topics

### Creating a geometry preferences object
- [convenience init(interfaceOrientations: UIInterfaceOrientationMask)](./ios/init%28interfaceorientations%29.md)
  Initializes a new window scene geometry preferences object with the specified interface orientations.
- [init()](./ios/init%28%29.md)
  Initializes a new window scene geometry preferences object.
### Requesting preferred interface orientations
- [var interfaceOrientations: UIInterfaceOrientationMask?](./ios/interfaceorientations.md)
  The preferred interface orientations for the scene.
- [interfaceOrientations](../../uiwindowscenegeometrypreferencesios/interfaceorientations.md)
  The preferred interface orientations for the scene.

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
- [interfaceOrientations](../../uiwindowscenegeometrypreferencesios/interfaceorientations.md)
  The preferred interface orientations for the scene.
### Working with window geometry
- [var effectiveGeometry: UIWindowScene.Geometry](../effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](../requestgeometryupdate%28_,errorhandler%29.md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](../geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences](../geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.Mac](./mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](./vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](../../uiproposedscenesizenopreference.md)
  Used as the value for a dimension of a size related preference when wanting to leave it unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/ios)*