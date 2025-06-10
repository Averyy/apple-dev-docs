# disconnect(throwing:)

**Framework**: WebKit  
**Kind**: method

Disconnects the port, terminating all further messages with an optional error.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func disconnect(throwing error: (any Error)?)
```

## Parameters

- `error`: An optional error indicating the reason for disconnection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/disconnect(throwing:))*