# hasLearnedWord(_:)

**Framework**: UIKit  
**Kind**: method

Returns whether the text checker has learned the specified word.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func hasLearnedWord(_ word: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the class has learned the word, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `word`: A string representing a word.

## See Also

- [func ignoreWord(String)](uitextchecker/ignoreword(_:).md)
  Tells the text checker to ignore the specified word when spell-checking.
- [var ignoredWords: [String]?](uitextchecker/ignoredwords.md)
  Returns the words that the text checker ignores when spell-checking.
- [class func learnWord(String)](uitextchecker/learnword(_:).md)
  Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [class func unlearnWord(String)](uitextchecker/unlearnword(_:).md)
  Tells the text checker to unlearn the specified word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/haslearnedword(_:))*