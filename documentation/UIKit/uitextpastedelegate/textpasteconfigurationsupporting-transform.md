# textPasteConfigurationSupporting(_:transform:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate to transform the pasted or dropped text item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, transform item: any UITextPasteItem)
```

#### Discussion

This method is called for each text paste item during a paste or drop operation. You’re required to call one of the `setResult` methods (see Setting a text paste item’s result value) on `item`, but the call doesn’t have to be within the scope of the transform method. It can, for example, be part of the asynchronous handling code for the [`itemProvider`](uitextpasteitem/itemprovider.md), or it can be part of a completion block. You can make the call whenever you prefer.

It’s safe to use the provided [`UITextPasteItem`](uitextpasteitem.md) object on any thread, but the transform method is always called on the main thread.

## Parameters

- `textPasteConfigurationSupporting`: The object that received the paste or drop request.
- `item`: The text paste item included in the paste or drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:transform:))*