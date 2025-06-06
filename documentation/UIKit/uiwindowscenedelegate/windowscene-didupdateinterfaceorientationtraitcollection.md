# windowScene(_:didUpdate:interfaceOrientation:traitCollection:)

**Framework**: UIKit  
**Kind**: method

Notifies you when the size, orientation, or traits of a scene change.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func windowScene(_ windowScene: UIWindowScene, didUpdate previousCoordinateSpace: any UICoordinateSpace, interfaceOrientation previousInterfaceOrientation: UIInterfaceOrientation, traitCollection previousTraitCollection: UITraitCollection)
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Discussion

The window scene environment typically changes in response to user actions. For example, the interface orientation changes in response to device orientation changes or screen mode in response to moving to another screen. Similarly, the user may resize scenes on iPad, which causes UIKit to report a change to the scene’s coordinate space. Use these changes to make any needed changes to your scene’s content or interface.

## Parameters

- `windowScene`: The window scene object whose environment changed.
- `previousCoordinateSpace`: The previous coordinate space of the scene. Get the current coordinate space from the   property of the   object.
- `previousInterfaceOrientation`: The previous interface orientation for your content. Get the current interface orientation from the   property of the   object.
- `previousTraitCollection`: The previous traits for the window. Get the current window traits from the   property of the   object.

## See Also

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)
  Fill connected displays with additional content from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdate:interfaceorientation:traitcollection:))*