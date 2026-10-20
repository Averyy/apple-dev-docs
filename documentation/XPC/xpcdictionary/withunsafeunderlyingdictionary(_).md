# withUnsafeUnderlyingDictionary(_:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Calls a closure with an unsafe reference to the dictionary.

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
func withUnsafeUnderlyingDictionary<ReturnType>(_ closure: (xpc_object_t) throws -> ReturnType) rethrows -> ReturnType
```

#### Return Value

The return value, if any, of the closure.

#### Discussion

> ⚠️ **Warning**:  It’s possible for `closure` to perform operations on the dictionary that cause the receiving dictionary to no longer wrap the underlying dictionary.

## Parameters

- `closure`: A closure that takes an [`xpc_object_t`](../xpc_object_t.md) parameter. If `closure` has a return value, that value is also used as the return value for the withUnsafeUnderlyingDictionary(body:) function.

## See Also

### Accessing keys and values
- [var keys: [String]](./keys.md)
  A collection containing just the keys of the dictionary.
- [var values: [xpc_object_t]](./values.md)
  A collection containing just the values of the dictionary.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/withunsafeunderlyingdictionary(_:))*