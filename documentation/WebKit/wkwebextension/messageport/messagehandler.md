# messageHandler

**Framework**: WebKit  
**Kind**: property

The block to be executed when a message is received from the web extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var messageHandler: ((Any?, (any Error)?) -> Void)? { get set }
```

#### Discussion

An optional block to be invoked when a message is received, taking two parameters: the message and an optional error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/messagehandler)*