# splitViewController(_:willChangeTo:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the display mode for the split view controller is about to change.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, willChangeTo displayMode: UISplitViewController.DisplayMode)
```

#### Discussion

The split view controller calls this method when its display mode is about to change. Because changing the display mode usually means hiding or showing one of the child view controllers, you can implement this method and use it to add or remove the controls for showing the primary view controller.

## Parameters

- `svc`: The split view controller whose display mode is changing.
- `displayMode`: The new display mode that is about to be applied to the split view controller.

## See Also

- [func targetDisplayModeForAction(in: UISplitViewController) -> UISplitViewController.DisplayMode](uisplitviewcontrollerdelegate/targetdisplaymodeforaction(in:).md)
  Asks the delegate to provide the display mode to apply when a split view controller action occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willchangeto:))*