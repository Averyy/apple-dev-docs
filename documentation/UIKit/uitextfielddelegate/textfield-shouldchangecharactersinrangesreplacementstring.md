# textField(_:shouldChangeCharactersInRanges:replacementString:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
optional func textField(_ textField: UITextField, shouldChangeCharactersInRanges ranges: [NSValue], replacementString string: String) -> Bool
```

#### Return Value

Returns YES if the text at the `ranges` should be replaced.

#### Discussion

Asks the delegate if the text at the specified `ranges` should be replaced with `string`.

If this method returns YES then the text field will, at its own discretion, choose any one of the specified `ranges` of text and replace it with the specified `replacementString` before deleting the text at the other ranges.

## Parameters

- `textField`: The text field asking the delegate
- `ranges`: The ranges of the text that should be deleted before replacing


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersinranges:replacementstring:))*