# xpc_dictionary_set_value(_:_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Sets the value for the specified key to the specified object.

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
func xpc_dictionary_set_value(_ xdict: xpc_object_t, _ key: UnsafePointer<CChar>, _ value: xpc_object_t?)
```

```c
extern void xpc_dictionary_set_value(xpc_object_t xdict, const char *key, xpc_object_t value);
```

## Parameters

- `xdict`: The dictionary object which is to be manipulated.
- `key`: The key for which the value shall be set.
- `value`: The object to insert. The object is retained by the dictionary. If there already exists a value for the specified key, the old value is released and overwritten by the new value. This parameter may be NULL, in which case the value corresponding to the specified key is deleted if present.

## See Also

### Dictionary objects
- [struct XPCDictionary](./xpcdictionary.md)
  A type that contains key-value pairs, notably used as the container of messages between a client and listener.
- [func xpc_dictionary_create(UnsafePointer<UnsafePointer<CChar>>?, UnsafePointer<xpc_object_t?>?, Int) -> xpc_object_t](./xpc_dictionary_create%28_,_,_%29.md)
  Creates an XPC object that represents a dictionary of XPC objects keyed to C-strings.
- [func xpc_dictionary_create_empty() -> xpc_object_t](./xpc_dictionary_create_empty%28%29.md)
  Creates an XPC object that represents a dictionary of XPC objects keyed to C-strings.
- [func xpc_dictionary_create_connection(xpc_object_t, UnsafePointer<CChar>) -> xpc_connection_t?](./xpc_dictionary_create_connection%28_,_%29.md)
  Creates a connection from a dictionary directly.
- [func xpc_dictionary_create_reply(xpc_object_t) -> xpc_object_t?](./xpc_dictionary_create_reply%28_%29.md)
  Creates a dictionary that is in reply to the specified dictionary.
- [func xpc_dictionary_get_count(xpc_object_t) -> Int](./xpc_dictionary_get_count%28_%29.md)
  Returns the number of values in the dictionary.
- [func xpc_dictionary_get_value(xpc_object_t, UnsafePointer<CChar>) -> xpc_object_t?](./xpc_dictionary_get_value%28_,_%29.md)
  Returns the value for the specified key.
- [func xpc_dictionary_apply(xpc_object_t, (UnsafePointer<CChar>, xpc_object_t) -> Bool) -> Bool](./xpc_dictionary_apply%28_,_%29.md)
  Invokes the specified block for every key-value pair in the dictionary.
- [func xpc_dictionary_dup_fd(xpc_object_t, UnsafePointer<CChar>) -> Int32](./xpc_dictionary_dup_fd%28_,_%29.md)
  Creates a file descriptor from a dictionary directly.
- [func xpc_dictionary_get_array(xpc_object_t, UnsafePointer<CChar>) -> xpc_object_t?](./xpc_dictionary_get_array%28_,_%29.md)
  Returns the array value for the specified key.
- [func xpc_dictionary_get_bool(xpc_object_t, UnsafePointer<CChar>) -> Bool](./xpc_dictionary_get_bool%28_,_%29.md)
  Gets a Boolean primitive value from a dictionary directly.
- [func xpc_dictionary_get_data(xpc_object_t, UnsafePointer<CChar>, UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](./xpc_dictionary_get_data%28_,_,_%29.md)
  Gets a raw data value from a dictionary directly.
- [func xpc_dictionary_get_date(xpc_object_t, UnsafePointer<CChar>) -> Int64](./xpc_dictionary_get_date%28_,_%29.md)
  Gets a date value from a dictionary directly.
- [func xpc_dictionary_get_dictionary(xpc_object_t, UnsafePointer<CChar>) -> xpc_object_t?](./xpc_dictionary_get_dictionary%28_,_%29.md)
  Returns the dictionary value for the specified key.
- [func xpc_dictionary_get_double(xpc_object_t, UnsafePointer<CChar>) -> Double](./xpc_dictionary_get_double%28_,_%29.md)
  Gets a double-precision floating point primitive value from a dictionary directly.
- [xpc_dictionary_get_int64](./xpc_dictionary_get_int64%28_,_%29.md)
  Gets a 64-bit integer primitive value from a dictionary directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_dictionary_set_value(_:_:_:))*