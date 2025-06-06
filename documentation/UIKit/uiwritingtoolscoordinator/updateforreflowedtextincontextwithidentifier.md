# updateForReflowedTextInContextWithIdentifier(_:)

**Framework**: UIKit  
**Kind**: method

Informs the coordinator that a change occurred to the view or its text that requires a layout update.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func updateForReflowedTextInContextWithIdentifier(_ contextID: UUID)
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

Use this method to inform Writing Tools when the geometry of your view changes, or when the text that precedes one of your context objects changes. Changes to the view’s geometry or text can affect the flow of any remaining text, and require a layout update. Writing Tools uses this method to refresh any layout-dependent information it’s currently tracking. For example, it uses it to refresh the location of proofreading marks it’s displaying in your view.

If a text change affects the text inside a context object, call the [`updateRange(_:with:reason:forContextWithIdentifier:)`](uiwritingtoolscoordinator/updaterange(_:with:reason:forcontextwithidentifier:).md) method to report that change instead.

## Parameters

- `contextID`: The unique identifier of the context object affected   by the change. Pass the identifier for the context object that comes   after the changes.

## See Also

- [func updateRange(NSRange, with: NSAttributedString, reason: UIWritingToolsCoordinator.TextUpdateReason, forContextWithIdentifier: UUID)](uiwritingtoolscoordinator/updaterange(_:with:reason:forcontextwithidentifier:).md)
  Informs the coordinator about changes your app made to the text in the specified context object.
- [UIWritingToolsCoordinator.TextUpdateReason](uiwritingtoolscoordinator/textupdatereason.md)
  Constants that specify the reason you updated your view’s content outside of the Writing Tools workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(_:))*