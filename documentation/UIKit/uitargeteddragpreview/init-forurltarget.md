# init(forURL:target:)

**Framework**: UIKit  
**Kind**: init

Initializes a new targeted drag item preview with a URL and a drag item preview.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
convenience init(for url: URL, target: UIDragPreviewTarget)
```

#### Return Value

A targeted drag preview for a URL based on the drag item preview target.

#### Discussion

This method creates a targeted drag item preview of the URL. The URL preview is a one-line, textual representation that might not show the full URL string. Don’t use a file URL.

## Parameters

- `url`: An Internet address referencing a remote resource, such as a webpage.
- `target`: A drag item preview target.

## See Also

- [convenience init(forURL: URL, title: String?, target: UIDragPreviewTarget)](uitargeteddragpreview/init(forurl:title:target:).md)
  Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargeteddragpreview/init(forurl:target:))*