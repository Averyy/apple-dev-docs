# XPCArray

**Framework**: Xpc  
**Kind**: struct

An ordered random-access collection of XPC objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
struct XPCArray
```

## Topics

### Creating an array
- [init()](xpcarray/init.md)
  Creates a new, empty array.
- [init(xpc_object_t)](xpcarray/init(_:).md)
  Creates a new array that contains the given XPC object.
- [func copy(into: XPCArray)](xpcarray/copy(into:).md)
  Copies the elements of the array to a different array.
### Inspecting an array
- [var isEmpty: Bool](xpcarray/isempty.md)
  A Boolean value that indicates whether the array is empty.
- [var count: Int](xpcarray/count.md)
  The number of elements in the array.
### Accessing elements
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
- [subscript<T>(Int) -> T?](xpcarray/subscript(_:)-9x9ho.md)
  Reads and writes the value at the given index as an unsigned integer.
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
- [func withUnsafeUnderlyingArray<ReturnType>((xpc_object_t) throws -> ReturnType) rethrows -> ReturnType](xpcarray/withunsafeunderlyingarray(_:).md)
  Calls a closure with an unsafe reference to the array.
### Iterating over an array’s elements
- [func forEach((XPCArray.IndexValuePair) throws -> Void) rethrows](xpcarray/foreach(_:)-6obs3.md)
  Calls the given closure with each element in the array in the same order as a for-in loop.
- [func forEach((Int, xpc_object_t) throws -> Void) rethrows](xpcarray/foreach(_:)-2ib8a.md)
  Calls the given closure with an index and element of the array in the same order as a for-in loop.
### Transforming an array
- [func map<ReturnType>((XPCArray.IndexValuePair) throws -> ReturnType) rethrows -> [ReturnType]](xpcarray/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
### Supporting types
- [typealias IndexValuePair](xpcarray/indexvaluepair.md)
  A type that contains an index and the object at that index.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func xpc_array_create(UnsafePointer<xpc_object_t>?, Int) -> xpc_object_t](xpc_array_create(_:_:).md)
  Creates an XPC object that represents an array of XPC objects.
- [func xpc_array_create_empty() -> xpc_object_t](xpc_array_create_empty().md)
  Creates an XPC object that represents an array of XPC objects.
- [func xpc_array_create_connection(xpc_object_t, Int) -> xpc_connection_t?](xpc_array_create_connection(_:_:).md)
  Creates a connection object from an array directly.
- [func xpc_array_set_value(xpc_object_t, Int, xpc_object_t)](xpc_array_set_value(_:_:_:).md)
  Inserts the specified object into the array at the specified index.
- [func xpc_array_get_value(xpc_object_t, Int) -> xpc_object_t](xpc_array_get_value(_:_:).md)
  Returns the value at the specified index in the array.
- [func xpc_array_append_value(xpc_object_t, xpc_object_t)](xpc_array_append_value(_:_:).md)
  Appends an object to an XPC array.
- [func xpc_array_get_count(xpc_object_t) -> Int](xpc_array_get_count(_:).md)
  Returns the count of values in the array.
- [func xpc_array_apply(xpc_object_t, (Int, xpc_object_t) -> Bool) -> Bool](xpc_array_apply(_:_:).md)
  Invokes the specified block for every value in the array.
- [func xpc_array_dup_fd(xpc_object_t, Int) -> Int32](xpc_array_dup_fd(_:_:).md)
  Gets a file descriptor from an array directly.
- [func xpc_array_get_array(xpc_object_t, Int) -> xpc_object_t?](xpc_array_get_array(_:_:).md)
  Returns the array at the specified index in the array.
- [func xpc_array_get_bool(xpc_object_t, Int) -> Bool](xpc_array_get_bool(_:_:).md)
  Gets a Boolean primitive value from an array directly.
- [func xpc_array_get_data(xpc_object_t, Int, UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](xpc_array_get_data(_:_:_:).md)
  Gets a pointer to the raw bytes of a data object from an array directly.
- [func xpc_array_get_date(xpc_object_t, Int) -> Int64](xpc_array_get_date(_:_:).md)
  Gets a date interval from an array directly.
- [func xpc_array_get_dictionary(xpc_object_t, Int) -> xpc_object_t?](xpc_array_get_dictionary(_:_:).md)
  Returns the dictionary at the specified index in the array.
- [func xpc_array_get_double(xpc_object_t, Int) -> Double](xpc_array_get_double(_:_:).md)
  Gets a double-precision floating point primitive value from an array directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray)*