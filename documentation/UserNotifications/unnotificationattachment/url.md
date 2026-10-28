# url

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSURL * URL;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSURL * URL;
```

## Discussion

The file at the specified URL is security scoped to your app. Before you access it, call the [`startAccessingSecurityScopedResource()`](../../Foundation/url/startaccessingsecurityscopedresource%28%29.md) method of [`NSURL`](../../Foundation/nsurl.md).

## See Also

### Getting the Attachment Contents
- [var identifier: String](./identifier.md)
  The unique identifier for the attachment.
- [var type: String](./type.md)
  The UTI type of the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachment/url)*