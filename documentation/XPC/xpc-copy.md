# xpc_copy(_:)

**Framework**: XPC  
**Kind**: func

Creates a copy of the object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_copy(_ object: xpc_object_t) -> xpc_object_t?
```

#### Return Value

The new object. `NULL` if the object type does not support copying or if sufficient memory for the copy could not be allocated. Service objects do not support copying.

#### Discussion

When called on an array or dictionary, [`xpc_copy(_:)`](xpc_copy(_:).md) will perform a deep copy.

The object returned is not necessarily guaranteed to be a new object, and whether it is will depend on the implementation of the object being copied.

## Parameters

- `object`: The object to copy.

## See Also

- [func xpc_copy_description(xpc_object_t) -> UnsafeMutablePointer<CChar>](xpc_copy_description(_:).md)
  Copies a debug string that describes the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_copy(_:))*