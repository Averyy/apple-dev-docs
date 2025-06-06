# withUnsafeUnderlyingDictionary(_:)

**Framework**: Xpc  
**Kind**: method

Calls a closure with an unsafe reference to the dictionary.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func withUnsafeUnderlyingDictionary<ReturnType>(_ closure: (xpc_object_t) throws -> ReturnType) rethrows -> ReturnType
```

#### Return Value

The return value, if any, of the closure.

#### Discussion

> ⚠️ **Warning**:  It’s possible for `closure` to perform operations on the dictionary that cause the receiving dictionary to no longer wrap the underlying dictionary.

 It’s possible for `closure` to perform operations on the dictionary that cause the receiving dictionary to no longer wrap the underlying dictionary.

## Parameters

- `closure`: A closure that takes an   parameter. If   has a return value, that value is also used as the return value for the withUnsafeUnderlyingDictionary(body:) function.

## See Also

- [var keys: [String]](xpcdictionary/keys.md)
  A collection containing just the keys of the dictionary.
- [var values: [xpc_object_t]](xpcdictionary/values.md)
  A collection containing just the values of the dictionary.
- [subscript(String) -> XPCDictionary?](xpcdictionary/subscript(_:)-4hbmg.md)
  Reads and writes the value associated with the given key as an XPC dictionary.
- [subscript(String) -> String?](xpcdictionary/subscript(_:)-80fs2.md)
  Reads and writes the value associated with the given key as a string.
- [subscript(String) -> Bool?](xpcdictionary/subscript(_:)-gas6.md)
  Reads and writes the value associated with the given key as a Boolean value.
- [subscript(String) -> xpc_object_t?](xpcdictionary/subscript(_:)-4j21u.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript<T>(String) -> T?](xpcdictionary/subscript(_:)-8gyze.md)
  Reads and writes the value associated with the given key as a floating point value.
- [subscript<T>(String) -> T?](xpcdictionary/subscript(_:)-4vrsa.md)
  Reads and writes the value associated with the given key as an unsigned integer value.
- [subscript<T>(String) -> T?](xpcdictionary/subscript(_:)-3i01t.md)
  Reads and writes the value associated with the given key as a signed integer value.
- [subscript(String, as _: XPCDictionary.Type) -> XPCDictionary?](xpcdictionary/subscript(_:as:)-1mm7n.md)
  Reads the value associated with the given key as an XPC dictionary.
- [subscript(String, as _: String.Type) -> String?](xpcdictionary/subscript(_:as:)-4zxc8.md)
  Reads and writes the value associated with the given key as a string.
- [subscript(String, as _: Bool.Type) -> Bool?](xpcdictionary/subscript(_:as:)-18db5.md)
  Reads and writes the value associated with the given key as a Boolean value.
- [subscript(String, as _: any OS_xpc_object.Type) -> xpc_object_t?](xpcdictionary/subscript(_:as:)-5y39v.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript(String, as _: xpc_type_t) -> xpc_object_t?](xpcdictionary/subscript(_:as:)-qjxa.md)
  Reads and writes the value associated with the given key as an XPC object.
- [subscript<T>(String, as _: T.Type) -> T?](xpcdictionary/subscript(_:as:)-3mzgc.md)
  Reads and writes the value associated with the given key as a floating point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/withunsafeunderlyingdictionary(_:))*