# reload(fromOrigin:)

**Framework**: WebKit  
**Kind**: method

Reloads the current webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@discardableResult
@MainActor final func reload(fromOrigin: Bool = false) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
```

#### Return Value

An async sequence you use to track the loading progress of the navigation. If the `Task` enclosing the sequence is cancelled, the page will stop loading all resources.

## Parameters

- `fromOrigin`: If  , end-to-end revalidation of the content using cache-validating conditionals   is performed, if possible.

## See Also

- [func stopLoading()](webpage/stoploading.md)
  Stops loading all resources on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/reload(fromorigin:))*