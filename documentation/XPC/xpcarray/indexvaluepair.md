# XPCArray.IndexValuePair

**Framework**: XPC  
**Kind**: typealias

A type that contains an index and the object at that index.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
typealias IndexValuePair = (index: Int, value: xpc_object_t)
```

#### Discussion

[`XPCArray`](xpcarray.md) exposes its values as instances of [`xpc_object_t`](xpc_object_t.md) even if they were originally set with other types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/indexvaluepair)*