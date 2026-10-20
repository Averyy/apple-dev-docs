# init(_:)

**Framework**: XPC  
**Kind**: init  
**Role**: Initializer

Creates a dictionary using the keys and values in the specified object parameter.

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
init(_ value: xpc_object_t)
```

## Parameters

- `value`: An XPC dictionary object. The object’s type must be [`XPC_TYPE_DICTIONARY`](../xpc_type_dictionary-swift.var.md).

## See Also

### Creating a dictionary
- [init()](./init%28%29.md)
  Creates an empty dictionary.
- [func copy(into: XPCDictionary)](./copy%28into%29.md)
  Copies the keys and values of the dictionary to a different dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/init(_:))*