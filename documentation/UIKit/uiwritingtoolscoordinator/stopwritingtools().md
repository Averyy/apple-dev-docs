# stopWritingTools()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Stops the current Writing Tools operation and dismisses the system UI.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
func stopWritingTools()
```

```objc
- (void) stopWritingTools;
```

## Discussion

Call this method to abort the current Writing Tools operation. This method dismisses the system’s Writing Tools UI and stops any in-flight interactions with your view. This method does not undo any changes that Writing Tools already made to your view’s content.

## See Also

### Managing the current state
- [var state: UIWritingToolsCoordinator.State](./state-swift.property.md)
  The current level of Writing Tools activity in your view.
- [UIWritingToolsCoordinator.State](./state-swift.enum.md)
  The states that indicate the current activity, if any, Writing Tools is performing in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/stopwritingtools())*