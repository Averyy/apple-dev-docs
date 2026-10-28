# subscript(_:)

**Framework**: XPC  
**Kind**: subscript  
**Role**: Instance Subscript

Reads and writes the value at the given index as a floating point value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
subscript<T>(index: Int) -> T? where T : BinaryFloatingPoint { get set }
```

## Return Value

The value at the specified index in the array, otherwise [`nil`](../../ObjectiveC/nil-227m0.md).

## Parameters

- `index`: The position of the element to access.

## See Also

### Accessing elements
- [subscript(Int) -> XPCDictionary?](./subscript%28_%29-1s7qq.md)
  Reads and writes the value at the given index as an XPC dictionary.
- [subscript(Int) -> String?](./subscript%28_%29-6c9gh.md)
  Reads and writes the value at the given index as a string.
- [subscript(Int) -> Bool?](./subscript%28_%29-i6v5.md)
  Reads and writes the value at the given index as a Boolean value.
- [subscript(Int) -> xpc_object_t?](./subscript%28_%29-56wjj.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript<T>(Int) -> T?](./subscript%28_%29-9x9ho.md)
  Reads and writes the value at the given index as an unsigned integer.
- [subscript<T>(Int) -> T?](./subscript%28_%29-2f94n.md)
  Reads and writes the value at the given index as a signed integer.
- [subscript(Int, as _: XPCDictionary.Type) -> XPCDictionary?](./subscript%28_,as%29-3ae6x.md)
  Reads the value associated with the given key as an XPC dictionary.
- [subscript(Int, as _: String.Type) -> String?](./subscript%28_,as%29-9ukjj.md)
  Reads and writes the value at the given index as a string.
- [subscript(Int, as _: Bool.Type) -> Bool?](./subscript%28_,as%29-1bilh.md)
  Reads and writes the value at the given index as a Boolean value.
- [subscript(Int, as _: any OS_xpc_object.Type) -> xpc_object_t?](./subscript%28_,as%29-931lh.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript(Int, as _: xpc_type_t) -> xpc_object_t?](./subscript%28_,as%29-3tgp4.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript<T>(Int, as _: T.Type) -> T?](./subscript%28_,as%29-2hql9.md)
  Reads and writes the value at the given index as a floating point value.
- [subscript<T>(Int, as _: T.Type) -> T?](./subscript%28_,as%29-6grs4.md)
  Reads and writes the value at the given index as an integer value.
- [subscript(Int, as _: Bool.Type, default _: @autoclosure () -> Bool) -> Bool](./subscript%28_,as,default%29-2bn95.md)
  Reads and writes the value at the given index as a Boolean value, falling back to the given default value.
- [subscript<T>(Int, as _: T.Type, default _: @autoclosure () -> T) -> T](./subscript%28_,as,default%29-3k2qm.md)
  Reads and writes the value at the given index as a floating point value, falling back to the given default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:)-8wubg)*