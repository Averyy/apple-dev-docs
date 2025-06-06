# requestGeometryUpdate(_:errorHandler:)

**Framework**: UIKit  
**Kind**: method

Requests an update to the window scene’s geometry using the specified geometry preferences object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func requestGeometryUpdate(_ geometryPreferences: UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)? = nil)
```

#### Discussion

Use this method to explicitly request geometry changes to the window scene. The following code shows an example of requesting the window scene to rotate to a landscape orientation in iOS.

```swift
// In a view controller, get the window scene.
guard let windowScene = view.window?.windowScene else { return }

// Request the window scene to rotate to any landscape orientation.
windowScene.requestGeometryUpdate(.iOS(interfaceOrientations: .landscape)) { error in
    // Handle denial of request.
}
```

## Parameters

- `geometryPreferences`: The geometry information to use for the request.
- `errorHandler`: An optional closure to call when an error occurs. The system may call the error handler asynchronously.

## See Also

- [var effectiveGeometry: UIWindowScene.Geometry](uiwindowscene/effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/requestgeometryupdate(_:errorhandler:))*