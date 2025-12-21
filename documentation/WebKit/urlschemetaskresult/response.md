# URLSchemeTaskResult.response(_:)

**Framework**: WebKit  
**Kind**: case

The response to return to WebKit. The response value must include the MIME type of the request resource.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case response(URLResponse)
```

#### Discussion

This value is used to provide WebKit with the MIME type of the requested resource and its expected size. This must be added to the task result sequence at least once, but may be added multiple times if needed. It must be added to the sequence before any data values are.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemetaskresult/response(_:))*