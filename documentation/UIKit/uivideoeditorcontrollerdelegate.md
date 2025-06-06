# UIVideoEditorControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods that your delegate object must implement to respond to the video editor.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIVideoEditorControllerDelegate : NSObjectProtocol
```

#### Overview

The methods of this protocol notify your delegate when the system has saved an edited movie or the user has canceled editing to discard any changes. There’s also a method for responding to errors encountered by the video editor.

The delegate methods are responsible for dismissing the video editor when the operation completes. To dismiss the editor, call the [`dismiss(animated:completion:)`](uiviewcontroller/dismiss(animated:completion:).md) method of the parent controller responsible for displaying the video editor. The video editor is described in [`UIVideoEditorController`](uivideoeditorcontroller.md).

## Topics

### Closing the video editor
- [func videoEditorController(UIVideoEditorController, didSaveEditedVideoToPath: String)](uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didsaveeditedvideotopath:).md)
  Notifies the delegate after the system finishes saving an edited movie.
- [func videoEditorControllerDidCancel(UIVideoEditorController)](uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel(_:).md)
  Notifies the delegate when the user cancels a movie editing operation.
### Handling errors
- [func videoEditorController(UIVideoEditorController, didFailWithError: any Error)](uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didfailwitherror:).md)
  Notifies the delegate when the video editor is unable to load or save a movie.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UINavigationControllerDelegate & UIVideoEditorControllerDelegate)?](uivideoeditorcontroller/delegate.md)
  The video editor’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate)*