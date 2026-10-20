# IORPC

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
struct IORPC
```

```c
typedef struct IORPC {
    ...
} IORPC;
```

## Topics

### Initializers
- [init()](./iorpc/api-3757883-init.md)
- [init(message: UnsafeMutablePointer<IORPCMessageMach>!, reply: UnsafeMutablePointer<IORPCMessageMach>!, sendSize: UInt32, replySize: UInt32)](./iorpc/api-3757884-init.md)
### Instance Properties
- [var message: UnsafeMutablePointer<IORPCMessageMach>!](./iorpc/api-3074874-message.md)
- [var reply: UnsafeMutablePointer<IORPCMessageMach>!](./iorpc/api-3074875-reply.md)
- [var replySize: UInt32](./iorpc/api-3074876-replysize.md)
- [var sendSize: UInt32](./iorpc/api-3074877-sendsize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iorpc)*