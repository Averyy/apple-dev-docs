# rangeOfMisspelledWord(in:range:startingAt:wrap:language:)

**Framework**: UIKit  
**Kind**: method

Initiates a search of a range of a string for a misspelled word.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func rangeOfMisspelledWord(in stringToCheck: String, range: NSRange, startingAt startingOffset: Int, wrap wrapFlag: Bool, language: String) -> NSRange
```

#### Return Value

The range of the first misspelled word encountered or `{NSNotFound, 0}` if none is found.

#### Discussion

To search an entire string or a range within that string, call this method in a loop, resetting `startingOffset` from each returned range, until you reach the end of the string or specified range within the string.

## Parameters

- `stringToCheck`: The string to check for misspelled words.
- `range`: The range of   to check for a misspelled word.
- `startingOffset`: The offset within   of   to begin checking for misspelled words.
- `wrapFlag`:   to continue checking from the beginning of   if no misspelled word is found between   and the end of  . Specify   to have spell-checking end at the end of  .
- `language`: The language of the of words to be checked for correct spelling. This string is a ISO 639-1 language code or a combined ISO 639-1 language code and ISO 3166-1 regional code (for example,  ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/rangeofmisspelledword(in:range:startingat:wrap:language:))*