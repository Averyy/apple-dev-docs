# init()

**Framework**: Watchkit  
**Kind**: init

Initializes and returns the interface controller using the specified remote notification data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor init()
```

## Overview

The initialized interface controller.

## Discussion

Use this method to initialize your notification interface controller and prepare it for display. You must call the `super` implementation of this method first. That method creates the interface objects for the outlets declared in your class and referencing items in your storyboard.

At some point after initialization, WatchKit calls the `didReceiveRemoteNotification(_:withCompletion:)` or `didReceive(_:withCompletion:)` method to deliver the notification payload.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/init())*