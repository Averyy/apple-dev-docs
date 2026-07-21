# showGrammarPresentation(for:in:)

**Framework**: UIKit  
**Kind**: method

Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func showGrammarPresentation(for range: NSRange, in context: UIWritingToolsCoordinator.Context) -> Bool
```

#### Discussion

Pass in context and range to identify the issue the user selected. Returns NO if the UI cannot be brought up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/showgrammarpresentation(for:in:))*