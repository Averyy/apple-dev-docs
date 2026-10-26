# xpc_array_create(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates an XPC object that represents an array of XPC objects.

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
func xpc_array_create(_ objects: UnsafePointer<xpc_object_t>?, _ count: Int) -> xpc_object_t
```

```c
extern xpc_object_txpc_array_create(xpc_object_t const*objects, size_t count);
```

#### Return Value

A new array object.

#### Discussion

This array must be contiguous and cannot contain any NULL values. If you wish to insert the equivalent of a NULL value, you may use the result of [`xpc_null_create()`](./xpc_null_create%28%29.md).

## Parameters

- `objects`: An array of XPC objects which is to be boxed. The order of this array is preserved in the object. If this array contains a NULL value, the behavior is undefined. This parameter may be NULL only if the count is 0.
- `count`: The number of objects in the given array. If the number passed is less than the actual number of values in the array, only the specified number of items are inserted into the resulting array. If the number passed is more than the the actual number of values, the behavior is undefined.

## See Also

### Array objects
- [struct XPCArray](./xpcarray.md)
  An ordered random-access collection of XPC objects.
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
- [func xpc_array_get_dictionary(xpc_object_t, Int) -> xpc_object_t?](./xpc_array_get_dictionary%28_,_%29.md)
  Returns the dictionary at the specified index in the array.
- [func xpc_array_get_double(xpc_object_t, Int) -> Double](./xpc_array_get_double%28_,_%29.md)
  Gets a double-precision floating point primitive value from an array directly.
- [xpc_array_get_int64](./xpc_array_get_int64%28_,_%29.md)
  Gets a 64-bit integer primitive value from an array directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_array_create(_:_:))*