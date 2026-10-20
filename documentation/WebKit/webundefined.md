# WebUndefined

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

`WebUndefined` objects are simply used to represent the JavaScript “undefined” value in methods when bridging between JavaScript and Objective-C. For example, if you invoke a JavaScript function that returns the JavaScript “undefined” value, then a `WebUndefined` object is returned to the Objective-C calling context.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class WebUndefined
```

```objc
@interface WebUndefined : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./webundefined/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Incorporating Scripts (Legacy)
- [class WebScriptObject](./webscriptobject.md)
  A `WebScriptObject` object is an Objective-C wrapper for a scripting object passed to your application from the scripting environment.
- [WebScripting](../ObjectiveC/webscripting.md)
  `WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webundefined)*