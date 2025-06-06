# init(scheme:host:path:)

**Framework**: Webkit  
**Kind**: init

Returns a pattern object for the specified scheme, host, and path strings.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
init(scheme: String, host: String, path: String) throws
```

#### Return Value

A pattern object, or `nil` if any of the strings are invalid and an error will be set.

## Parameters

- `scheme`: On output, a pointer to an error object that describes why the method failed, or   if no error occurred. If you are not interested in the error information, pass   for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/init(scheme:host:path:))*