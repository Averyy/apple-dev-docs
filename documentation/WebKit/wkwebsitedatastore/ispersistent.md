# isPersistent

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether this object stores data to disk.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isPersistent: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the data store writes data to disk, or [`false`](https://developer.apple.com/documentation/swift/false) if it doesn’t.

## See Also

- [var identifier: UUID?](wkwebsitedatastore/identifier.md)
  An identifier that uniquely identifies a data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/ispersistent)*