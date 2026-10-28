# prefersGrabberVisible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the sheet shows a grabber at the top.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var prefersGrabberVisible: Bool { get set }
```

```objc
@property (nonatomic) BOOL prefersGrabberVisible;
```

## Discussion

The default value is [`false`](../../Swift/false.md), which means the sheet doesn’t show a grabber. A *grabber* is a visual affordance that indicates that a sheet is resizable. Showing a grabber may be useful when it isn’t apparent that a sheet can resize or when the sheet can’t dismiss interactively.

Set this value to [`true`](../../Swift/true.md) for the system to draw a grabber in the standard system-defined location. The system automatically hides the grabber at appropriate times, like when the sheet is full screen in a compact-height size class or when another sheet presents on top of it.

## See Also

### Managing the appearance
- [var prefersPageSizing: Bool](./preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var prefersEdgeAttachedInCompactHeight: Bool](./prefersedgeattachedincompactheight.md)
  A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](./widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [var preferredCornerRadius: CGFloat?](./preferredcornerradius-3mb5.md)
  The corner radius that the sheet attempts to present with.
- [preferredCornerRadius](./preferredcornerradius-358tc.md)
  The corner radius that the sheet attempts to present with.
- [UISheetPresentationControllerAutomaticDimension](../uisheetpresentationcontrollerautomaticdimension.md)
  The default value to apply to a dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersgrabbervisible)*