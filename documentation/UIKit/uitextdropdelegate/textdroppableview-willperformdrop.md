# textDroppableView(_:willPerformDrop:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the drop operation is about to happen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textDroppableView(_ textDroppableView: any UIView & UITextDroppable, willPerformDrop drop: any UITextDropRequest)
```

#### Discussion

If you need to modify the drag items before the drop operation happens, provide the text view a [`pasteDelegate`](uitextpasteconfigurationsupporting/pastedelegate.md) object that implements the [`paste(itemProviders:)`](uipasteconfigurationsupporting/paste(itemproviders:).md) method. In the implementation, do the item conversion and paste the text.

## Parameters

- `textDroppableView`: The text view that received the drop activity.
- `drop`: The drop request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:willperformdrop:))*