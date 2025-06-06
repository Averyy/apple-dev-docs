# scene(_:continue:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate to handle the specified Handoff-related activity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scene(_ scene: UIScene, continue userActivity: NSUserActivity)
```

#### Discussion

Use this method to update the specified scene with the data from the provided activity object. UIKit calls this method on your app’s main thread only after it receives all of the data for an activity object, which might originate from a different device.

## Parameters

- `scene`: The scene handling the activity.
- `userActivity`: The object containing the activity-related data. Use the information in this object to continue the user’s activity in your scene.

## See Also

- [func scene(UIScene, willContinueUserActivityWithType: String)](uiscenedelegate/scene(_:willcontinueuseractivitywithtype:).md)
  Tells the delegate that it’s about to receive Handoff-related data.
- [func scene(UIScene, didFailToContinueUserActivityWithType: String, error: any Error)](uiscenedelegate/scene(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the activity couldn’t be continued.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:continue:))*