# values

**Framework**: XPC  
**Kind**: property  
**Role**: Instance Property

A collection containing just the values of the dictionary.

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
var values: [xpc_object_t] { get }
```

## Discussion

A collection containing just the values of the dictionary. When iterated over, values appear in this collection in the same order as they occur in the dictionary’s key-value pairs.

> **Note**:  The complexity of this property is O(*n*) over the dictionary’s [`count`](./count.md).

## See Also

### Accessing keys and values
- [var keys: [String]](./keys.md)
  A collection containing just the keys of the dictionary.
- [subscript(String) -> XPCDictionary?](./subscript%28_%29-4hbmg.md)
  Reads and writes the value associated with the given key as an XPC dictionary.
- [subscript(String) -> String?](./subscript%28_%29-80fs2.md)
  Reads and writes the value associated with the given key as a string.
- [subscript(String) -> Bool?](./subscript%28_%29-gas6.md)
  Reads and writes the value associated with the given key as a Boolean value.
- [subscript(String) -> xpc_object_t?](./subscript%28_%29-4j21u.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript<T>(String) -> T?](./subscript%28_%29-8gyze.md)
  Reads and writes the value associated with the given key as a floating point value.
- [subscript<T>(String) -> T?](./subscript%28_%29-4vrsa.md)
  Reads and writes the value associated with the given key as an unsigned integer value.
- [subscript<T>(String) -> T?](./subscript%28_%29-3i01t.md)
  Reads and writes the value associated with the given key as a signed integer value.
- [subscript(String, as _: XPCDictionary.Type) -> XPCDictionary?](./subscript%28_,as%29-1mm7n.md)
  Reads the value associated with the given key as an XPC dictionary.
- [subscript(String, as _: String.Type) -> String?](./subscript%28_,as%29-4zxc8.md)
  Reads and writes the value associated with the given key as a string.
- [subscript(String, as _: Bool.Type) -> Bool?](./subscript%28_,as%29-18db5.md)
  Reads and writes the value associated with the given key as a Boolean value.
- [subscript(String, as _: any OS_xpc_object.Type) -> xpc_object_t?](./subscript%28_,as%29-5y39v.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript(String, as _: xpc_type_t) -> xpc_object_t?](./subscript%28_,as%29-qjxa.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript<T>(String, as _: T.Type) -> T?](./subscript%28_,as%29-3mzgc.md)
  Reads and writes the value associated with the given key as a floating point value.
- [subscript<T>(String, as _: T.Type) -> T?](./subscript%28_,as%29-119cl.md)
  Reads and writes the value associated with the given key as an integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/values)*