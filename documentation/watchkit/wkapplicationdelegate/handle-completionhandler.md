# handle(_:completionHandler:)

**Framework**: WatchKit  
**Kind**: method

Responds to a Siri intent.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func handle(_ intent: INIntent) async -> INIntentResponse
```

#### Discussion

The system calls this method when it receives a Siri intent. Implement a method that handles the incoming intent, and then call the completion handler as quickly as possible.

## Parameters

- `intent`: An intent containing information about the user’s request.
- `completionHandler`: A closure that you call as soon as you finish handling the intent.

## See Also

- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkintentdidrunrefreshbackgroundtask))
  A background task used to update your app after a SiriKit intent runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:completionhandler:))*