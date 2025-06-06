# learnWord(_:)

**Framework**: UIKit  
**Kind**: method

Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func learnWord(_ word: String)
```

#### Discussion

When a `UITextChecker` object learns a word, it is added to the dictionary. It is global across languages.

## Parameters

- `word`: A string representing the word for the class to learn.

## See Also

- [func ignoreWord(String)](uitextchecker/ignoreword(_:).md)
  Tells the text checker to ignore the specified word when spell-checking.
- [var ignoredWords: [String]?](uitextchecker/ignoredwords.md)
  Returns the words that the text checker ignores when spell-checking.
- [class func unlearnWord(String)](uitextchecker/unlearnword(_:).md)
  Tells the text checker to unlearn the specified word.
- [class func hasLearnedWord(String) -> Bool](uitextchecker/haslearnedword(_:).md)
  Returns whether the text checker has learned the specified word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/learnword(_:))*