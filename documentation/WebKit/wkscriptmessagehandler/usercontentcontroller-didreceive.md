# userContentController(_:didReceive:)

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Tells the handler that a webpage sent a script message.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage)
```

#### Discussion

Use this method to respond to a message sent from the webpage’s JavaScript code. Use the message parameter to get the message contents and to determine the originating web view.

## Parameters

- `userContentController`: The user content controller that delivered the message to your handler.
- `message`: An object that contains the message details.

## See Also

- [class WKScriptMessage](wkscriptmessage.md)
  An object that encapsulates a message sent by JavaScript code from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler/usercontentcontroller(_:didreceive:))*