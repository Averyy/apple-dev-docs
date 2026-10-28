# UNNotificationPresentationOptionNone

**Framework**: User Notifications  
**Kind**: var  
**Role**: Global Variable

No alert.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
static const UNNotificationPresentationOptions UNNotificationPresentationOptionNone;
```

## Discussion

Specify this constant when you want to silence any user interactions for a notification.

## See Also

### Receiving Notifications
- [func userNotificationCenter(UNUserNotificationCenter, willPresent: UNNotification, withCompletionHandler: (UNNotificationPresentationOptions) -> Void)](./unusernotificationcenterdelegate/usernotificationcenter%28_,willpresent,withcompletionhandler%29.md)
  Asks the delegate how to handle a notification that arrived while the app was running in the foreground.
- [struct UNNotificationPresentationOptions](./unnotificationpresentationoptions.md)
  Constants indicating how to present a notification in a foreground app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptionnone)*