# sendMessage(_:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Sends a message to the connected web extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func sendMessage(_ message: Any?) async throws
```

#### Discussion

> **Note**: The message must be JSON-serializable according to doc://com.apple.documentation/documentation/foundation/foundation/jsonserialization.

The message must be JSON-serializable according to doc://com.apple.documentation/documentation/foundation/foundation/jsonserialization.

## Parameters

- `message`: The JSON-serializable message to be sent.
- `completionHandler`: An optional block to be invoked after the message is sent, taking an optional error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/sendmessage(_:completionhandler:))*