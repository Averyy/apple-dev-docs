# showGrammarPresentation(for:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
func showGrammarPresentation(for range: NSRange, in context: UIWritingToolsCoordinator.Context) -> Bool
```

```objc
- (BOOL) showGrammarPresentationForRange:(NSRange) range inContext:(UIWritingToolsCoordinatorContext *) context;
```

## Discussion

Pass in context and range to identify the issue the user selected. The context must match one of the contexts returned from [`writingToolsCoordinator(_:requestsContextsFor:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestscontextsfor,completion%29.md) and the range must match the range in the context of one of the grammar details returned for that context from [`writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestsgrammarresultsfor,completion%29.md) Returns NO if the UI cannot be brought up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/showgrammarpresentation(for:in:))*