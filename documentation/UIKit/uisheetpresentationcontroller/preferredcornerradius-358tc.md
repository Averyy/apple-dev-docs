# preferredCornerRadius

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The corner radius that the sheet attempts to present with.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```objc
@property (nonatomic) CGFloat preferredCornerRadius;
```

#### Discussion

The default value is [`UISheetPresentationControllerAutomaticDimension`](../uisheetpresentationcontrollerautomaticdimension.md). This property only has an effect when the sheet is at the front of its sheet stack.

## See Also

### Managing the appearance
- [var prefersGrabberVisible: Bool](./prefersgrabbervisible.md)
  A Boolean value that determines whether the sheet shows a grabber at the top.
- [var prefersPageSizing: Bool](./preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var prefersEdgeAttachedInCompactHeight: Bool](./prefersedgeattachedincompactheight.md)
  A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](./widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [UISheetPresentationControllerAutomaticDimension](../uisheetpresentationcontrollerautomaticdimension.md)
  The default value to apply to a dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/preferredcornerradius-358tc)*