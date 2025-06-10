# XPC objects

**Framework**: XPC

Encapsulate data in objects that represent primitive types, collections, and more.

## Topics

### Objects
- [typealias xpc_object_t](xpc_object_t.md)
  A type that can describe all XPC objects, including dictionaries, arrays, strings, and numbers.
- [typealias xpc_type_t](xpc_type_t.md)
  A type that describes XPC object types.
- [protocol OS_xpc_object](os_xpc_object.md)
  The interface for an XPC object.
- [class OS_xpc_listener](os_xpc_listener-swift.class.md)
### Identity
- [func xpc_get_type(xpc_object_t) -> xpc_type_t](xpc_get_type(_:).md)
  Returns the type of an object.
- [func xpc_type_get_name(xpc_type_t) -> UnsafePointer<CChar>](xpc_type_get_name(_:).md)
  Returns a string that describes an XPC object type.
- [func xpc_hash(xpc_object_t) -> Int](xpc_hash(_:).md)
  Calculates a hash value for the specified object.
### Comparison
- [func xpc_equal(xpc_object_t, xpc_object_t) -> Bool](xpc_equal(_:_:).md)
  Compares two objects for equality.
### Copying
- [func xpc_copy(xpc_object_t) -> xpc_object_t?](xpc_copy(_:).md)
  Creates a copy of the object.
- [func xpc_copy_description(xpc_object_t) -> UnsafeMutablePointer<CChar>](xpc_copy_description(_:).md)
  Copies a debug string that describes the object.
### Boolean objects
- [func xpc_bool_create(Bool) -> xpc_object_t](xpc_bool_create(_:).md)
  Creates an XPC Boolean object.
- [func xpc_bool_get_value(xpc_object_t) -> Bool](xpc_bool_get_value(_:).md)
  Returns the underlying Boolean value from the object.
- [var XPC_BOOL_TRUE: xpc_object_t](xpc_bool_true-swift.var.md)
  A constant that represents a Boolean value of true.
- [var XPC_BOOL_FALSE: xpc_object_t](xpc_bool_false-swift.var.md)
  A constant that represents a Boolean value of false.
### Data objects
- [func xpc_data_create(UnsafeRawPointer?, Int) -> xpc_object_t](xpc_data_create(_:_:).md)
  Creates an XPC object that represents a buffer of bytes.
- [func xpc_data_create_with_dispatch_data(dispatch_data_t) -> xpc_object_t](xpc_data_create_with_dispatch_data(_:).md)
  Creates an XPC object that represents a buffer of bytes that the specified GCD data object describes.
- [func xpc_data_get_bytes(xpc_object_t, UnsafeMutableRawPointer, Int, Int) -> Int](xpc_data_get_bytes(_:_:_:_:).md)
  Copies the bytes in a data object into the specified buffer.
- [func xpc_data_get_bytes_ptr(xpc_object_t) -> UnsafeRawPointer?](xpc_data_get_bytes_ptr(_:).md)
  Returns a pointer to the internal storage of a data object.
- [func xpc_data_get_length(xpc_object_t) -> Int](xpc_data_get_length(_:).md)
  Returns the length of the data that an XPC data object encapsulates.
### Number objects
- [func xpc_double_create(Double) -> xpc_object_t](xpc_double_create(_:).md)
  Creates an XPC double object.
- [func xpc_double_get_value(xpc_object_t) -> Double](xpc_double_get_value(_:).md)
  Returns the underlying double-precision floating point value from an object.
- [func xpc_int64_create(Int64) -> xpc_object_t](xpc_int64_create(_:).md)
  Creates an XPC signed integer object.
- [func xpc_int64_get_value(xpc_object_t) -> Int64](xpc_int64_get_value(_:).md)
  Returns the underlying signed 64-bit integer value from an object.
- [func xpc_uint64_create(UInt64) -> xpc_object_t](xpc_uint64_create(_:).md)
  Creates an XPC unsigned integer object.
- [func xpc_uint64_get_value(xpc_object_t) -> UInt64](xpc_uint64_get_value(_:).md)
  Returns the underlying unsigned 64-bit integer value from an object.
### Array objects
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
- [func xpc_array_get_double(xpc_object_t, Int) -> Double](xpc_array_get_double(_:_:).md)
  Gets a double-precision floating point primitive value from an array directly.
- [func xpc_array_get_int64(xpc_object_t, Int) -> Int64](xpc_array_get_int64(_:_:).md)
  Gets a 64-bit integer primitive value from an array directly.
