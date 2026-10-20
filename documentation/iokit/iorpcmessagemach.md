# IORPCMessageMach

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
struct IORPCMessageMach
```

```c
typedef struct IORPCMessageMach {
    ...
} IORPCMessageMach;
```

## Topics

### Initializers
- [init()](./iorpcmessagemach/api-3757891-init.md)
- [init(msgh: mach_msg_header_t, msgh_body: mach_msg_body_t, objects: ())](./iorpcmessagemach/api-3757892-init.md)
### Instance Properties
- [var msgh: mach_msg_header_t](./iorpcmessagemach/api-3074887-msgh.md)
- [var msgh_body: mach_msg_body_t](./iorpcmessagemach/api-3074888-msgh_body.md)
- [var objects: ()](./iorpcmessagemach/api-3074889-objects.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iorpcmessagemach)*