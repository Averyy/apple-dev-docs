# UIScrollView.ContentInsetAdjustmentBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIScrollViewContentInsetAdjustmentBehavior : NSInteger;
```

## Topics

### Enumeration Cases
- [UIScrollView.ContentInsetAdjustmentBehavior.always](./contentinsetadjustmentbehavior-swift.enum/always.md)
  Always include the safe area insets in the content adjustment.
- [UIScrollView.ContentInsetAdjustmentBehavior.automatic](./contentinsetadjustmentbehavior-swift.enum/automatic.md)
  Automatically adjust the scroll view insets.
- [UIScrollView.ContentInsetAdjustmentBehavior.never](./contentinsetadjustmentbehavior-swift.enum/never.md)
  Do not adjust the scroll view insets.
- [UIScrollView.ContentInsetAdjustmentBehavior.scrollableAxes](./contentinsetadjustmentbehavior-swift.enum/scrollableaxes.md)
  Adjust the insets only in the scrollable directions.
### Initializers
- [init?(rawValue: Int)](./contentinsetadjustmentbehavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the content inset behavior
- [var adjustedContentInset: UIEdgeInsets](./adjustedcontentinset.md)
  The insets derived from the content insets and the safe area of the scroll view.
- [var contentInset: UIEdgeInsets](./contentinset.md)
  The custom distance that the content view is inset from the safe area or scroll view edges.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](./contentinsetadjustmentbehavior-swift.property.md)
  The behavior for determining the adjusted content offsets.
- [func adjustedContentInsetDidChange()](./adjustedcontentinsetdidchange%28%29.md)
  Notifies the scroll view when the adjusted content insets of the scroll view change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum)*