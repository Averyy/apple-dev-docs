# init(_:)

**Framework**: XPC  
**Kind**: init

Creates a new array that contains the given XPC object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(_ value: xpc_object_t)
```

## Parameters

- `value`: An XPC object. The object’s type must be [`XPC_TYPE_ARRAY`](xpc_type_array-swift.var.md).

## See Also

- [init()](xpcarray/init.md)
  Creates a new, empty array.
- [func copy(into: XPCArray)](xpcarray/copy(into:).md)
  Copies the elements of the array to a different array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/init(_:))*