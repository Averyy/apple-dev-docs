# videoEditorControllerDidCancel(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when the user cancels a movie editing operation.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func videoEditorControllerDidCancel(_ editor: UIVideoEditorController)
```

```objc
- (void) videoEditorControllerDidCancel:(UIVideoEditorController *) editor;
```

## Parameters

- `editor`: The video editor that the user canceled, not wanting to save changes.

## See Also

### Closing the video editor
- [func videoEditorController(UIVideoEditorController, didSaveEditedVideoToPath: String)](./videoeditorcontroller%28_,didsaveeditedvideotopath%29.md)
  Notifies the delegate after the system finishes saving an edited movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel(_:))*