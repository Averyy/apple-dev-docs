# UIVideoEditorControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that your delegate object must implement to respond to the video editor.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
@MainActor
protocol UIVideoEditorControllerDelegate : NSObjectProtocol
```

```objc
@protocol UIVideoEditorControllerDelegate <NSObject>
```

## Overview

The methods of this protocol notify your delegate when the system has saved an edited movie or the user has canceled editing to discard any changes. There’s also a method for responding to errors encountered by the video editor.

The delegate methods are responsible for dismissing the video editor when the operation completes. To dismiss the editor, call the [`dismiss(animated:completion:)`](./uiviewcontroller/dismiss%28animated,completion%29.md) method of the parent controller responsible for displaying the video editor. The video editor is described in [`UIVideoEditorController`](./uivideoeditorcontroller.md).

## Topics

### Closing the video editor
- [func videoEditorController(UIVideoEditorController, didSaveEditedVideoToPath: String)](./uivideoeditorcontrollerdelegate/videoeditorcontroller%28_,didsaveeditedvideotopath%29.md)
  Notifies the delegate after the system finishes saving an edited movie.
- [func videoEditorControllerDidCancel(UIVideoEditorController)](./uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel%28_%29.md)
  Notifies the delegate when the user cancels a movie editing operation.
### Handling errors
- [func videoEditorController(UIVideoEditorController, didFailWithError: any Error)](./uivideoeditorcontrollerdelegate/videoeditorcontroller%28_,didfailwitherror%29.md)
  Notifies the delegate when the video editor is unable to load or save a movie.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing changes to the video
- [var delegate: (any UINavigationControllerDelegate & UIVideoEditorControllerDelegate)?](./uivideoeditorcontroller/delegate.md)
  The video editor’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate)*