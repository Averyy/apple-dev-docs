# UIWritingToolsCoordinator.TextReplacementReason.rejected

**Framework**: UIKit  
**Kind**: case

An option to replace the text in your view when a grammar suggestion is rejected.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case rejected
```

#### Discussion

When the user interacts with a grammar issue and the UI is shown, and the option to ignore a suggestion is chosen, this reason will be used. Update your view’s text storage without animating the change. In addition, use `ignoreGrammarRange` on [`UITextChecker`](uitextchecker.md) to make sure that the suggestion will continue to be ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/rejected)*