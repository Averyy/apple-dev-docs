# textField(_:shouldChangeCharactersInRanges:replacementString:)

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
optional func textField(_ textField: UITextField, shouldChangeCharactersInRanges ranges: [NSValue], replacementString string: String) -> Bool
```

#### Return Value

Returns YES if the text at the `ranges` should be replaced.

#### Discussion

If this method returns YES then the text field will, at its own discretion, choose any one of the specified `ranges` of text and replace it with the specified `replacementString` before deleting the text at the other ranges.

## Parameters

- `textField`: The text field asking the delegate
- `ranges`: The ranges of the text that should be deleted before replacing


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersinranges:replacementstring:))*