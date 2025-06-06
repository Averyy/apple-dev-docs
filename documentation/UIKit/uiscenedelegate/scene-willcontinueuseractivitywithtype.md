# scene(_:willContinueUserActivityWithType:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that it’s about to receive Handoff-related data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scene(_ scene: UIScene, willContinueUserActivityWithType userActivityType: String)
```

#### Discussion

Use this method to prepare to handle an activity with the specified type. After this method returns, UIKit provides feedback to the user that your scene is handling the activity.

## Parameters

- `scene`: The scene handling the activity.
- `userActivityType`: The type of activity to continue.

## See Also

- [func scene(UIScene, continue: NSUserActivity)](uiscenedelegate/scene(_:continue:).md)
  Tells the delegate to handle the specified Handoff-related activity.
- [func scene(UIScene, didFailToContinueUserActivityWithType: String, error: any Error)](uiscenedelegate/scene(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the activity couldn’t be continued.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:willcontinueuseractivitywithtype:))*