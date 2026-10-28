# userContentController(_:didReceive:replyHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
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
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage, replyHandler: @escaping @MainActor @Sendable (Any?, String?) -> Void)
```

```swift
func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) async -> (Any?, String?)
```

```objc
- (void) userContentController:(WKUserContentController *) userContentController didReceiveScriptMessage:(WKScriptMessage *) message replyHandler:(void (^)(id, NSString *)) replyHandler;
```

## Discussion

Use this method to handle a message from the webpage and provide an appropriate response.

## Parameters

- `userContentController`: The user content controller that delivered the message to your handler.
- `message`: An object that contains the message details.
- `replyHandler`: A reply handler block to execute with the response to send back to the webpage. This block has no return value and takes the following parameters:

  - **reply**: An object that contains the data to return to the webpage. Allowed types for this parameter are [`NSNumber`](../../Foundation/nsnumber.md), [`NSString`](../../Foundation/nsstring.md), [`NSDate`](../../Foundation/nsdate.md), [`NSArray`](../../Foundation/nsarray.md), [`NSDictionary`](../../Foundation/nsdictionary.md), and [`NSNull`](../../Foundation/nsnull.md). Specify `nil` if an error occurred.
  - **errorMessage**: `nil` on success, or a string that describes the error that occurred.

## See Also

### Receiving Messages
- [class WKScriptMessage](../wkscriptmessage.md)
  An object that encapsulates a message sent by JavaScript code from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessagehandlerwithreply/usercontentcontroller(_:didreceive:replyhandler:))*