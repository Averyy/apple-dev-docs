# ignoredWords

**Framework**: UIKit  
**Kind**: property

Returns the words that the text checker ignores when spell-checking.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var ignoredWords: [String]? { get set }
```

#### Return Value

An array of strings, each of which specifies a word the receiver ignores when it is spell-checking a document.

#### Discussion

The spell checker excludes ignored words as misspelled words during the current spell-checking session only.

## See Also

- [func ignoreWord(String)](uitextchecker/ignoreword(_:).md)
  Tells the text checker to ignore the specified word when spell-checking.
- [class func learnWord(String)](uitextchecker/learnword(_:).md)
  Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [class func unlearnWord(String)](uitextchecker/unlearnword(_:).md)
  Tells the text checker to unlearn the specified word.
- [class func hasLearnedWord(String) -> Bool](uitextchecker/haslearnedword(_:).md)
  Returns whether the text checker has learned the specified word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/ignoredwords)*