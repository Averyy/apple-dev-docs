# ignoreWord(_:)

**Framework**: UIKit  
**Kind**: method

Tells the text checker to ignore the specified word when spell-checking.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func ignoreWord(_ wordToIgnore: String)
```

#### Discussion

The spell checker excludes ignored words as misspelled words during the current spell-checking session only.

## Parameters

- `wordToIgnore`: A string that is a word the receiver should ignore when it is spell-checking a document.

## See Also

- [var ignoredWords: [String]?](uitextchecker/ignoredwords.md)
  Returns the words that the text checker ignores when spell-checking.
- [class func learnWord(String)](uitextchecker/learnword(_:).md)
  Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [class func unlearnWord(String)](uitextchecker/unlearnword(_:).md)
  Tells the text checker to unlearn the specified word.
- [class func hasLearnedWord(String) -> Bool](uitextchecker/haslearnedword(_:).md)
  Returns whether the text checker has learned the specified word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/ignoreword(_:))*