# init(string:)

**Framework**: Webkit  
**Kind**: init

Returns a pattern object for the specified pattern string.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
init(string: String) throws
```

#### Return Value

A pattern object, or `nil` if the pattern string is invalid and an error will be set.

## Parameters

- `string`: On output, a pointer to an error object that describes why the method failed, or   if no error occurred. If you are not interested in the error information, pass   for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/init(string:))*