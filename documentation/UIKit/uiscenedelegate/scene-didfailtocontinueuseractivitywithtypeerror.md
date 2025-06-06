# scene(_:didFailToContinueUserActivityWithType:error:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the activity couldn’t be continued.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scene(_ scene: UIScene, didFailToContinueUserActivityWithType userActivityType: String, error: any Error)
```

#### Discussion

Use this method to let the user know that the specified activity couldn’t be completed. If you don’t implement this method, UIKit displays an error to the user with an appropriate message about the reason for the failure.

## Parameters

- `scene`: The scene handling the activity.
- `userActivityType`: The type of the activity that failed.
- `error`: An error object indicating the reason for the failure.

## See Also

- [func scene(UIScene, willContinueUserActivityWithType: String)](uiscenedelegate/scene(_:willcontinueuseractivitywithtype:).md)
  Tells the delegate that it’s about to receive Handoff-related data.
- [func scene(UIScene, continue: NSUserActivity)](uiscenedelegate/scene(_:continue:).md)
  Tells the delegate to handle the specified Handoff-related activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:didfailtocontinueuseractivitywithtype:error:))*