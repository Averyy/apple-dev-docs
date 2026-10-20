# handleUserActivity(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Responds to Handoff–related activity from complications and notifications.

**Availability**:
- watchOS 2.0+ - Deprecated in 9.2

## Declaration

```swift
optional func handleUserActivity(_ userInfo: [AnyHashable : Any]?)
```

```objc
- (void) handleUserActivity:(NSDictionary *) userInfo;
```

#### Discussion

Use this method to respond to Handoff–related activity. WatchKit calls this method when your app launches as a result of a Handoff action. Use the information in the provided `userInfo` dictionary to determine how you want to respond to the action. For example, you might decide to display a specific interface controller.

The default implementation of this method does nothing. When overriding this method, don’t call `super`.

> **Note**:  If you are creating a SwiftUI app for watchOS 7 or later, use the [`onContinueUserActivity(_:perform:)`](../../SwiftUI/view/oncontinueuseractivity%28_,perform%29.md) modifier instead.

##### Handling Activities from Complications and Notifications

WatchKit calls this method when your app launches from a complication or notification. Update your app’s user interface based on the `userInfo` parameter. Your app should seamlessly continue the interaction from the complication or notification.

When your app launches because the user tapped on a complication, the `userInfo` dictionary contains the [`CLKLaunchedTimelineEntryDateKey`](../../ClockKit/clklaunchedtimelineentrydatekey.md) key. The value is a Date object that indicates when the complication launched.

## Parameters

- `userInfo`: The dictionary containing data about the activity.

## See Also

### Related Documentation
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](../wkinterfacecontroller/updateuseractivity%28_,userinfo,webpageurl%29.md)
  Registers the current user activity with the system.
### Coordinating handoff activity
- [func handle(NSUserActivity)](./handle%28_%29-5pyj1.md)
  Responds to Handoff–related activity from Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleuseractivity(_:))*