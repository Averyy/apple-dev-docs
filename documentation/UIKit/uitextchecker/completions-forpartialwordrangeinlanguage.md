# completions(forPartialWordRange:in:language:)

**Framework**: UIKit  
**Kind**: method

Returns an array of strings that are possible completions for a partially entered word.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func completions(forPartialWordRange range: NSRange, in string: String, language: String) -> [String]?
```

#### Return Value

An array of strings, each of which is a completion of a partially entered word represented by `range` in `string`. If no possible completions are found,  the method returns an empty array.

#### Discussion

The strings in the array are in the order they should be presented to the user—that is, more probable completions come first in the array.

## Parameters

- `range`: The range of a partially entered word in  .
- `string`: A string in which there is a partially entered word, as located by  .
- `language`: The language of the of the words that are possible corrections. This string is a ISO 639-1 language code or a combined ISO 639-1 language code and ISO 3166-1 regional code (for example,  ).

## See Also

- [func guesses(forWordRange: NSRange, in: String, language: String) -> [String]?](uitextchecker/guesses(forwordrange:in:language:).md)
  Returns a list of words that are possible valid replacements for a misspelled word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/completions(forpartialwordrange:in:language:))*