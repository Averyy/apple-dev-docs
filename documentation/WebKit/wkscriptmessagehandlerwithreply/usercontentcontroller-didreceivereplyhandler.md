# userContentController(_:didReceive:replyHandler:)

**Framework**: WebKit  
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
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) async -> (Any?, String?)
```

#### Discussion

Use this method to handle a message from the webpage and provide an appropriate response.

## Parameters

- `userContentController`: The user content controller that delivered the message to your handler.
- `message`: An object that contains the message details.
- `replyHandler`: A reply handler block to execute with the response to send back to the webpage. This block has no return value and takes the following parameters: - **reply**: An object that contains the data to return to the webpage. Allowed types for this parameter are [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), and [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull). Specify `nil` if an error occurred.
- **errorMessage**: `nil` on success, or a string that describes the error that occurred.

## See Also

- [class WKScriptMessage](wkscriptmessage.md)
  An object that encapsulates a message sent by JavaScript code from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessagehandlerwithreply/usercontentcontroller(_:didreceive:replyhandler:))*