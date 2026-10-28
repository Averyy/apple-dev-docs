# date

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The delivery date of the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var date: Date { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSDate * date;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSDate * date;
```

## Discussion

The system displays this date to the user in Notification Center.

## See Also

### Getting the Notification Details
- [var request: UNNotificationRequest](./request.md)
  The notification request containing the payload and trigger condition for the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotification/date)*