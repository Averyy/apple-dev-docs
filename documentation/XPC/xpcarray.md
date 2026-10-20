# XPCArray

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

An ordered random-access collection of XPC objects.

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
struct XPCArray
```

## Topics

### Creating an array
- [init()](./xpcarray/init%28%29.md)
  Creates a new, empty array.
- [init(xpc_object_t)](./xpcarray/init%28_%29.md)
  Creates a new array that contains the given XPC object.
- [func copy(into: XPCArray)](./xpcarray/copy%28into%29.md)
  Copies the elements of the array to a different array.
### Inspecting an array
- [var isEmpty: Bool](./xpcarray/isempty.md)
  A Boolean value that indicates whether the array is empty.
- [var count: Int](./xpcarray/count.md)
  The number of elements in the array.
### Accessing elements
- [subscript(Int) -> XPCDictionary?](./xpcarray/subscript%28_%29-1s7qq.md)
  Reads and writes the value at the given index as an XPC dictionary.
- [subscript(Int) -> String?](./xpcarray/subscript%28_%29-6c9gh.md)
  Reads and writes the value at the given index as a string.
- [subscript(Int) -> Bool?](./xpcarray/subscript%28_%29-i6v5.md)
  Reads and writes the value at the given index as a Boolean value.
- [subscript(Int) -> xpc_object_t?](./xpcarray/subscript%28_%29-56wjj.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript<T>(Int) -> T?](./xpcarray/subscript%28_%29-8wubg.md)
  Reads and writes the value at the given index as a floating point value.
- [subscript<T>(Int) -> T?](./xpcarray/subscript%28_%29-9x9ho.md)
  Reads and writes the value at the given index as an unsigned integer.
- [subscript<T>(Int) -> T?](./xpcarray/subscript%28_%29-2f94n.md)
  Reads and writes the value at the given index as a signed integer.
- [subscript(Int, as _: XPCDictionary.Type) -> XPCDictionary?](./xpcarray/subscript%28_,as%29-3ae6x.md)
  Reads the value associated with the given key as an XPC dictionary.
- [subscript(Int, as _: String.Type) -> String?](./xpcarray/subscript%28_,as%29-9ukjj.md)
  Reads and writes the value at the given index as a string.
- [subscript(Int, as _: Bool.Type) -> Bool?](./xpcarray/subscript%28_,as%29-1bilh.md)
  Reads and writes the value at the given index as a Boolean value.
- [subscript(Int, as _: any OS_xpc_object.Type) -> xpc_object_t?](./xpcarray/subscript%28_,as%29-931lh.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript(Int, as _: xpc_type_t) -> xpc_object_t?](./xpcarray/subscript%28_,as%29-3tgp4.md)
  Reads and writes the value at the given index as an XPC object.
- [subscript<T>(Int, as _: T.Type) -> T?](./xpcarray/subscript%28_,as%29-2hql9.md)
  Reads and writes the value at the given index as a floating point value.
- [subscript<T>(Int, as _: T.Type) -> T?](./xpcarray/subscript%28_,as%29-6grs4.md)
  Reads and writes the value at the given index as an integer value.
- [subscript(Int, as _: Bool.Type, default _: @autoclosure () -> Bool) -> Bool](./xpcarray/subscript%28_,as,default%29-2bn95.md)
  Reads and writes the value at the given index as a Boolean value, falling back to the given default value.
- [subscript<T>(Int, as _: T.Type, default _: @autoclosure () -> T) -> T](./xpcarray/subscript%28_,as,default%29-3k2qm.md)
  Reads and writes the value at the given index as a floating point value, falling back to the given default value.
- [func withUnsafeUnderlyingArray<ReturnType>((xpc_object_t) throws -> ReturnType) rethrows -> ReturnType](./xpcarray/withunsafeunderlyingarray%28_%29.md)
  Calls a closure with an unsafe reference to the array.
### Iterating over an array’s elements
- [func forEach((XPCArray.IndexValuePair) throws -> Void) rethrows](./xpcarray/foreach%28_%29-6obs3.md)
  Calls the given closure with each element in the array in the same order as a for-in loop.
- [func forEach((Int, xpc_object_t) throws -> Void) rethrows](./xpcarray/foreach%28_%29-2ib8a.md)
  Calls the given closure with an index and element of the array in the same order as a for-in loop.
### Transforming an array
- [func map<ReturnType>((XPCArray.IndexValuePair) throws -> ReturnType) rethrows -> [ReturnType]](./xpcarray/map%28_%29.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
### Supporting types
- [typealias IndexValuePair](./xpcarray/indexvaluepair.md)
  A type that contains an index and the object at that index.
### Subscripts
- [subscript(Int) -> XPCArray?](./xpcarray/subscript%28_%29-6ud0q.md)
  Get or set a value in this array as an XPCArray.
- [subscript(Int) -> XPCEndpoint?](./xpcarray/subscript%28_%29-7io5d.md)
  Get or set a value in this array as an endpoint.
- [subscript(Int) -> uuid_t?](./xpcarray/subscript%28_%29-9akd5.md)
  Get or set a value in this array as a UUID.
- [subscript(Int) -> FileDescriptor?](./xpcarray/subscript%28_%29-9c21w.md)
  Get or set a value in this array as a file descriptor.
- [subscript(Int) -> RawSpan?](./xpcarray/subscript%28_%29-us15.md)
  Get or set a value in this array as data.
- [subscript(Int, as _: uuid_t.Type) -> uuid_t?](./xpcarray/subscript%28_,as%29-4xkvt.md)
  Get a value in this array as a UUID.
- [subscript(Int, as _: FileDescriptor.Type) -> FileDescriptor?](./xpcarray/subscript%28_,as%29-54977.md)
  Get a value in this array as a file descriptor.
- [subscript(Int, as _: XPCEndpoint.Type) -> XPCEndpoint?](./xpcarray/subscript%28_,as%29-5g1u8.md)
  Get a value in this array as an endpoint.
- [subscript(Int, as _: XPCArray.Type) -> XPCArray?](./xpcarray/subscript%28_,as%29-6vjz.md)
  Get a value in this array as an XPCArray.
- [subscript(Int, as _: RawSpan.Type) -> RawSpan?](./xpcarray/subscript%28_,as%29-96zf2.md)
  Get a value in this array as data.
- [subscript(Int, as _: FileDescriptor.Type, default _: @autoclosure () -> FileDescriptor) -> FileDescriptor](./xpcarray/subscript%28_,as,default%29-3h2ng.md)
  Get a value in this array as a file descriptor.
- [subscript(Int, as _: XPCEndpoint.Type, default _: @autoclosure () -> XPCEndpoint) -> XPCEndpoint](./xpcarray/subscript%28_,as,default%29-46zsb.md)
  Get a value in this array as an endpoint.
- [subscript(Int, as _: uuid_t.Type, default _: @autoclosure () -> uuid_t) -> uuid_t](./xpcarray/subscript%28_,as,default%29-4ey7n.md)
  Get a value in this array as a UUID.
- [subscript(Int, as _: XPCArray.Type, default _: @autoclosure () -> XPCArray) -> XPCArray](./xpcarray/subscript%28_,as,default%29-645o4.md)
  Get a value in this array as an XPCArray.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Array objects
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
- [func xpc_array_get_dictionary(xpc_object_t, Int) -> xpc_object_t?](./xpc_array_get_dictionary%28_,_%29.md)
  Returns the dictionary at the specified index in the array.
- [func xpc_array_get_double(xpc_object_t, Int) -> Double](./xpc_array_get_double%28_,_%29.md)
  Gets a double-precision floating point primitive value from an array directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray)*