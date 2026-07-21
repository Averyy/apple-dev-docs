# writingToolsCoordinator(_:setGrammarCheckingEnabled:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when the user chooses to disable grammar checking.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, setGrammarCheckingEnabled enabled: Bool)
```

#### Discussion

To support the grammar presentation UI, the delegate is notified if the user chooses the option provided in the grammar presentation UI to disable grammar checking for the view. If you use grammar presentation, you should implement this method to respond to that action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:setgrammarcheckingenabled:))*