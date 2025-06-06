# init(forURL:title:target:)

**Framework**: UIKit  
**Kind**: init

Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
convenience init(for url: URL, title: String?, target: UIDragPreviewTarget)
```

#### Return Value

A drag preview for a URL with a title based on the specified drag item preview target.

#### Discussion

This method creates a two-line drag item preview, with the title displayed on the first line. The second line is a textual representation of the URL that might not show the full URL string. Don’t use a file URL. Passing `nil` for the title is the same as calling [`init(forURL:target:)`](uitargeteddragpreview/init(forurl:target:).md).

## Parameters

- `url`: An Internet address referencing a remote resource, such as a webpage.
- `title`: A title for the URL.
- `target`: A drag item preview target.

## See Also

- [convenience init(forURL: URL, target: UIDragPreviewTarget)](uitargeteddragpreview/init(forurl:target:).md)
  Initializes a new targeted drag item preview with a URL and a drag item preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargeteddragpreview/init(forurl:title:target:))*