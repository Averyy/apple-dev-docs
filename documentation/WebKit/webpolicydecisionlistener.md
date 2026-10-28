# WebPolicyDecisionListener

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

This protocol enables [`WebView`](./webview-swift.class.md) policy delegates to communicate with listener objects. A listener object conforming to this protocol is passed as one of the arguments to web view policy delegate methods.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebPolicyDecisionListener : NSObjectProtocol
```

```objc
@protocol WebPolicyDecisionListener <NSObject>
```

## Overview

This protocol allows delegates to handle download decisions asynchronously. For example, the policy delegate may display a sheet, and the listener object gets notified only after the user clicks an OK or Cancel button. You do not directly create objects that conform to this protocol.

## Topics

### Making Resource-Usage Decisions
- [func download()](./webpolicydecisionlistener/download%28%29.md)
  Tells the listener to download the resource instead of displaying it.
- [func ignore()](./webpolicydecisionlistener/ignore%28%29.md)
  Tells the listener to ignore the resource.
- [func use()](./webpolicydecisionlistener/use%28%29.md)
  Tells the listener to use the resource.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
### Setting Policies (Legacy)
- [protocol WebPolicyDelegate](./webpolicydelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydecisionlistener)*