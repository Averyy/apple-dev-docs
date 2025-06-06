# position(within:atCharacterOffset:)

**Framework**: UIKit  
**Kind**: method

Returns the position within a range of a document’s text that corresponds to the character offset from the start of that range.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func position(within range: UITextRange, atCharacterOffset offset: Int) -> UITextPosition?
```

#### Return Value

An object that represents a position in a document’s visible text.

#### Discussion

You should implement this method if you don’t have a one-to-one correspondence between [`UITextPosition`](uitextposition.md) objects within the given range and character offsets into a document string.

## Parameters

- `range`: An object that specifies a range of text in a document.
- `offset`: A character offset from the start of  .

## See Also

- [func characterOffset(of: UITextPosition, within: UITextRange) -> Int](uitextinput/characteroffset(of:within:).md)
  Returns the character offset of a position in a document’s text that falls within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/position(within:atcharacteroffset:))*