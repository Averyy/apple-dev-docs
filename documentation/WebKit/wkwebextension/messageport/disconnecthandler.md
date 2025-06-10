# disconnectHandler

**Framework**: WebKit  
**Kind**: property

The block to be executed when the port disconnects.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var disconnectHandler: (((any Error)?) -> Void)? { get set }
```

#### Discussion

An optional block to be invoked when the port disconnects, taking an optional error that indicates if the disconnection was caused by an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/disconnecthandler)*