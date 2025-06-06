# init(_:)

**Framework**: Xpc  
**Kind**: init

Creates a dictionary using the keys and values in the specified object parameter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
init(_ value: xpc_object_t)
```

## Parameters

- `value`: An XPC dictionary object. The object’s type must be  .

## See Also

- [init()](xpcdictionary/init.md)
  Creates an empty dictionary.
- [func copy(into: XPCDictionary)](xpcdictionary/copy(into:).md)
  Copies the keys and values of the dictionary to a different dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/init(_:))*