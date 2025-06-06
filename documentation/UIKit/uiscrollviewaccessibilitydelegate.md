# UIScrollViewAccessibilityDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods you can implement to provide accessibility information for a scroll view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIScrollViewAccessibilityDelegate : UIScrollViewDelegate
```

## Topics

### Providing descriptive information
- [func accessibilityScrollStatus(for: UIScrollView) -> String?](uiscrollviewaccessibilitydelegate/accessibilityscrollstatus(for:).md)
  Returns a string describing the content at the current offset in the scroll view.
- [func accessibilityAttributedScrollStatus(for: UIScrollView) -> NSAttributedString?](uiscrollviewaccessibilitydelegate/accessibilityattributedscrollstatus(for:).md)
  Returns an attributed string describing the content at the current offset in the scroll view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIScrollViewDelegate](uiscrollviewdelegate.md)

## See Also

- [class UIAccessibilityElement](uiaccessibilityelement.md)
  An element that should be accessible to users with disabilities, but that isn’t accessible by default.
- [protocol UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md)
  A set of methods you can implement to provide accessibility information for individual components of a picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate)*