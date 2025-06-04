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

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func handle(_ intent: INIntent) async -> INIntentResponse
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func handle(_ intent: INIntent) async -> INIntentResponse
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkintentdidrunrefreshbackgroundtask))
  A background task used to update your app after a SiriKit intent runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:completionhandler:))*