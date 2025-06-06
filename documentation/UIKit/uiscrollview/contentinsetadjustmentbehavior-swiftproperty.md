# contentInsetAdjustmentBehavior

**Framework**: UIKit  
**Kind**: property

The behavior for determining the adjusted content offsets.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior { get set }
```

#### Discussion

This property specifies how the safe area insets are used to modify the content area of the scroll view. The default value of this property is [`UIScrollView.ContentInsetAdjustmentBehavior.automatic`](uiscrollview/contentinsetadjustmentbehavior-swift.enum/automatic.md).

## See Also

- [var adjustedContentInset: UIEdgeInsets](uiscrollview/adjustedcontentinset.md)
  The insets derived from the content insets and the safe area of the scroll view.
- [var contentInset: UIEdgeInsets](uiscrollview/contentinset.md)
  The custom distance that the content view is inset from the safe area or scroll view edges.
- [UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.enum.md)
  Constants indicating how safe area insets are added to the adjusted content inset.
- [func adjustedContentInsetDidChange()](uiscrollview/adjustedcontentinsetdidchange.md)
  Notifies the scroll view when the adjusted content insets of the scroll view change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.property)*