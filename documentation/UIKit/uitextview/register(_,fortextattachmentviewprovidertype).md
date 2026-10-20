# register(_:forTextAttachmentViewProviderType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Register the UITextAttachmentViewProviderReusePolicy for all instances of a particular subclass of NSTextAttachmentViewProvider.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func register(_ policy: UITextAttachmentViewProviderReusePolicy, forTextAttachmentViewProviderType viewProviderType: AnyClass)
```

```objc
- (void) registerTextAttachmentViewProviderReusePolicy:(UITextAttachmentViewProviderReusePolicy) policy forTextAttachmentViewProviderType:(Class) viewProviderType;
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](../managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)

## See Also

### Managing attachment view reuse
- [struct UITextAttachmentViewProviderReusePolicy](../uitextattachmentviewproviderreusepolicy.md)
  An option set that controls whether a text view reuses attachment view providers when scrolling or editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/register(_:fortextattachmentviewprovidertype:))*