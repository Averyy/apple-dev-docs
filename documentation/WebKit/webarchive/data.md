# data

**Framework**: Webkit  
**Kind**: property

The data representation of the receiver.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var data: Data! { get }
```

#### Discussion

Can be used to save the web archive to a file, to put it on the pasteboard using the [`WebArchivePboardType`](webarchivepboardtype.md) type, or used to initialize another web archive using the [`init(data:)`](webarchive/init(data:).md) method.

## See Also

- [var mainResource: WebResource!](webarchive/mainresource.md)
  The receiver’s main resource.
- [var subresources: [Any]!](webarchive/subresources.md)
  The receiver’s subresources, or `nil` if there are none.
- [var subframeArchives: [Any]!](webarchive/subframearchives.md)
  Archives representing the receiver’s subresources or `nil` if there are none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webarchive/data)*