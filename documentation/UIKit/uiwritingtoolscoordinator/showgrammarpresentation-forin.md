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

Pass in context and range to identify the issue the user selected. The context must match one of the contexts returned from [`writingToolsCoordinator(_:requestsContextsFor:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:).md) and the range must match the range in the context of one of the grammar details returned for that context from [`writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsgrammarresultsfor:completion:).md) Returns NO if the UI cannot be brought up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/showgrammarpresentation(for:in:))*