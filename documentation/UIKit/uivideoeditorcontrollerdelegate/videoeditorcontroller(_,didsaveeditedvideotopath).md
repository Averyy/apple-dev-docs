# videoEditorController(_:didSaveEditedVideoToPath:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate after the system finishes saving an edited movie.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func videoEditorController(_ editor: UIVideoEditorController, didSaveEditedVideoToPath editedVideoPath: String)
```

```objc
- (void) videoEditorController:(UIVideoEditorController *) editor didSaveEditedVideoToPath:(NSString *) editedVideoPath;
```

## Parameters

- `editor`: The video editor that has finished editing and saving a movie.
- `editedVideoPath`: The filesystem path to the edited movie.

## See Also

### Closing the video editor
- [func videoEditorControllerDidCancel(UIVideoEditorController)](./videoeditorcontrollerdidcancel%28_%29.md)
  Notifies the delegate when the user cancels a movie editing operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didsaveeditedvideotopath:))*