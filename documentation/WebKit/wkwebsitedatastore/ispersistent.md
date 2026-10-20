# isPersistent

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this object stores data to disk.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var isPersistent: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPersistent) BOOL persistent;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the data store writes data to disk, or [`false`](../../Swift/false.md) if it doesn’t.

## See Also

### Inspecting data store properties
- [var identifier: UUID?](./identifier.md)
  An identifier that uniquely identifies a data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/ispersistent)*