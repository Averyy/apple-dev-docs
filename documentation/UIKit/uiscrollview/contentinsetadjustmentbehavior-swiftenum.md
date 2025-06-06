# UIScrollView.ContentInsetAdjustmentBehavior

**Framework**: UIKit  
**Kind**: enum

Constants indicating how safe area insets are added to the adjusted content inset.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ContentInsetAdjustmentBehavior
```

## Topics

### Enumeration Cases
- [UIScrollView.ContentInsetAdjustmentBehavior.always](uiscrollview/contentinsetadjustmentbehavior-swift.enum/always.md)
  Always include the safe area insets in the content adjustment.
- [UIScrollView.ContentInsetAdjustmentBehavior.automatic](uiscrollview/contentinsetadjustmentbehavior-swift.enum/automatic.md)
  Automatically adjust the scroll view insets.
- [UIScrollView.ContentInsetAdjustmentBehavior.never](uiscrollview/contentinsetadjustmentbehavior-swift.enum/never.md)
  Do not adjust the scroll view insets.
- [UIScrollView.ContentInsetAdjustmentBehavior.scrollableAxes](uiscrollview/contentinsetadjustmentbehavior-swift.enum/scrollableaxes.md)
  Adjust the insets only in the scrollable directions.
### Initializers
- [init?(rawValue: Int)](uiscrollview/contentinsetadjustmentbehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var adjustedContentInset: UIEdgeInsets](uiscrollview/adjustedcontentinset.md)
  The insets derived from the content insets and the safe area of the scroll view.
- [var contentInset: UIEdgeInsets](uiscrollview/contentinset.md)
  The custom distance that the content view is inset from the safe area or scroll view edges.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.property.md)
  The behavior for determining the adjusted content offsets.
- [func adjustedContentInsetDidChange()](uiscrollview/adjustedcontentinsetdidchange.md)
  Notifies the scroll view when the adjusted content insets of the scroll view change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum)*