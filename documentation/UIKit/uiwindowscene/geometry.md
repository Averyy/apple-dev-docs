# UIWindowScene.Geometry

**Framework**: UIKit  
**Kind**: class

An object that provides geometry information about the window scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class Geometry
```

## Topics

### Accessing scene geometry
- [var systemFrame: CGRect](uiwindowscene/geometry/systemframe.md)
  The current frame of the scene, in system coordinates.
- [var coordinateSpace: any UICoordinateSpace](uiwindowscene/geometry/coordinatespace.md)
  The coordinate space of the scene
- [var interfaceOrientation: UIInterfaceOrientation](uiwindowscene/geometry/interfaceorientation.md)
  The current interface orientation for the scene.
- [var isInterfaceOrientationLocked: Bool](uiwindowscene/geometry/isinterfaceorientationlocked.md)
  If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.
### Instance Properties
- [var isInteractivelyResizing: Bool](uiwindowscene/geometry/isinteractivelyresizing.md)
  Returns true when the scene is being resized interactively, otherwise false.
- [var maximumSize: CGSize](uiwindowscene/geometry/maximumsize.md)
- [var minimumSize: CGSize](uiwindowscene/geometry/minimumsize.md)
- [var resizingRestrictions: UIWindowSceneResizingRestrictions](uiwindowscene/geometry/resizingrestrictions.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var effectiveGeometry: UIWindowScene.Geometry](uiwindowscene/effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](uiwindowscene/requestgeometryupdate(_:errorhandler:).md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.GeometryPreferences](uiwindowscene/geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.iOS](uiwindowscene/geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Mac](uiwindowscene/geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](uiwindowscene/geometrypreferences/vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](uiproposedscenesizenopreference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometry)*