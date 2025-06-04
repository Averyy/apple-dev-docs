# handle(_:)

**Framework**: WatchKit  
**Kind**: method

Responds to Handoff–related activity from Siri.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func handle(_ userActivity: NSUserActivity)
```

#### Discussion

WatchKit calls this method when it receives data associated with a user activity. Use this method to update your app on Apple Watch so that the user can continue the activity from where they left off.

## Parameters

- `userActivity`: The activity object containing the data associated with the task the user was performing. Use the data to continue the user’s activity in your app on Apple Watch.

## See Also

- [func handleUserActivity([AnyHashable : Any]?)](wkapplicationdelegate/handleuseractivity(_:).md)
  Responds to Handoff–related activity from complications and notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-3kqsk)*