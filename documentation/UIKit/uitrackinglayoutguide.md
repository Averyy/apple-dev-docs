# UITrackingLayoutGuide

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A layout guide that automatically activates and deactivates layout constraints depending on its proximity to edges.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITrackingLayoutGuide
```

```objc
@interface UITrackingLayoutGuide : UILayoutGuide
```

## Topics

### Configuring automatic constraint activation
- [func setConstraints([NSLayoutConstraint], activeWhenNearEdge: NSDirectionalRectEdge)](./uitrackinglayoutguide/setconstraints%28_,activewhennearedge%29.md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [func setConstraints([NSLayoutConstraint], activeWhenAwayFrom: NSDirectionalRectEdge)](./uitrackinglayoutguide/setconstraints%28_,activewhenawayfrom%29.md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [func constraints(activeWhenNearEdge: NSDirectionalRectEdge) -> [NSLayoutConstraint]](./uitrackinglayoutguide/constraints%28activewhennearedge%29.md)
  Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
- [func constraints(activeWhenAwayFrom: NSDirectionalRectEdge) -> [NSLayoutConstraint]](./uitrackinglayoutguide/constraints%28activewhenawayfrom%29.md)
  Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.
### Tracking constraints
- [func removeAllTrackedConstraints()](./uitrackinglayoutguide/removealltrackedconstraints%28%29.md)
  Stops the layout guide from tracking any constraints.

## Relationships

### Inherits From
- [UILayoutGuide](./uilayoutguide.md)
### Inherited By
- [UIKeyboardLayoutGuide](./uikeyboardlayoutguide.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIPopoverPresentationControllerSourceItem](./uipopoverpresentationcontrollersourceitem.md)

## See Also

### Keyboard layout
- [Adjusting your layout with keyboard layout guide](./adjusting-your-layout-with-keyboard-layout-guide.md)
  Respond dynamically to keyboard movement by using the tracking features of the keyboard layout guide.
- [class UIKeyboardLayoutGuide](./uikeyboardlayoutguide.md)
  A layout guide that represents the space the keyboard occupies in your app’s layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitrackinglayoutguide)*