# accessibilityScrollStatus(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a string describing the content at the current offset in the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func accessibilityScrollStatus(for scrollView: UIScrollView) -> String?
```

```objc
- (NSString *) accessibilityScrollStatusForScrollView:(UIScrollView *) scrollView;
```

## Return Value

A custom status string for the current offset.

## Discussion

For example, in a user interface that scrolls through the books in a bookcase, you could return “Books 10 through 20”. By default, VoiceOver announces “Page *X* of *Y*” while scrolling.

Use the [`accessibilityAttributedScrollStatus(for:)`](./accessibilityattributedscrollstatus%28for%29.md) method if portions of your string should be spoken in a different language.

## Parameters

- `scrollView`: The scroll view containing the content.

## See Also

### Providing descriptive information
- [func accessibilityAttributedScrollStatus(for: UIScrollView) -> NSAttributedString?](./accessibilityattributedscrollstatus%28for%29.md)
  Returns an attributed string describing the content at the current offset in the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityscrollstatus(for:))*