# videoEditorController(_:didSaveEditedVideoToPath:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate after the system finishes saving an edited movie.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func videoEditorController(_ editor: UIVideoEditorController, didSaveEditedVideoToPath editedVideoPath: String)
```

## Parameters

- `editor`: The video editor that has finished editing and saving a movie.
- `editedVideoPath`: The filesystem path to the edited movie.

## See Also

- [func videoEditorControllerDidCancel(UIVideoEditorController)](uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel(_:).md)
  Notifies the delegate when the user cancels a movie editing operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didsaveeditedvideotopath:))*