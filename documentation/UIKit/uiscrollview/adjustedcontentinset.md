# adjustedContentInset

**Framework**: UIKit  
**Kind**: property

The insets derived from the content insets and the safe area of the scroll view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var adjustedContentInset: UIEdgeInsets { get }
```

#### Discussion

Use this property to obtain the adjusted area in which to draw content. The [`contentInsetAdjustmentBehavior`](uiscrollview/contentinsetadjustmentbehavior-swift.property.md) property determines whether the safe area insets are included in the adjustment. The safe area insets are then added to the values in the [`contentInset`](uiscrollview/contentinset.md) property to obtain the final value of this property.

## See Also

- [var contentInset: UIEdgeInsets](uiscrollview/contentinset.md)
  The custom distance that the content view is inset from the safe area or scroll view edges.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.property.md)
  The behavior for determining the adjusted content offsets.
- [UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.enum.md)
  Constants indicating how safe area insets are added to the adjusted content inset.
- [func adjustedContentInsetDidChange()](uiscrollview/adjustedcontentinsetdidchange.md)
  Notifies the scroll view when the adjusted content insets of the scroll view change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/adjustedcontentinset)*