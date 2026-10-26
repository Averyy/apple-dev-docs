# xpc_array_create_connection(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates a connection object from an array directly.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func xpc_array_create_connection(_ xarray: xpc_object_t, _ index: Int) -> xpc_connection_t?
```

```c
extern xpc_connection_txpc_array_create_connection(xpc_object_t xarray, size_t index);
```

#### Return Value

A new connection created from the value at the specified index. You are responsible for calling [`xpc_release`](./xpc_release.md) on the returned connection. `NULL` if the value at the specified index is not an endpoint containing a connection. Each call to this method for the same index in the same array will yield a different connection. See [`xpc_connection_create_from_endpoint(_:)`](./xpc_connection_create_from_endpoint%28_%29.md) for discussion as to the responsibilities when dealing with the returned connection.

## Parameters

- `xarray`: The array which is to be examined.
- `index`: The index of the value to obtain. This value must lie within the index space of the array (0 to N-1 inclusive, where N is the count of the array). If the index is outside that range, the behavior is undefined.

## See Also

### Array objects
- [struct XPCArray](./xpcarray.md)
  An ordered random-access collection of XPC objects.
- [func xpc_array_create(UnsafePointer<xpc_object_t>?, Int) -> xpc_object_t](./xpc_array_create%28_,_%29.md)
  Creates an XPC object that represents an array of XPC objects.
- [func xpc_array_create_empty() -> xpc_object_t](./xpc_array_create_empty%28%29.md)
  Creates an XPC object that represents an array of XPC objects.
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
- [func xpc_array_get_dictionary(xpc_object_t, Int) -> xpc_object_t?](./xpc_array_get_dictionary%28_,_%29.md)
  Returns the dictionary at the specified index in the array.
- [func xpc_array_get_double(xpc_object_t, Int) -> Double](./xpc_array_get_double%28_,_%29.md)
  Gets a double-precision floating point primitive value from an array directly.
- [xpc_array_get_int64](./xpc_array_get_int64%28_,_%29.md)
  Gets a 64-bit integer primitive value from an array directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_array_create_connection(_:_:))*