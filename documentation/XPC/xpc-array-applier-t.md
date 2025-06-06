# xpc_array_applier_t

**Framework**: Xpc  
**Kind**: typealias

A block to invoke for every value in the array.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_array_applier_t = (Int, xpc_object_t) -> Bool
```

#### Return Value

A Boolean indicating whether iteration should continue.

## Parameters

- `index`: The current index in the iteration.
- `value`: The current value in the iteration.

## See Also

- [struct XPCArray](xpcarray.md)
  An ordered random-access collection of XPC objects.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_array_applier_t)*