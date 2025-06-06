# videoEditorControllerDidCancel(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when the user cancels a movie editing operation.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func videoEditorControllerDidCancel(_ editor: UIVideoEditorController)
```

## Parameters

- `editor`: The video editor that the user canceled, not wanting to save changes.

## See Also

- [func videoEditorController(UIVideoEditorController, didSaveEditedVideoToPath: String)](uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didsaveeditedvideotopath:).md)
  Notifies the delegate after the system finishes saving an edited movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel(_:))*