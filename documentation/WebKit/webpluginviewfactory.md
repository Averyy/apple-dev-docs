# WebPlugInViewFactory

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebPlugInViewFactory : NSObjectProtocol
```

```objc
@protocol WebPlugInViewFactory <NSObject>
```

## Topics

### Type Methods
- [static func plugInView(withArguments: [AnyHashable : Any]!) -> NSView!](./webpluginviewfactory/pluginview%28witharguments%29.md)
  Creates a new plug-in view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
### Implementing Plugins  (Legacy)
- [WebPlugIn](../ObjectiveC/webplugin.md)
  The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.
- [WebPlugInContainer](../ObjectiveC/webplugincontainer.md)
  `WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpluginviewfactory)*