- [func xpc_array_get_string(xpc_object_t, Int) -> UnsafePointer<CChar>?](xpc_array_get_string(_:_:).md)
  Gets a C-string value from an array directly.
- [func xpc_array_get_uint64(xpc_object_t, Int) -> UInt64](xpc_array_get_uint64(_:_:).md)
  Gets a 64-bit unsigned integer primitive value from an array directly.
- [func xpc_array_get_uuid(xpc_object_t, Int) -> UnsafePointer<UInt8>?](xpc_array_get_uuid(_:_:).md)
  Gets a UUID value from an array directly.
- [func xpc_array_set_bool(xpc_object_t, Int, Bool)](xpc_array_set_bool(_:_:_:).md)
  Inserts a Boolean primitive value into an array.
- [func xpc_array_set_connection(xpc_object_t, Int, xpc_connection_t)](xpc_array_set_connection(_:_:_:).md)
  Inserts a connection into an array.
- [func xpc_array_set_data(xpc_object_t, Int, UnsafeRawPointer, Int)](xpc_array_set_data(_:_:_:_:).md)
  Inserts a raw data value into an array.
- [func xpc_array_set_date(xpc_object_t, Int, Int64)](xpc_array_set_date(_:_:_:).md)
  Inserts a date value into an array.
- [func xpc_array_set_double(xpc_object_t, Int, Double)](xpc_array_set_double(_:_:_:).md)
  Inserts a double-precision floating point primitive value into an array.
- [func xpc_array_set_fd(xpc_object_t, Int, Int32)](xpc_array_set_fd(_:_:_:).md)
  Inserts a file descriptor into an array.
- [func xpc_array_set_int64(xpc_object_t, Int, Int64)](xpc_array_set_int64(_:_:_:).md)
  Inserts a 64-bit integer primitive value into an array.
- [func xpc_array_set_string(xpc_object_t, Int, UnsafePointer<CChar>)](xpc_array_set_string(_:_:_:).md)
  Inserts a C-string into an array.
- [func xpc_array_set_uint64(xpc_object_t, Int, UInt64)](xpc_array_set_uint64(_:_:_:).md)
  Inserts a 64-bit unsigned integer primitive value into an array.
- [func xpc_array_set_uuid(xpc_object_t, Int, UnsafePointer<UInt8>)](xpc_array_set_uuid(_:_:_:).md)
  Inserts a UUID primitive value into an array.
- [typealias xpc_array_applier_t](xpc_array_applier_t.md)
  A block to invoke for every value in the array.
- [var XPC_ARRAY_APPEND: size_t](xpc_array_append-swift.var.md)
  A constant to pass as the destination index to the class of primitive XPC array setters indicating that the specified primitive needs to append to the array.
### Dictionary objects
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
- [func xpc_dictionary_get_double(xpc_object_t, UnsafePointer<CChar>) -> Double](xpc_dictionary_get_double(_:_:).md)
  Gets a double-precision floating point primitive value from a dictionary directly.
- [func xpc_dictionary_get_int64(xpc_object_t, UnsafePointer<CChar>) -> Int64](xpc_dictionary_get_int64(_:_:).md)
  Gets a 64-bit integer primitive value from a dictionary directly.
- [func xpc_dictionary_get_remote_connection(xpc_object_t) -> xpc_connection_t?](xpc_dictionary_get_remote_connection(_:).md)
  Returns the connection that receives the dictionary.
- [func xpc_dictionary_get_string(xpc_object_t, UnsafePointer<CChar>) -> UnsafePointer<CChar>?](xpc_dictionary_get_string(_:_:).md)
  Gets a C-string value from a dictionary directly.
- [func xpc_dictionary_get_uint64(xpc_object_t, UnsafePointer<CChar>) -> UInt64](xpc_dictionary_get_uint64(_:_:).md)
  Gets a 64-bit unsigned integer primitive value from a dictionary directly.
- [func xpc_dictionary_get_uuid(xpc_object_t, UnsafePointer<CChar>) -> UnsafePointer<UInt8>?](xpc_dictionary_get_uuid(_:_:).md)
  Gets a UUID value from a dictionary directly.
- [func xpc_dictionary_set_bool(xpc_object_t, UnsafePointer<CChar>, Bool)](xpc_dictionary_set_bool(_:_:_:).md)
  Inserts a Boolean primitive value into a dictionary.
- [func xpc_dictionary_set_connection(xpc_object_t, UnsafePointer<CChar>, xpc_connection_t)](xpc_dictionary_set_connection(_:_:_:).md)
  Inserts a connection into a dictionary.
- [func xpc_dictionary_set_data(xpc_object_t, UnsafePointer<CChar>, UnsafeRawPointer, Int)](xpc_dictionary_set_data(_:_:_:_:).md)
  Inserts a raw data value into a dictionary.
- [func xpc_dictionary_set_date(xpc_object_t, UnsafePointer<CChar>, Int64)](xpc_dictionary_set_date(_:_:_:).md)
  Inserts a date primitive value into a dictionary.
- [func xpc_dictionary_set_double(xpc_object_t, UnsafePointer<CChar>, Double)](xpc_dictionary_set_double(_:_:_:).md)
  Inserts a double-precision floating point primitive value into a dictionary.
- [func xpc_dictionary_set_fd(xpc_object_t, UnsafePointer<CChar>, Int32)](xpc_dictionary_set_fd(_:_:_:).md)
  Inserts a file descriptor into a dictionary.
- [func xpc_dictionary_set_int64(xpc_object_t, UnsafePointer<CChar>, Int64)](xpc_dictionary_set_int64(_:_:_:).md)
  Inserts a 64-bit integer primitive value into a dictionary.
- [func xpc_dictionary_set_string(xpc_object_t, UnsafePointer<CChar>, UnsafePointer<CChar>)](xpc_dictionary_set_string(_:_:_:).md)
  Inserts a C-string value into a dictionary.
- [func xpc_dictionary_set_uint64(xpc_object_t, UnsafePointer<CChar>, UInt64)](xpc_dictionary_set_uint64(_:_:_:).md)
  Inserts a 64-bit unsigned integer primitive value into a dictionary.
- [func xpc_dictionary_set_uuid(xpc_object_t, UnsafePointer<CChar>, UnsafePointer<UInt8>)](xpc_dictionary_set_uuid(_:_:_:).md)
  Inserts a UUID primitive value into an array.
- [typealias xpc_dictionary_applier_t](xpc_dictionary_applier_t.md)
  A block to invoke for every key-value pair in the dictionary.
- [func xpc_dictionary_copy_mach_send(xpc_object_t, UnsafePointer<CChar>) -> mach_port_t](xpc_dictionary_copy_mach_send(_:_:).md)
- [func xpc_dictionary_set_mach_send(xpc_object_t, UnsafePointer<CChar>, mach_port_t)](xpc_dictionary_set_mach_send(_:_:_:).md)
### String objects
- [func xpc_string_create(UnsafePointer<CChar>) -> xpc_object_t](xpc_string_create(_:).md)
  Creates an XPC object that represents a null-terminated C-string.
- [func xpc_string_create_with_format_and_arguments(UnsafePointer<CChar>, CVaListPointer) -> xpc_object_t](xpc_string_create_with_format_and_arguments(_:_:).md)
  Creates an XPC object that represents a C-string that the specified format string and argument list pointer generate.
- [func xpc_string_get_length(xpc_object_t) -> Int](xpc_string_get_length(_:).md)
  Returns the length of the underlying string.
- [func xpc_string_get_string_ptr(xpc_object_t) -> UnsafePointer<CChar>?](xpc_string_get_string_ptr(_:).md)
  Returns a pointer to the internal storage of a string object.
### File Descriptor objects
- [func xpc_fd_create(Int32) -> xpc_object_t?](xpc_fd_create(_:).md)
  Creates an XPC object that represents a POSIX file descriptor.
- [func xpc_fd_dup(xpc_object_t) -> Int32](xpc_fd_dup(_:).md)
  Returns a file descriptor that is equivalent to the one that the specified file descriptor object boxes.
### Date objects
- [func xpc_date_create(Int64) -> xpc_object_t](xpc_date_create(_:).md)
  Creates an XPC date object.
- [func xpc_date_create_from_current() -> xpc_object_t](xpc_date_create_from_current().md)
  Creates an XPC date object that represents the current date.
- [func xpc_date_get_value(xpc_object_t) -> Int64](xpc_date_get_value(_:).md)
  Returns the underlying date interval from an object.
### UUID objects
- [func xpc_uuid_create(UnsafePointer<UInt8>) -> xpc_object_t](xpc_uuid_create(_:).md)
  Creates an XPC object that represents a universally unique identifier (UUID).
- [func xpc_uuid_get_bytes(xpc_object_t) -> UnsafePointer<UInt8>?](xpc_uuid_get_bytes(_:).md)
  Copies the UUID that an XPC UUID object boxes into the specified UUID buffer.
### Shared memory objects
- [func xpc_shmem_create(UnsafeMutableRawPointer, Int) -> xpc_object_t](xpc_shmem_create(_:_:).md)
  Creates an XPC object that represents the specified shared memory region.
- [func xpc_shmem_map(xpc_object_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Int](xpc_shmem_map(_:_:).md)
  Maps the region that the XPC shared memory object boxes into the caller’s address space.
### Null objects
- [func xpc_null_create() -> xpc_object_t](xpc_null_create().md)
  Creates an XPC object that represents the null object.
### Object life cycle
- [func xpc_retain(xpc_object_t) -> xpc_object_t](xpc_retain(_:).md)
- [func xpc_release(xpc_object_t)](xpc_release(_:).md)
### Types of objects
- [var XPC_TYPE_ACTIVITY: xpc_type_t](xpc_type_activity-swift.var.md)
  A type that represents the XPC activity object.
- [var XPC_TYPE_ARRAY: xpc_type_t](xpc_type_array-swift.var.md)
  A type that represents an array of XPC objects.
- [var XPC_TYPE_BOOL: xpc_type_t](xpc_type_bool-swift.var.md)
  A type that represents a Boolean value.
- [var XPC_TYPE_CONNECTION: xpc_type_t](xpc_type_connection-swift.var.md)
  A type that represents a connection to a named service.
- [var XPC_TYPE_DATA: xpc_type_t](xpc_type_data-swift.var.md)
  A type that represents an arbitrary buffer of bytes.
- [var XPC_TYPE_DATE: xpc_type_t](xpc_type_date-swift.var.md)
  A type that represents a date interval.
- [var XPC_TYPE_DICTIONARY: xpc_type_t](xpc_type_dictionary-swift.var.md)
  A type that represents a dictionary of XPC objects keyed off of C-strings.
- [var XPC_TYPE_DOUBLE: xpc_type_t](xpc_type_double-swift.var.md)
  A type that represents an IEEE-compliant, double-precision floating point value.
- [var XPC_TYPE_ENDPOINT: xpc_type_t](xpc_type_endpoint-swift.var.md)
  A type that represents a connection in serialized form.
- [var XPC_TYPE_FD: xpc_type_t](xpc_type_fd-swift.var.md)
  A type that represents a POSIX file descriptor.
- [var XPC_TYPE_INT64: xpc_type_t](xpc_type_int64-swift.var.md)
  A type that represents a signed, 64-bit integer value.
- [var XPC_TYPE_NULL: xpc_type_t](xpc_type_null-swift.var.md)
  A type that represents a null object.
- [var XPC_TYPE_SHMEM: xpc_type_t](xpc_type_shmem-swift.var.md)
  A type that represents a region of shared memory.
- [var XPC_TYPE_STRING: xpc_type_t](xpc_type_string-swift.var.md)
  A type that represents a null-terminated C-string.
- [var XPC_TYPE_UINT64: xpc_type_t](xpc_type_uint64-swift.var.md)
  A type that represents an unsigned, 64-bit integer value.
- [var XPC_TYPE_UUID: xpc_type_t](xpc_type_uuid-swift.var.md)
  A type that represents a universally unique identifier.
### Errors
- [struct XPCRichError](xpcricherror.md)
  An error that contains a description and indicates if you can retry the operation that caused the error.
- [var XPC_TYPE_RICH_ERROR: xpc_type_t](xpc_type_rich_error-swift.var.md)
  A type that represents a rich error object.
- [var XPC_TYPE_ERROR: xpc_type_t](xpc_type_error-swift.var.md)
  A type that represents an error object.
- [let XPC_ERROR_KEY_DESCRIPTION: UnsafePointer<CChar>](xpc_error_key_description-swift.var.md)
  A key for querying an error dictionary to retrieve a string with a human-readable description of the error.
- [var XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT: xpc_object_t](xpc_error_peer_code_signing_requirement-swift.var.md)

## See Also

- [Utilities](utilities.md)
  Browse debugging utilities and constants to use with the XPC APIs.
- [XPC connections](xpc-connections.md)
  Create and manage connections to services using connection-based APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc-objects)*