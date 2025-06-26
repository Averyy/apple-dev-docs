# textView(_:shouldChangeTextInRanges:replacementText:)

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
optional func textView(_ textView: UITextView, shouldChangeTextInRanges ranges: [NSValue], replacementText text: String) -> Bool
```

#### Return Value

Returns true if the text at the `ranges` should be replaced.

#### Discussion

If this method returns YES then the text view will, at its own discretion, choose any one of the specified `ranges` of text and replace it with the specified `replacementText` before deleting the text at the other ranges. If the delegate does not implement this method then the `textView:shouldChangeTextInRange:replacementText:` method will be called and passed the union range instead. If the delegate also does not implement that method then YES is assumed.

## Parameters

- `textView`: The text view asking the delegate
- `ranges`: The ranges of the text that should be deleted before replacing


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldchangetextinranges:replacementtext:))*