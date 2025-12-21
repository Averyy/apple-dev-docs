# WebPolicyDecisionListener

**Framework**: WebKit  
**Kind**: protocol

This protocol enables [`WebView`](webview-swift.class.md) policy delegates to communicate with listener objects. A listener object conforming to this protocol is passed as one of the arguments to web view policy delegate methods.

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebPolicyDecisionListener : NSObjectProtocol
```

#### Overview

This protocol allows delegates to handle download decisions asynchronously. For example, the policy delegate may display a sheet, and the listener object gets notified only after the user clicks an OK or Cancel button. You do not directly create objects that conform to this protocol.

## Topics

### Making Resource-Usage Decisions
- [func download()](webpolicydecisionlistener/download.md)
  Tells the listener to download the resource instead of displaying it.
- [func ignore()](webpolicydecisionlistener/ignore.md)
  Tells the listener to ignore the resource.
- [func use()](webpolicydecisionlistener/use.md)
  Tells the listener to use the resource.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [protocol WebPolicyDelegate](webpolicydelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydecisionlistener)*