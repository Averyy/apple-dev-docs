# learnWord(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class func learnWord(_ word: String)
```

```objc
+ (void) learnWord:(NSString *) word;
```

#### Discussion

When a `UITextChecker` object learns a word, it is added to the dictionary. It is global across languages.

## Parameters

- `word`: A string representing the word for the class to learn.

## See Also

### Learning and Ignoring Words
- [func ignoreWord(String)](./ignoreword%28_%29.md)
  Tells the text checker to ignore the specified word when spell-checking.
- [var ignoredWords: [String]?](./ignoredwords.md)
  Returns the words that the text checker ignores when spell-checking.
- [class func unlearnWord(String)](./unlearnword%28_%29.md)
  Tells the text checker to unlearn the specified word.
- [class func hasLearnedWord(String) -> Bool](./haslearnedword%28_%29.md)
  Returns whether the text checker has learned the specified word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/learnword(_:))*