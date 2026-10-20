# proto_media_detached

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.4+

## Declaration

```c
typedef errno_t (*proto_media_detached)(ifnet_t ifp, protocol_family_t protocol);
```

#### Return Value

See the discussion.

#### Discussion

proto_media_detached notifies you that your protocol has been detached.

## Parameters

- `ifp`: The interface.
- `protocol_family`: The protocol family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_media_detached)*