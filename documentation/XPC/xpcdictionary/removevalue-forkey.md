# removeValue(forKey:)

**Framework**: Xpc  
**Kind**: method

Removes the given key and its associated value from the dictionary.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
@discardableResult
func removeValue(forKey key: String) -> xpc_object_t?
```

#### Return Value

The value that was removed, or nil if the key was not present in the dictionary.

## Parameters

- `key`: The key to remove along with its associated value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/removevalue(forkey:))*