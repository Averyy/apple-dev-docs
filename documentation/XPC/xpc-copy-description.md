# xpc_copy_description(_:)

**Framework**: XPC  
**Kind**: func

Copies a debug string that describes the object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_copy_description(_ object: xpc_object_t) -> UnsafeMutablePointer<CChar>
```

#### Return Value

A string describing object which contains information useful for debugging. This string should be disposed of with `free(3)` when done.

## Parameters

- `object`: The object which is to be examined.

## See Also

- [func xpc_copy(xpc_object_t) -> xpc_object_t?](xpc_copy(_:).md)
  Creates a copy of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_copy_description(_:))*