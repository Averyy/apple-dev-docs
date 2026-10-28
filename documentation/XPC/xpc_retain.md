# xpc_retain

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Increments the reference count of an object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern xpc_object_txpc_retain(xpc_object_t object);
```

## Return Value

The object which was given.

## Discussion

Calls to [`xpc_retain`](./xpc_retain.md) must be balanced with calls to [`xpc_release`](./xpc_release.md) to avoid leaking memory.

## Parameters

- `object`: The object which is to be manipulated.

## See Also

### Object life cycle
- [xpc_release](./xpc_release.md)
  Decrements the reference count of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_retain)*