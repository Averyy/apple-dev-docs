# IORPCMessage

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
struct IORPCMessage
```

```c
typedef struct IORPCMessage {
    ...
} IORPCMessage;
```

## Topics

### Initializers
- [init()](./iorpcmessage/api-3757885-init.md)
- [init(msgid: UInt64, flags: UInt64, objectRefs: UInt64, objects: ())](./iorpcmessage/api-3757886-init.md)
### Instance Properties
- [var flags: UInt64](./iorpcmessage/api-3074881-flags.md)
- [var msgid: UInt64](./iorpcmessage/api-3074882-msgid.md)
- [var objectRefs: UInt64](./iorpcmessage/api-3074884-objectrefs.md)
- [var objects: ()](./iorpcmessage/api-3353076-objects.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iorpcmessage)*