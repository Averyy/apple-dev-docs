# subscript(_:)

**Framework**: Xpc  
**Kind**: subscript

Reads and writes the value at the given index as an unsigned integer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
subscript<T>(index: Int) -> T? where T : UnsignedInteger { get set }
```

#### Return Value

The value at the specified index in the array, otherwise [`Nil`](https://developer.apple.com/documentation/objectivec/nil).

## Parameters

- `index`: The position of the element to access.

## See Also

- [subscript(Int) -> XPCDictionary?](xpcarray/subscript(_:)-1s7qq.md)
  Reads and writes the value at the given index as an XPC dictionary.
- [subscript(Int) -> String?](xpcarray/subscript(_:)-6c9gh.md)
  Reads and writes the value at the given index as a string.
- [subscript(Int) -> Bool?](xpcarray/subscript(_:)-i6v5.md)
  Reads and writes the value at the given index as a Boolean value.
- [subscript(Int) -> xpc_object_t?](xpcarray/subscript(_:)-56wjj.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript<T>(Int) -> T?](xpcarray/subscript(_:)-8wubg.md)
  Reads and writes the value at the given index as a floating point value.
- [subscript<T>(Int) -> T?](xpcarray/subscript(_:)-2f94n.md)
  Reads and writes the value at the given index as a signed integer.
- [subscript(Int, as _: XPCDictionary.Type) -> XPCDictionary?](xpcarray/subscript(_:as:)-3ae6x.md)
  Reads the value associated with the given key as an XPC dictionary.
- [subscript(Int, as _: String.Type) -> String?](xpcarray/subscript(_:as:)-9ukjj.md)
  Reads and writes the value at the given index as a string.
- [subscript(Int, as _: Bool.Type) -> Bool?](xpcarray/subscript(_:as:)-1bilh.md)
  Reads and writes the value at the given index as a Boolean value.
- [subscript(Int, as _: any OS_xpc_object.Type) -> xpc_object_t?](xpcarray/subscript(_:as:)-931lh.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript(Int, as _: xpc_type_t) -> xpc_object_t?](xpcarray/subscript(_:as:)-3tgp4.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript<T>(Int, as _: T.Type) -> T?](xpcarray/subscript(_:as:)-2hql9.md)
  Reads and writes the value at the given index as a floating point value.
- [subscript<T>(Int, as _: T.Type) -> T?](xpcarray/subscript(_:as:)-6grs4.md)
  Reads and writes the value at the given index as an integer value.
- [subscript(Int, as _: Bool.Type, default _: @autoclosure () -> Bool) -> Bool](xpcarray/subscript(_:as:default:)-2bn95.md)
  Reads and writes the value at the given index as a Boolean value, falling back to the given default value.
- [subscript<T>(Int, as _: T.Type, default _: @autoclosure () -> T) -> T](xpcarray/subscript(_:as:default:)-3k2qm.md)
  Reads and writes the value at the given index as a floating point value, falling back to the given default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:)-9x9ho)*