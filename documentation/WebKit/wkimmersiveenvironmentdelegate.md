# WKImmersiveEnvironmentDelegate

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- visionOS 27.0+

## Declaration

```swift
@MainActor
protocol WKImmersiveEnvironmentDelegate : NSObjectProtocol
```

```objc
@protocol WKImmersiveEnvironmentDelegate <NSObject>
```

## Overview

A protocol for managing immersive environment presentation in a web view.

Implement the methods of this protocol to control authorization, presentation, and dismissal of immersive environments requested by websites.

## Topics

### Instance Methods
- [func webView(WKWebView, dismiss: WKImmersiveEnvironment, completionHandler: () -> Void)](./wkimmersiveenvironmentdelegate/webview%28_,dismiss,completionhandler%29.md)
- [func webView(WKWebView, present: WKImmersiveEnvironment, completionHandler: ((any Error)?) -> Void)](./wkimmersiveenvironmentdelegate/webview%28_,present,completionhandler%29.md)
- [func webView(WKWebView, shouldAllowImmersiveEnvironmentFromFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](./wkimmersiveenvironmentdelegate/webview%28_,shouldallowimmersiveenvironmentfromframe,completionhandler%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Immersive environments
- [class WKImmersiveEnvironment](./wkimmersiveenvironment.md)
- [var allowsImmersiveEnvironments: Bool](./wkwebviewconfiguration/allowsimmersiveenvironments.md)
- [var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)?](./wkwebview/immersiveenvironmentdelegate.md)
- [func dismissImmersiveEnvironment(completionHandler: () -> Void)](./wkwebview/dismissimmersiveenvironment%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkimmersiveenvironmentdelegate)*