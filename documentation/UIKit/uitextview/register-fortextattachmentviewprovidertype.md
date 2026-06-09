# register(_:forTextAttachmentViewProviderType:)

**Framework**: UIKit  
**Kind**: method

Register the UITextAttachmentViewProviderReusePolicy for all instances of a particular subclass of NSTextAttachmentViewProvider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func register(_ policy: UITextAttachmentViewProviderReusePolicy, forTextAttachmentViewProviderType viewProviderType: AnyClass)
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)

## See Also

- [struct UITextAttachmentViewProviderReusePolicy](uitextattachmentviewproviderreusepolicy.md)
  An option set that controls whether a text view reuses attachment view providers when scrolling or editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/register(_:fortextattachmentviewprovidertype:))*