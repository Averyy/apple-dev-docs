# scene(_:willContinueUserActivityWithType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that it’s about to receive Handoff-related data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func scene(_ scene: UIScene, willContinueUserActivityWithType userActivityType: String)
```

```objc
- (void) scene:(UIScene *) scene willContinueUserActivityWithType:(NSString *) userActivityType;
```

#### Discussion

Use this method to prepare to handle an activity with the specified type. After this method returns, UIKit provides feedback to the user that your scene is handling the activity.

## Parameters

- `scene`: The scene handling the activity.
- `userActivityType`: The type of activity to continue.

## See Also

### Continuing user activities
- [func scene(UIScene, continue: NSUserActivity)](./scene%28_,continue%29.md)
  Tells the delegate to handle the specified Handoff-related activity.
- [func scene(UIScene, didFailToContinueUserActivityWithType: String, error: any Error)](./scene%28_,didfailtocontinueuseractivitywithtype,error%29.md)
  Tells the delegate that the activity couldn’t be continued.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:willcontinueuseractivitywithtype:))*