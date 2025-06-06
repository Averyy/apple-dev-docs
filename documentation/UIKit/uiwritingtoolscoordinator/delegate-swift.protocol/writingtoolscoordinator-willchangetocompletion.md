# writingToolsCoordinator(_:willChangeTo:completion:)

**Framework**: UIKit  
**Kind**: method

Notifies your delegate of relevant state changes when Writing Tools is running in your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, willChangeTo newState: UIWritingToolsCoordinator.State) async
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

Use state transitions to perform actions related to your view or text storage. When Writing Tools is active, it updates its state to indicate what task it’s currently performing. Writing Tools starts in the [`UIWritingToolsCoordinator.State.inactive`](uiwritingtoolscoordinator/state-swift.enum/inactive.md) state and moves to other states as it presents UI and starts interacting with your view’s content. For example, it moves to the [`UIWritingToolsCoordinator.State.interactiveStreaming`](uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.md) state when it’s making changes to your view’s text storage.

## Parameters

- `writingToolsCoordinator`: The coordinator object providing   information to your custom view.
- `completion`: A handler to execute when your delegate finishes processing   the change of state. The handler has no parameters or return value. You   must call this handler at some point during the implementation of your method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:))*