# xpc_array_get_data(_:_:_:)

**Framework**: XPC  
**Kind**: func

Gets a pointer to the raw bytes of a data object from an array directly.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_array_get_data(_ xarray: xpc_object_t, _ index: Int, _ length: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?
```

#### Return Value

The underlying bytes at the specified index. NULL if the value at the specified index is not a data value.

## Parameters

- `xarray`: The array which is to be examined.
- `index`: The index of the value to obtain. This value must lie within the index space of the array (0 to N-1 inclusive, where N is the count of the array). If the index is outside that range, the behavior is undefined.
- `length`: Upon return output, will contain the length of the data corresponding to the specified key.

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
- [func xpc_array_get_date(xpc_object_t, Int) -> Int64](xpc_array_get_date(_:_:).md)
  Gets a date interval from an array directly.
- [func xpc_array_get_dictionary(xpc_object_t, Int) -> xpc_object_t?](xpc_array_get_dictionary(_:_:).md)
  Returns the dictionary at the specified index in the array.
- [func xpc_array_get_double(xpc_object_t, Int) -> Double](xpc_array_get_double(_:_:).md)
  Gets a double-precision floating point primitive value from an array directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_array_get_data(_:_:_:))*