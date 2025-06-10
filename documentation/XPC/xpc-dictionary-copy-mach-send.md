# xpc_dictionary_copy_mach_send(_:_:)

**Framework**: XPC  
**Kind**: func

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_dictionary_copy_mach_send(_ xdict: xpc_object_t, _ key: UnsafePointer<CChar>) -> mach_port_t
```

## See Also

- [struct XPCDictionary](xpcdictionary.md)
  A type that contains key-value pairs, notably used as the container of messages between a client and listener.
- [func xpc_dictionary_create(UnsafePointer<UnsafePointer<CChar>>?, UnsafePointer<xpc_object_t?>?, Int) -> xpc_object_t](xpc_dictionary_create(_:_:_:).md)
  Creates an XPC object that represents a dictionary of XPC objects keyed to C-strings.
- [func xpc_dictionary_create_empty() -> xpc_object_t](xpc_dictionary_create_empty().md)
  Creates an XPC object that represents a dictionary of XPC objects keyed to C-strings.
- [func xpc_dictionary_create_connection(xpc_object_t, UnsafePointer<CChar>) -> xpc_connection_t?](xpc_dictionary_create_connection(_:_:).md)
  Creates a connection from a dictionary directly.
- [func xpc_dictionary_create_reply(xpc_object_t) -> xpc_object_t?](xpc_dictionary_create_reply(_:).md)
  Creates a dictionary that is in reply to the specified dictionary.
- [func xpc_dictionary_set_value(xpc_object_t, UnsafePointer<CChar>, xpc_object_t?)](xpc_dictionary_set_value(_:_:_:).md)
  Sets the value for the specified key to the specified object.
- [func xpc_dictionary_get_count(xpc_object_t) -> Int](xpc_dictionary_get_count(_:).md)
  Returns the number of values in the dictionary.
- [func xpc_dictionary_get_value(xpc_object_t, UnsafePointer<CChar>) -> xpc_object_t?](xpc_dictionary_get_value(_:_:).md)
  Returns the value for the specified key.
- [func xpc_dictionary_apply(xpc_object_t, (UnsafePointer<CChar>, xpc_object_t) -> Bool) -> Bool](xpc_dictionary_apply(_:_:).md)
  Invokes the specified block for every key-value pair in the dictionary.
- [func xpc_dictionary_dup_fd(xpc_object_t, UnsafePointer<CChar>) -> Int32](xpc_dictionary_dup_fd(_:_:).md)
  Creates a file descriptor from a dictionary directly.
- [func xpc_dictionary_get_array(xpc_object_t, UnsafePointer<CChar>) -> xpc_object_t?](xpc_dictionary_get_array(_:_:).md)
  Returns the array value for the specified key.
- [func xpc_dictionary_get_bool(xpc_object_t, UnsafePointer<CChar>) -> Bool](xpc_dictionary_get_bool(_:_:).md)
  Gets a Boolean primitive value from a dictionary directly.
- [func xpc_dictionary_get_data(xpc_object_t, UnsafePointer<CChar>, UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](xpc_dictionary_get_data(_:_:_:).md)
  Gets a raw data value from a dictionary directly.
- [func xpc_dictionary_get_date(xpc_object_t, UnsafePointer<CChar>) -> Int64](xpc_dictionary_get_date(_:_:).md)
  Gets a date value from a dictionary directly.
- [func xpc_dictionary_get_dictionary(xpc_object_t, UnsafePointer<CChar>) -> xpc_object_t?](xpc_dictionary_get_dictionary(_:_:).md)
  Returns the dictionary value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_dictionary_copy_mach_send(_:_:))*