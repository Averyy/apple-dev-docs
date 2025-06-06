# previewParametersProvider

**Framework**: UIKit  
**Kind**: property

The handler block that provides the preview parameters for the specified cell.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var previewParametersProvider: ((UITableViewCell) -> UIDragPreviewParameters?)? { get set }
```

#### Discussion

Specify a custom block when you want to provide a custom preview for your placeholder cell. If you don’t specify a block, the table view uses a default preview for the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropplaceholder/previewparametersprovider)*