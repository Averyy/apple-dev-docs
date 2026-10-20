# copy(into:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Copies the keys and values of the dictionary to a different dictionary.

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
func copy(into destination: XPCDictionary)
```

## Parameters

- `destination`: The dictionary to copy the keys and values into.

## See Also

### Creating a dictionary
- [init()](./init%28%29.md)
  Creates an empty dictionary.
- [init(xpc_object_t)](./init%28_%29.md)
  Creates a dictionary using the keys and values in the specified object parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/copy(into:))*