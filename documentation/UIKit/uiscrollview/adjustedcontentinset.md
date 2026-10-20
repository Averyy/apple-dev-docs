# adjustedContentInset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The insets derived from the content insets and the safe area of the scroll view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var adjustedContentInset: UIEdgeInsets { get }
```

```objc
@property (nonatomic, readonly) UIEdgeInsets adjustedContentInset;
```

#### Discussion

Use this property to obtain the adjusted area in which to draw content. The [`contentInsetAdjustmentBehavior`](./contentinsetadjustmentbehavior-swift.property.md) property determines whether the safe area insets are included in the adjustment. The safe area insets are then added to the values in the [`contentInset`](./contentinset.md) property to obtain the final value of this property.

## See Also

### Managing the content inset behavior
- [var contentInset: UIEdgeInsets](./contentinset.md)
  The custom distance that the content view is inset from the safe area or scroll view edges.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](./contentinsetadjustmentbehavior-swift.property.md)
  The behavior for determining the adjusted content offsets.
- [UIScrollView.ContentInsetAdjustmentBehavior](./contentinsetadjustmentbehavior-swift.enum.md)
  Constants indicating how safe area insets are added to the adjusted content inset.
- [func adjustedContentInsetDidChange()](./adjustedcontentinsetdidchange%28%29.md)
  Notifies the scroll view when the adjusted content insets of the scroll view change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/adjustedcontentinset)*