# sessionIdentifier

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The identifier for the triggering background transfer.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var sessionIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * sessionIdentifier;
```

## Discussion

This property holds the background session identifier from the [`URLSessionConfiguration`](../../Foundation/urlsessionconfiguration.md) object used to create the background transfer. Use this identifier to create a configuration and session object to connect to the background session task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask/sessionidentifier)*