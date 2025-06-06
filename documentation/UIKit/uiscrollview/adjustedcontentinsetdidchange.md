# adjustedContentInsetDidChange()

**Framework**: UIKit  
**Kind**: method

Notifies the scroll view when the adjusted content insets of the scroll view change.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func adjustedContentInsetDidChange()
```

## See Also

- [var adjustedContentInset: UIEdgeInsets](uiscrollview/adjustedcontentinset.md)
  The insets derived from the content insets and the safe area of the scroll view.
- [var contentInset: UIEdgeInsets](uiscrollview/contentinset.md)
  The custom distance that the content view is inset from the safe area or scroll view edges.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.property.md)
  The behavior for determining the adjusted content offsets.
- [UIScrollView.ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.enum.md)
  Constants indicating how safe area insets are added to the adjusted content inset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/adjustedcontentinsetdidchange())*