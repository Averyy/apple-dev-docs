# IORPCMessageFromMach(_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
func IORPCMessageFromMach(_ msg: UnsafeMutablePointer<IORPCMessageMach>!, _ reply: Bool) -> UnsafeMutablePointer<IORPCMessage>!
```

```c
IORPCMessage * IORPCMessageFromMach(IORPCMessageMach *msg, bool reply);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/3325691-iorpcmessagefrommach)*