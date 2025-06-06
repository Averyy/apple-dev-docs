# userContentController(_:didReceive:replyHandler:)

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Tells the handler that a webpage sent a script message that included a reply.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) async -> (Any?, String?)
```

#### Discussion

Use this method to handle a message from the webpage and provide an appropriate response.

## Parameters

- `userContentController`: The user content controller that delivered the message to your handler.
- `message`: An object that contains the message details.
- `replyHandler`: A reply handler block to execute with the response to send back to the webpage. This block has no return value and takes the following parameters:

## See Also

- [class WKScriptMessage](wkscriptmessage.md)
  An object that encapsulates a message sent by JavaScript code from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessagehandlerwithreply/usercontentcontroller(_:didreceive:replyhandler:))*