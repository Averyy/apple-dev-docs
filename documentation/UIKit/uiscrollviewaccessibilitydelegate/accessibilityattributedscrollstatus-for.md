# accessibilityAttributedScrollStatus(for:)

**Framework**: UIKit  
**Kind**: method

Returns an attributed string describing the content at the current offset in the scroll view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func accessibilityAttributedScrollStatus(for scrollView: UIScrollView) -> NSAttributedString?
```

#### Return Value

An attributed string describing the content.

#### Discussion

Your implementation of this method returns a description of the content that’s currently visible in the scroll view. Use this method (instead of the [`accessibilityScrollStatus(for:)`](uiscrollviewaccessibilitydelegate/accessibilityscrollstatus(for:).md) method) when you want to include attributes that specify which language to use when speaking the text. For more information, see [`UIAccessibilitySpeechAttributeLanguage`](uiaccessibilityspeechattributelanguage.md).

## Parameters

- `scrollView`: The scroll view containing the content.

## See Also

- [func accessibilityScrollStatus(for: UIScrollView) -> String?](uiscrollviewaccessibilitydelegate/accessibilityscrollstatus(for:).md)
  Returns a string describing the content at the current offset in the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityattributedscrollstatus(for:))*