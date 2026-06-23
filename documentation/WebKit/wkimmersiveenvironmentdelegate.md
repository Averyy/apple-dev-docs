# WKImmersiveEnvironmentDelegate

**Framework**: WebKit  
**Kind**: protocol

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol WKImmersiveEnvironmentDelegate : NSObjectProtocol
```

#### Overview

A protocol for managing immersive environment presentation in a web view.

Implement the methods of this protocol to control authorization, presentation, and dismissal of immersive environments requested by websites.

## Topics

### Instance Methods
- [func webView(WKWebView, dismiss: WKImmersiveEnvironment, completionHandler: () -> Void)](wkimmersiveenvironmentdelegate/webview(_:dismiss:completionhandler:).md)
- [func webView(WKWebView, present: WKImmersiveEnvironment, completionHandler: ((any Error)?) -> Void)](wkimmersiveenvironmentdelegate/webview(_:present:completionhandler:).md)
- [func webView(WKWebView, shouldAllowImmersiveEnvironmentFromFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](wkimmersiveenvironmentdelegate/webview(_:shouldallowimmersiveenvironmentfromframe:completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKImmersiveEnvironment](wkimmersiveenvironment.md)
- [var allowsImmersiveEnvironments: Bool](wkwebviewconfiguration/allowsimmersiveenvironments.md)
- [var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)?](wkwebview/immersiveenvironmentdelegate.md)
- [func dismissImmersiveEnvironment(completionHandler: () -> Void)](wkwebview/dismissimmersiveenvironment(completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkimmersiveenvironmentdelegate)*