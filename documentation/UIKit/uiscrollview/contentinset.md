# contentInset

**Framework**: UIKit  
**Kind**: property

The custom distance that the content view is inset from the safe area or scroll view edges.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentInset: UIEdgeInsets { get set }
```

#### Discussion

Use this property to extend the space between your content and the edges of the content view. The unit of size is points. The default value is [`zero`](uiedgeinsets/zero.md).

By default, UIKit automatically adjusts the content inset to account for overlapping bars. You use this property to extend that distance even further, perhaps to accommodate your own custom content. Get the total adjustment — the safe area plus your custom insets — using the [`adjustedContentInset`](uiscrollview/adjustedcontentinset.md) property. To change how the safe area is applied, modify the [`contentInsetAdjustmentBehavior`](uiscrollview/contentinsetadjustmentbehavior-swift.property.md) property.

## See Also

- [var adjustedContentInset: UIEdgeInsets](uiscrollview/adjustedcontentinset.md)
  The insets derived from the content insets and the safe area of the scroll view.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.property.md)
  The behavior for determining the adjusted content offsets.
- [UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.enum.md)
  Constants indicating how safe area insets are added to the adjusted content inset.
- [func adjustedContentInsetDidChange()](uiscrollview/adjustedcontentinsetdidchange.md)
  Notifies the scroll view when the adjusted content insets of the scroll view change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentinset)*