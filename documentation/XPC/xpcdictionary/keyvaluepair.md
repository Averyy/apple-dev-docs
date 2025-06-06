# XPCDictionary.KeyValuePair

**Framework**: Xpc  
**Kind**: typealias

A type that contains a dictionary’s key-value pair.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
typealias KeyValuePair = (key: String, value: xpc_object_t)
```

#### Discussion

[`XPCDictionary`](xpcdictionary.md) exposes its values as instances of [`xpc_object_t`](xpc_object_t.md) even if they were originally set with other types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/keyvaluepair)*