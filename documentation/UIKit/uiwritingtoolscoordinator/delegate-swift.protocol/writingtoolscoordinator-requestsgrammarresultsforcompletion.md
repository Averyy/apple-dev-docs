# writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for information about grammar issues in the specified context.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, grammarResultsFor context: UIWritingToolsCoordinator.Context) async -> [NSTextCheckingResult]
```

#### Discussion

To support the grammar presentation UI, the delegate should provide information about the identified and currently indicated grammar issues in the specified context. The elements of the results array should be `NSTextCheckingResult` objects of grammar type, of the sort that are returned from grammar checking, with ranges relative to the context. If you use grammar presentation, you must implement this delegate method to provide them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsgrammarresultsfor:completion:))*