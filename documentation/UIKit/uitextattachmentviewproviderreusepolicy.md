# UITextAttachmentViewProviderReusePolicy

**Framework**: UIKit  
**Kind**: struct

An option set that controls whether a text view reuses attachment view providers when scrolling or editing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct UITextAttachmentViewProviderReusePolicy
```

#### Overview

By default, when content scrolls out of the visible area, `UITextView` removes the attachment view from the view hierarchy. [`NSTextAttachmentViewProvider`](nstextattachmentviewprovider.md) itself persists, but the text view may recreate its view when the content returns. Editing the paragraph containing an attachment has a more significant effect: Because [`NSTextLayoutFragment`](nstextlayoutfragment.md) is immutable, the text view replaces the existing fragment, discarding and recreating any [`NSTextAttachmentViewProvider`](nstextattachmentviewprovider.md) instances it holds. For attachments with views like a media player, a drawing canvas, or a focused control, either behavior can cause views to flicker or lose their state.

To reuse providers instead of recreating them, register a reuse policy for your view provider subclass:

```swift
textView.register(
    [.onScrollingOutOfViewport, .onEditingInlineParagraphs],
    forTextAttachmentViewProviderType: MyAttachmentViewProvider.self
)
```

You can use [`onScrollingOutOfViewport`](uitextattachmentviewproviderreusepolicy/onscrollingoutofviewport.md) or [`onEditingInlineParagraphs`](uitextattachmentviewproviderreusepolicy/oneditinginlineparagraphs.md) on their own, or combine them to cover both scrolling and editing. Once registered, the reuse policy applies to every instance of that view provider subclass for as long as the text view exists.

Use [`onScrollingOutOfViewport`](uitextattachmentviewproviderreusepolicy/onscrollingoutofviewport.md) to keep an attachment view in the view hierarchy when its content scrolls out of the visible area — when it scrolls back into view, the text view reuses the existing view instead of recreating it, preserving states like first responder status and media playback position. Use [`onEditingInlineParagraphs`](uitextattachmentviewproviderreusepolicy/oneditinginlineparagraphs.md) to keep a provider when someone edits the paragraph containing it; on the next layout pass, the text view reuses it instead of creating a new one, which prevents visible flicker when someone types near an attachment.

## Topics

### Creating a reuse policy
- [init(rawValue: UInt)](uitextattachmentviewproviderreusepolicy/init(rawvalue:).md)
### Specifying reuse policy options
- [static var onScrollingOutOfViewport: UITextAttachmentViewProviderReusePolicy](uitextattachmentviewproviderreusepolicy/onscrollingoutofviewport.md)
- [static var onEditingInlineParagraphs: UITextAttachmentViewProviderReusePolicy](uitextattachmentviewproviderreusepolicy/oneditinginlineparagraphs.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func register(UITextAttachmentViewProviderReusePolicy, forTextAttachmentViewProviderType: AnyClass)](uitextview/register(_:fortextattachmentviewprovidertype:).md)
  Register the UITextAttachmentViewProviderReusePolicy for all instances of a particular subclass of NSTextAttachmentViewProvider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextattachmentviewproviderreusepolicy)*