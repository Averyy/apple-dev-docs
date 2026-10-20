# XPCDictionary

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

A type that contains key-value pairs, notably used as the container of messages between a client and listener.

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
struct XPCDictionary
```

## Topics

### Creating a dictionary
- [init()](./xpcdictionary/init%28%29.md)
  Creates an empty dictionary.
- [init(xpc_object_t)](./xpcdictionary/init%28_%29.md)
  Creates a dictionary using the keys and values in the specified object parameter.
- [func copy(into: XPCDictionary)](./xpcdictionary/copy%28into%29.md)
  Copies the keys and values of the dictionary to a different dictionary.
### Replying to client messages
- [func reply(XPCDictionary)](./xpcdictionary/reply%28_%29.md)
  Sends a reply to the originator of the dictionary.
### Inspecting a dictionary
- [var isEmpty: Bool](./xpcdictionary/isempty.md)
  A Boolean value that indicates whether the dictionary is empty.
- [var count: Int](./xpcdictionary/count.md)
  The number of key-value pairs in the dictionary.
### Accessing keys and values
- [var keys: [String]](./xpcdictionary/keys.md)
  A collection containing just the keys of the dictionary.
- [var values: [xpc_object_t]](./xpcdictionary/values.md)
  A collection containing just the values of the dictionary.
- [subscript(String) -> XPCDictionary?](./xpcdictionary/subscript%28_%29-4hbmg.md)
  Reads and writes the value associated with the given key as an XPC dictionary.
- [subscript(String) -> String?](./xpcdictionary/subscript%28_%29-80fs2.md)
  Reads and writes the value associated with the given key as a string.
- [subscript(String) -> Bool?](./xpcdictionary/subscript%28_%29-gas6.md)
  Reads and writes the value associated with the given key as a Boolean value.
- [subscript(String) -> xpc_object_t?](./xpcdictionary/subscript%28_%29-4j21u.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript<T>(String) -> T?](./xpcdictionary/subscript%28_%29-8gyze.md)
  Reads and writes the value associated with the given key as a floating point value.
- [subscript<T>(String) -> T?](./xpcdictionary/subscript%28_%29-4vrsa.md)
  Reads and writes the value associated with the given key as an unsigned integer value.
- [subscript<T>(String) -> T?](./xpcdictionary/subscript%28_%29-3i01t.md)
  Reads and writes the value associated with the given key as a signed integer value.
- [subscript(String, as _: XPCDictionary.Type) -> XPCDictionary?](./xpcdictionary/subscript%28_,as%29-1mm7n.md)
  Reads the value associated with the given key as an XPC dictionary.
- [subscript(String, as _: String.Type) -> String?](./xpcdictionary/subscript%28_,as%29-4zxc8.md)
  Reads and writes the value associated with the given key as a string.
- [subscript(String, as _: Bool.Type) -> Bool?](./xpcdictionary/subscript%28_,as%29-18db5.md)
  Reads and writes the value associated with the given key as a Boolean value.
- [subscript(String, as _: any OS_xpc_object.Type) -> xpc_object_t?](./xpcdictionary/subscript%28_,as%29-5y39v.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript(String, as _: xpc_type_t) -> xpc_object_t?](./xpcdictionary/subscript%28_,as%29-qjxa.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript<T>(String, as _: T.Type) -> T?](./xpcdictionary/subscript%28_,as%29-3mzgc.md)
  Reads and writes the value associated with the given key as a floating point value.
- [subscript<T>(String, as _: T.Type) -> T?](./xpcdictionary/subscript%28_,as%29-119cl.md)
  Reads and writes the value associated with the given key as an integer value.
- [subscript(String, as _: Bool.Type, default _: @autoclosure () -> Bool) -> Bool](./xpcdictionary/subscript%28_,as,default%29-5ufgs.md)
  Reads and writes the value associated with the given key as a Boolean value, falling back to the given default value.
- [subscript<T>(String, as _: T.Type, default _: @autoclosure () -> T) -> T](./xpcdictionary/subscript%28_,as,default%29-4ssx3.md)
  Reads and writes the value associated with the given key converted to the specified type, falling back to the given default value.
- [func withUnsafeUnderlyingDictionary<ReturnType>((xpc_object_t) throws -> ReturnType) rethrows -> ReturnType](./xpcdictionary/withunsafeunderlyingdictionary%28_%29.md)
  Calls a closure with an unsafe reference to the dictionary.
### Removing keys and values
- [func removeValue(forKey: String) -> xpc_object_t?](./xpcdictionary/removevalue%28forkey%29.md)
  Removes the given key and its associated value from the dictionary.
### Supporting types
- [XPCDictionary.KeyValuePair](./xpcdictionary/keyvaluepair.md)
  A type that contains a dictionary’s key-value pair.
### Iterating over keys and values
- [func forEach((XPCDictionary.KeyValuePair) throws -> Void) rethrows](./xpcdictionary/foreach%28_%29-9hufx.md)
  Calls the given closure with each element in the dictionary in the same order as a for-in loop.
- [func forEach((String, xpc_object_t) throws -> Void) rethrows](./xpcdictionary/foreach%28_%29-6riqn.md)
  Calls the given closure with each key and value in the dictionary in the same order as a for-in loop.
### Transforming a dictionary
- [func map<ReturnType>((XPCDictionary.KeyValuePair) throws -> ReturnType) rethrows -> [ReturnType]](./xpcdictionary/map%28_%29.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
### Subscripts
- [subscript(String) -> uuid_t?](./xpcdictionary/subscript%28_%29-11qvo.md)
  Get or set a value in this dictionary as a UUID.
- [subscript(String) -> XPCEndpoint?](./xpcdictionary/subscript%28_%29-2p7tp.md)
  Get or set an `XPCEndpoint` value in this dictionary.
- [subscript(String) -> FileDescriptor?](./xpcdictionary/subscript%28_%29-hl1w.md)
  Get or set a value in this dictionary as a file descriptor.
- [subscript(String) -> RawSpan?](./xpcdictionary/subscript%28_%29-n49r.md)
  Get or set a value in this dictionary as data.
- [subscript(String) -> XPCArray?](./xpcdictionary/subscript%28_%29-u6bo.md)
  Get or set a value in this dictionary as an XPCArray.
- [subscript(String, as _: RawSpan.Type) -> RawSpan?](./xpcdictionary/subscript%28_,as%29-1nvet.md)
  Get a value in this dictionary as data.
- [subscript(String, as _: FileDescriptor.Type) -> FileDescriptor?](./xpcdictionary/subscript%28_,as%29-279le.md)
  Get a value in this dictionary as a file descriptor.
- [subscript(String, as _: XPCArray.Type) -> XPCArray?](./xpcdictionary/subscript%28_,as%29-58a41.md)
  Get a value in this dictionary as an XPCArray.
- [subscript(String, as _: XPCEndpoint.Type) -> XPCEndpoint?](./xpcdictionary/subscript%28_,as%29-7rdzi.md)
  Get an `XPCEndpoint` value in this dictionary.
- [subscript(String, as _: uuid_t.Type) -> uuid_t?](./xpcdictionary/subscript%28_,as%29-91g9b.md)
  Get a value in this dictionary as a UUID.
- [subscript(String, as _: XPCArray.Type, default _: @autoclosure () -> XPCArray) -> XPCArray](./xpcdictionary/subscript%28_,as,default%29-17z80.md)
  Get a value in this dictionary as an XPCArray.
- [subscript(String, as _: FileDescriptor.Type, default _: @autoclosure () -> FileDescriptor) -> FileDescriptor](./xpcdictionary/subscript%28_,as,default%29-51ffh.md)
  Get a value in this dictionary as a file descriptor.
- [subscript(String, as _: uuid_t.Type, default _: @autoclosure () -> uuid_t) -> uuid_t](./xpcdictionary/subscript%28_,as,default%29-vwea.md)
  Get a value in this dictionary as a UUID.
### Default Implementations
- [ExpressibleByDictionaryLiteral Implementations](./xpcdictionary/expressiblebydictionaryliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByDictionaryLiteral](../Swift/expressiblebydictionaryliteral.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Dictionary objects
- [func xpc_dictionary_create(UnsafePointer<UnsafePointer<CChar>>?, UnsafePointer<xpc_object_t?>?, Int) -> xpc_object_t](./xpc_dictionary_create%28_,_,_%29.md)
  Creates an XPC object that represents a dictionary of XPC objects keyed to C-strings.
- [func xpc_dictionary_create_empty() -> xpc_object_t](./xpc_dictionary_create_empty%28%29.md)
  Creates an XPC object that represents a dictionary of XPC objects keyed to C-strings.
- [func xpc_dictionary_create_connection(xpc_object_t, UnsafePointer<CChar>) -> xpc_connection_t?](./xpc_dictionary_create_connection%28_,_%29.md)
  Creates a connection from a dictionary directly.
- [func xpc_dictionary_create_reply(xpc_object_t) -> xpc_object_t?](./xpc_dictionary_create_reply%28_%29.md)
  Creates a dictionary that is in reply to the specified dictionary.
- [func xpc_dictionary_set_value(xpc_object_t, UnsafePointer<CChar>, xpc_object_t?)](./xpc_dictionary_set_value%28_,_,_%29.md)
  Sets the value for the specified key to the specified object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary)*