# options

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The behaviors associated with the action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var options: UNNotificationActionOptions { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) UNNotificationActionOptions options;
```

*macOS*

```objc
@property (atomic, readonly) UNNotificationActionOptions options;
```

#### Discussion

You app should define options for an action when your app requires the corresponding behavior.

## See Also

### Getting Options
- [struct UNNotificationActionOptions](../unnotificationactionoptions.md)
  The behaviors you can apply to an action.
- [UNNotificationActionOptionNone](../unnotificationactionoptionnone.md)
  The action has the default behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationaction/options)*