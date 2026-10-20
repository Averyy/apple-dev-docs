# type

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The UTI type of the attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var type: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * type;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * type;
```

#### Discussion

The system derives the value of this property from the attachment data.

## See Also

### Getting the Attachment Contents
- [var identifier: String](./identifier.md)
  The unique identifier for the attachment.
- [var url: URL](./url.md)
  The URL of the file for this attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachment/type)*