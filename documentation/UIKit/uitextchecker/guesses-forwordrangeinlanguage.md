# guesses(forWordRange:in:language:)

**Framework**: UIKit  
**Kind**: method

Returns a list of words that are possible valid replacements for a misspelled word.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func guesses(forWordRange range: NSRange, in string: String, language: String) -> [String]?
```

#### Return Value

An array of strings each of which might be a correct substitute (that is, a guess) for a misspelled word in the given range of the string. If no possible guesses are found,  the method returns an empty array.

#### Discussion

The strings in the array are in the order they should be presented to the user—that is, more probable guesses come first in the array.

## Parameters

- `range`: The range of a misspelled word in  .
- `string`: A string in which there is a misspelled word, as located by  .
- `language`: The language of the of the words that are possible corrections. This string is from the ISO 639-1 standard, for example   (Spanish).

## See Also

- [func completions(forPartialWordRange: NSRange, in: String, language: String) -> [String]?](uitextchecker/completions(forpartialwordrange:in:language:).md)
  Returns an array of strings that are possible completions for a partially entered word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/guesses(forwordrange:in:language:))*