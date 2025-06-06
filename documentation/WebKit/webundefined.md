# WebUndefined

**Framework**: Webkit  
**Kind**: class

`WebUndefined` objects are simply used to represent the JavaScript “undefined” value in methods when bridging between JavaScript and Objective-C. For example, if you invoke a JavaScript function that returns the JavaScript “undefined” value, then a `WebUndefined` object is returned to the Objective-C calling context.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class WebUndefined
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WebScriptObject](webscriptobject.md)
  A `WebScriptObject` object is an Objective-C wrapper for a scripting object passed to your application from the scripting environment.
- [WebScripting](../ObjectiveC/webscripting.md)
  `WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webundefined)*