# hasLearnedWord(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns whether the text checker has learned the specified word.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class func hasLearnedWord(_ word: String) -> Bool
```

```objc
+ (BOOL) hasLearnedWord:(NSString *) word;
```

## Return Value

[`true`](../../Swift/true.md) if the class has learned the word, otherwise [`false`](../../Swift/false.md).

## Parameters

- `word`: A string representing a word.

## See Also

### Learning and Ignoring Words
- [func ignoreWord(String)](./ignoreword%28_%29.md)
  Tells the text checker to ignore the specified word when spell-checking.
- [var ignoredWords: [String]?](./ignoredwords.md)
  Returns the words that the text checker ignores when spell-checking.
- [class func learnWord(String)](./learnword%28_%29.md)
  Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [class func unlearnWord(String)](./unlearnword%28_%29.md)
  Tells the text checker to unlearn the specified word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/haslearnedword(_:))*