# ignoredWords

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the words that the text checker ignores when spell-checking.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var ignoredWords: [String]? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSArray<NSString *> * ignoredWords;
```

#### Return Value

An array of strings, each of which specifies a word the receiver ignores when it is spell-checking a document.

#### Discussion

The spell checker excludes ignored words as misspelled words during the current spell-checking session only.

## See Also

### Learning and Ignoring Words
- [func ignoreWord(String)](./ignoreword%28_%29.md)
  Tells the text checker to ignore the specified word when spell-checking.
- [class func learnWord(String)](./learnword%28_%29.md)
  Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [class func unlearnWord(String)](./unlearnword%28_%29.md)
  Tells the text checker to unlearn the specified word.
- [class func hasLearnedWord(String) -> Bool](./haslearnedword%28_%29.md)
  Returns whether the text checker has learned the specified word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/ignoredwords)*