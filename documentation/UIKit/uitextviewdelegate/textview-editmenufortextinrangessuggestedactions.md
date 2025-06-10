# textView(_:editMenuForTextInRanges:suggestedActions:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
optional func textView(_ textView: UITextView, editMenuForTextInRanges ranges: [NSValue], suggestedActions: [UIMenuElement]) -> UIMenu?
```

#### Return Value

Return a UIMenu describing the desired menu hierarchy. Return @c nil to present the default system menu.

## Parameters

- `textView`: The text view requesting the menu.
- `ranges`: The text ranges for which the menu is presented for.
- `suggestedActions`: The actions and commands that the system suggests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:editmenufortextinranges:suggestedactions:))*