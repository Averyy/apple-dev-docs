# init(mainResource:subresources:subframeArchives:)

**Framework**: Webkit  
**Kind**: init

Initializes the receiver with a resource and optional subresources and subframe archives..

**Availability**:
- macOS 10.3+

## Declaration

```swift
init!(mainResource: WebResource!, subresources: [Any]!, subframeArchives: [Any]!)
```

#### Discussion

This method initializes and returns the receiver by setting the main resource to `mainResource`, and setting the subresources and subframe archives if supplied. The `subresources` argument should be an array of WebResource objects or `nil` if none are specified. The `subframeArchives` should be and array of WebArchive objects used by the subframes or `nil` if none are specified.

## See Also

- [init!(data: Data!)](webarchive/init(data:).md)
  Initializes and returns the receiver, specifying the initial content data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webarchive/init(mainresource:subresources:subframearchives:))*