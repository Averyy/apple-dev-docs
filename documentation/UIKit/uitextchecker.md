# UITextChecker

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object to check a string (usually the text of a document) for misspelled words.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextChecker
```

```objc
@interface UITextChecker : NSObject
```

#### Overview

[`UITextChecker`](./uitextchecker.md) spell-checks using a lexicon for a specific language. You can tell it to ignore specific words when spell-checking a particular document and you can have it learn words, which adds those words to the lexicon. You generally use one instance of [`UITextChecker`](./uitextchecker.md) per document, although you can use a single instance to spell-check related pieces of text if you want to share ignored words and other state.

You may also use a text checker to obtain completions for partially entered words, as well as possible replacements for misspelled words, which you then can present to users.

## Topics

### Initiating a Spell Check
- [func rangeOfMisspelledWord(in: String, range: NSRange, startingAt: Int, wrap: Bool, language: String) -> NSRange](./uitextchecker/rangeofmisspelledword%28in,range,startingat,wrap,language%29.md)
  Initiates a search of a range of a string for a misspelled word.
### Obtaining Word Guesses and Completions
- [func guesses(forWordRange: NSRange, in: String, language: String) -> [String]?](./uitextchecker/guesses%28forwordrange,in,language%29.md)
  Returns a list of words that are possible valid replacements for a misspelled word.
- [func completions(forPartialWordRange: NSRange, in: String, language: String) -> [String]?](./uitextchecker/completions%28forpartialwordrange,in,language%29.md)
  Returns an array of strings that are possible completions for a partially entered word.
### Learning and Ignoring Words
- [func ignoreWord(String)](./uitextchecker/ignoreword%28_%29.md)
  Tells the text checker to ignore the specified word when spell-checking.
- [var ignoredWords: [String]?](./uitextchecker/ignoredwords.md)
  Returns the words that the text checker ignores when spell-checking.
- [class func learnWord(String)](./uitextchecker/learnword%28_%29.md)
  Tells the text checker to learn the specified word so that it doesn’t evaluate it as misspelled.
- [class func unlearnWord(String)](./uitextchecker/unlearnword%28_%29.md)
  Tells the text checker to unlearn the specified word.
- [class func hasLearnedWord(String) -> Bool](./uitextchecker/haslearnedword%28_%29.md)
  Returns whether the text checker has learned the specified word.
### Getting the Available Languages
- [class var availableLanguages: [String]](./uitextchecker/availablelanguages.md)
  Returns the languages that the text checker’s class can perform spell-checking for.
### Instance Methods
- [func ignoreGrammarRange(NSRange, inSentence: String)](./uitextchecker/ignoregrammarrange%28_,insentence%29.md)
- [func requestGrammarChecking(of: String, range: NSRange, waitForAllResults: Bool, completionHandler: (([NSTextCheckingResult]) -> Void)?)](./uitextchecker/requestgrammarchecking%28of,range,waitforallresults,completionhandler%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Spell checking
- [enum UITextGrammarCheckingType](./uitextgrammarcheckingtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker)*