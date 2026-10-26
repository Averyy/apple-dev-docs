# xpc_array_get_dictionary(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Returns the dictionary at the specified index in the array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func xpc_array_get_dictionary(_ xarray: xpc_object_t, _ index: Int) -> xpc_object_t?
```

```c
extern xpc_object_txpc_array_get_dictionary(xpc_object_t xarray, size_t index);
```

#### Return Value

The object at the specified index within the array or `NULL` if the given object was not an XPC array or if the the value at the specified index was not a dictionary.

## Parameters

- `xarray`: The array object which is to be examined.
- `index`: The index of the value to obtain. This value must lie within the range of indexes as specified in [`xpc_array_set_value(_:_:_:)`](./xpc_array_set_value%28_,_,_%29.md).

## See Also

### Array objects
- [struct XPCArray](./xpcarray.md)
  An ordered random-access collection of XPC objects.
- [func xpc_array_create(UnsafePointer<xpc_object_t>?, Int) -> xpc_object_t](./xpc_array_create%28_,_%29.md)
  Creates an XPC object that represents an array of XPC objects.
- [func xpc_array_create_empty() -> xpc_object_t](./xpc_array_create_empty%28%29.md)
  Creates an XPC object that represents an array of XPC objects.
- [func xpc_array_create_connection(xpc_object_t, Int) -> xpc_connection_t?](./xpc_array_create_connection%28_,_%29.md)
  Creates a connection object from an array directly.
- [func xpc_array_set_value(xpc_object_t, Int, xpc_object_t)](./xpc_array_set_value%28_,_,_%29.md)
  Inserts the specified object into the array at the specified index.
- [func xpc_array_get_value(xpc_object_t, Int) -> xpc_object_t](./xpc_array_get_value%28_,_%29.md)
  Returns the value at the specified index in the array.
- [func xpc_array_append_value(xpc_object_t, xpc_object_t)](./xpc_array_append_value%28_,_%29.md)
  Appends an object to an XPC array.
- [func xpc_array_get_count(xpc_object_t) -> Int](./xpc_array_get_count%28_%29.md)
  Returns the count of values in the array.
- [func xpc_array_apply(xpc_object_t, (Int, xpc_object_t) -> Bool) -> Bool](./xpc_array_apply%28_,_%29.md)
  Invokes the specified block for every value in the array.
- [func xpc_array_dup_fd(xpc_object_t, Int) -> Int32](./xpc_array_dup_fd%28_,_%29.md)
  Gets a file descriptor from an array directly.
- [func xpc_array_get_array(xpc_object_t, Int) -> xpc_object_t?](./xpc_array_get_array%28_,_%29.md)
  Returns the array at the specified index in the array.
- [func xpc_array_get_bool(xpc_object_t, Int) -> Bool](./xpc_array_get_bool%28_,_%29.md)
  Gets a Boolean primitive value from an array directly.
- [func xpc_array_get_data(xpc_object_t, Int, UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](./xpc_array_get_data%28_,_,_%29.md)
  Gets a pointer to the raw bytes of a data object from an array directly.
- [func xpc_array_get_date(xpc_object_t, Int) -> Int64](./xpc_array_get_date%28_,_%29.md)
  Gets a date interval from an array directly.
- [func xpc_array_get_double(xpc_object_t, Int) -> Double](./xpc_array_get_double%28_,_%29.md)
  Gets a double-precision floating point primitive value from an array directly.
- [xpc_array_get_int64](./xpc_array_get_int64%28_,_%29.md)
  Gets a 64-bit integer primitive value from an array directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_array_get_dictionary(_:_:))*