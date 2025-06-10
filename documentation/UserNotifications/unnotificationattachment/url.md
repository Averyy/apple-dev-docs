# url

**Framework**: User Notifications  
**Kind**: property

The URL of the file for this attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var url: URL { get }
```

#### Discussion

The file at the specified URL is security scoped to your app. Before you access it, call the [`startAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/Foundation/URL/startAccessingSecurityScopedResource()) method of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL).

## See Also

- [var identifier: String](unnotificationattachment/identifier.md)
  The unique identifier for the attachment.
- [var type: String](unnotificationattachment/type.md)
  The UTI type of the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachment/url)*