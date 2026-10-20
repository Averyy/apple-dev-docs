# prefersPageSizing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the sheet sizes itself for readable content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
var prefersPageSizing: Bool { get set }
```

```objc
@property (nonatomic) BOOL prefersPageSizing;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). The default value indicates the sheet uses [`UIModalPresentationStyle.pageSheet`](../uimodalpresentationstyle/pagesheet.md) behavior, in which the sheet width follows the readable width.

When the value is set to [`false`](../../Swift/false.md), the sheet uses [`UIModalPresentationStyle.formSheet`](../uimodalpresentationstyle/formsheet.md) behavior, in which the sheet size follows the presented view controller’s [`preferredContentSize`](../uiviewcontroller/preferredcontentsize.md).

## See Also

### Managing the appearance
- [var prefersGrabberVisible: Bool](./prefersgrabbervisible.md)
  A Boolean value that determines whether the sheet shows a grabber at the top.
- [var prefersEdgeAttachedInCompactHeight: Bool](./prefersedgeattachedincompactheight.md)
  A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](./widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [var preferredCornerRadius: CGFloat?](./preferredcornerradius-3mb5.md)
  The corner radius that the sheet attempts to present with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/preferspagesizing)*