# forEach(_:)

**Framework**: Xpc  
**Kind**: method

Calls the given closure with each element in the array in the same order as a for-in loop.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func forEach(_ body: (XPCArray.IndexValuePair) throws -> Void) rethrows
```

## Parameters

- `body`: A closure that takes an element of the array as a parameter.

## See Also

- [func forEach((Int, xpc_object_t) throws -> Void) rethrows](xpcarray/foreach(_:)-2ib8a.md)
  Calls the given closure with an index and element of the array in the same order as a for-in loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/foreach(_:)-6obs3)*