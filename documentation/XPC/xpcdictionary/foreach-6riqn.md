# forEach(_:)

**Framework**: Xpc  
**Kind**: method

Calls the given closure with each key and value in the dictionary in the same order as a for-in loop.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func forEach(_ body: (String, xpc_object_t) throws -> Void) rethrows
```

## Parameters

- `body`: A closure that takes a key and a value as parameters.

## See Also

- [func forEach((XPCDictionary.KeyValuePair) throws -> Void) rethrows](xpcdictionary/foreach(_:)-9hufx.md)
  Calls the given closure with each element in the dictionary in the same order as a for-in loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/foreach(_:)-6riqn)*