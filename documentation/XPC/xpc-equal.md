# xpc_equal(_:_:)

**Framework**: Xpc  
**Kind**: func

Compares two objects for equality.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_equal(_ object1: xpc_object_t, _ object2: xpc_object_t) -> Bool
```

#### Return Value

Returns true if the objects are equal, otherwise false. Two objects must be of the same type in order to be equal.

#### Discussion

For two arrays to be equal, they must contain the same values at the same indexes. For two dictionaries to be equal, they must contain the same values for the same keys.

Two objects being equal implies that their hashes (as returned by [`xpc_hash(_:)`](xpc_hash(_:).md)) are also equal.

## Parameters

- `object1`: The first object to compare.
- `object2`: The second object to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_equal(_:_:))*