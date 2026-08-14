# WebUndefined

**Framework**: WebKit  
**Kind**: class

`WebUndefined` objects are simply used to represent the JavaScript “undefined” value in methods when bridging between JavaScript and Objective-C. For example, if you invoke a JavaScript function that returns the JavaScript “undefined” value, then a `WebUndefined` object is returned to the Objective-C calling context.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class WebUndefined
```

## Topics

### Initializers
- [init?(coder: NSCoder)](webundefined/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class WebScriptObject](webscriptobject.md)
  A `WebScriptObject` object is an Objective-C wrapper for a scripting object passed to your application from the scripting environment.
- [WebScripting](../objectivec/webscripting.md)
  `WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webundefined)*