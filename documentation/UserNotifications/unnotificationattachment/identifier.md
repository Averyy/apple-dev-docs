# identifier

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var identifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * identifier;
```

## See Also

### Getting the Attachment Contents
- [var url: URL](./url.md)
  The URL of the file for this attachment.
- [var type: String](./type.md)
  The UTI type of the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachment/identifier)*