# handle(_:completionHandler:)

**Framework**: WatchKit  
**Kind**: method

Responds to a Siri intent.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@MainActor
optional func handle(_ intent: INIntent) async -> INIntentResponse
```

## Mentions

- [Using background tasks](using-background-tasks.md)

## See Also

- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md)
  A background task used to update your app after a SiriKit intent runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:completionhandler:))*