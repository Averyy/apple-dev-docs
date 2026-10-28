# handleUserActivity(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Responds to Handoff–related activity from complications and notifications.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
optional func handleUserActivity(_ userInfo: [AnyHashable : Any]?)
```

```objc
- (void) handleUserActivity:(NSDictionary *) userInfo;
```

## Discussion

Use this method to respond to Handoff–related activity. WatchKit calls this method when your app launches as a result of a Handoff action. Use the information in the provided `userInfo` dictionary to determine how you want to respond to the action. For example, you might decide to display a specific view.

The default implementation of this method does nothing. When overriding this method, don’t call `super`.

> **Note**:  If you’re creating a SwiftUI app for watchOS 7 or later, use the [`onContinueUserActivity(_:perform:)`](../../SwiftUI/view/oncontinueuseractivity%28_,perform%29.md) modifier instead.

## Parameters

- `userInfo`: The dictionary containing data about the activity.

## See Also

### Related Documentation
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](../wkinterfacecontroller/updateuseractivity%28_,userinfo,webpageurl%29.md)
  Registers the current user activity with the system.
### Coordinating Handoff activity
- [func handle(NSUserActivity)](./handle%28_%29-3kqsk.md)
  Responds to Handoff–related activity from Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleuseractivity(_:))*