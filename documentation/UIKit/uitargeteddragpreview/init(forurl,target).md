# init(forURL:target:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new targeted drag item preview with a URL and a drag item preview.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
convenience init(forURL url: URL, target: UIDragPreviewTarget)
```

## Return Value

A targeted drag preview for a URL based on the drag item preview target.

## Discussion

This method creates a targeted drag item preview of the URL. The URL preview is a one-line, textual representation that might not show the full URL string. Don’t use a file URL.

## Parameters

- `url`: An Internet address referencing a remote resource, such as a webpage.
- `target`: A drag item preview target.

## See Also

### Initializing a targeted drag item preview
- [convenience init(forURL: URL, title: String?, target: UIDragPreviewTarget)](./init%28forurl,title,target%29.md)
  Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargeteddragpreview/init(forurl:target:))*