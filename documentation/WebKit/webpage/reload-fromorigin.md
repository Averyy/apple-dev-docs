# reload(fromOrigin:)

**Framework**: WebKit  
**Kind**: method

Reloads the current webpage.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@discardableResult
@MainActor final func reload(fromOrigin: Bool = false) -> WebPage.NavigationID?
```

#### Return Value

A navigation identifier you use to track the loading progress of the request.

## Parameters

- `fromOrigin`: If  , end-to-end revalidation of the content using cache-validating conditionals   is performed, if possible.

## See Also

- [func stopLoading()](webpage/stoploading.md)
  Stops loading all resources on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/reload(fromorigin:))*