# handleUserActivity(_:)

**Framework**: Watchkit  
**Kind**: method

Responds to Handoff–related activity from complications and notifications.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor optional func handleUserActivity(_ userInfo: [AnyHashable : Any]?)
```

## Overview

Use this method to respond to Handoff–related activity. WatchKit calls this method when your app launches as a result of a Handoff action. Use the information in the provided `userInfo` dictionary to determine how you want to respond to the action. For example, you might decide to display a specific view.

The default implementation of this method does nothing. When overriding this method, don’t call `super`.

> **Note**:  If you’re creating a SwiftUI app for watchOS 7 or later, use the [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onContinueUserActivity(_:perform:)) modifier instead.

 If you’re creating a SwiftUI app for watchOS 7 or later, use the [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onContinueUserActivity(_:perform:)) modifier instead.

## Parameters

- `userInfo`: The dictionary containing data about the activity.

## See Also

- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](updateuseractivity(_:userinfo:webpageurl:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:)))
- [func handle(NSUserActivity)](handle(_:)-3kqsk.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-3kqsk))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleuseractivity(_:))*