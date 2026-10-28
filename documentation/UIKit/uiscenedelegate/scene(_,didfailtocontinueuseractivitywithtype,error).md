# scene(_:didFailToContinueUserActivityWithType:error:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the activity couldn’t be continued.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func scene(_ scene: UIScene, didFailToContinueUserActivityWithType userActivityType: String, error: any Error)
```

```objc
- (void) scene:(UIScene *) scene didFailToContinueUserActivityWithType:(NSString *) userActivityType error:(NSError *) error;
```

## Discussion

Use this method to let the user know that the specified activity couldn’t be completed. If you don’t implement this method, UIKit displays an error to the user with an appropriate message about the reason for the failure.

## Parameters

- `scene`: The scene handling the activity.
- `userActivityType`: The type of the activity that failed.
- `error`: An error object indicating the reason for the failure.

## See Also

### Continuing user activities
- [func scene(UIScene, willContinueUserActivityWithType: String)](./scene%28_,willcontinueuseractivitywithtype%29.md)
  Tells the delegate that it’s about to receive Handoff-related data.
- [func scene(UIScene, continue: NSUserActivity)](./scene%28_,continue%29.md)
  Tells the delegate to handle the specified Handoff-related activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:didfailtocontinueuseractivitywithtype:error:))*