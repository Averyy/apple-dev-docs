# handle(_:completionHandler:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Responds to a Siri intent.

**Availability**:
- watchOS 5.0+ - Deprecated in 9.2

## Declaration

```swift
optional func handle(_ intent: INIntent, completionHandler: @escaping (INIntentResponse) -> Void)
```

```swift
optional func handle(_ intent: INIntent) async -> INIntentResponse
```

```objc
- (void) handleIntent:(INIntent *) intent completionHandler:(void (^)(INIntentResponse *intentResponse)) completionHandler;
```

## Mentions

- [Using background tasks](../using-background-tasks.md)

## See Also

### Related Documentation
- [class WKIntentDidRunRefreshBackgroundTask](../wkintentdidrunrefreshbackgroundtask.md)
  A background task used to update your app after a SiriKit intent runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:completionhandler:))*