# state

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current level of Writing Tools activity in your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
var state: UIWritingToolsCoordinator.State { get }
```

```objc
@property (nonatomic, readonly) UIWritingToolsCoordinatorState state;
```

#### Discussion

Use this property to determine when Writing Tools is actively making changes to your view. During the course of Writing Tools interactions, the system reports state changes to the delegate’s [`writingToolsCoordinator(_:willChangeTo:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,willchangeto,completion%29.md) method and updates this property accordingly.

## See Also

### Managing the current state
- [func stopWritingTools()](./stopwritingtools%28%29.md)
  Stops the current Writing Tools operation and dismisses the system UI.
- [UIWritingToolsCoordinator.State](./state-swift.enum.md)
  The states that indicate the current activity, if any, Writing Tools is performing in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.property)*