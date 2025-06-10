# UIVideoEditorController

**Framework**: UIKit  
**Kind**: class

A view controller that manages the system interface for trimming video frames and encoding a previously recorded movie.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIVideoEditorController
```

#### Overview

A video editor manages user interactions and provides the filesystem path of the edited movie to your delegate object (see [`UIVideoEditorControllerDelegate`](uivideoeditorcontrollerdelegate.md)). The features of the [`UIVideoEditorController`](uivideoeditorcontroller.md) class are available only on devices that support video recording. Use a video editor when your intent is to provide an interface for movie editing. While the [`UIImagePickerController`](uiimagepickercontroller.md) class also lets a user trim movies, its primary roles are choosing saved pictures and movies, and capturing new pictures and movies.

> ❗ **Important**:  The `UIVideoEditorController` class supports portrait mode only. This class is intended to be used as-is and doesn’t support subclassing. The view hierarchy for this class is private; don’t modify the view hierarchy. This class doesn’t support modifications to its appearance by use of overlay views.

## Topics

### Managing changes to the video
- [var delegate: (any UINavigationControllerDelegate & UIVideoEditorControllerDelegate)?](uivideoeditorcontroller/delegate.md)
  The video editor’s delegate object.
- [protocol UIVideoEditorControllerDelegate](uivideoeditorcontrollerdelegate.md)
  A set of methods that your delegate object must implement to respond to the video editor.
### Determining editing availability
- [class func canEditVideo(atPath: String) -> Bool](uivideoeditorcontroller/caneditvideo(atpath:).md)
  Returns a Boolean value indicating whether a video file can be edited.
### Configuring the editor
- [var videoMaximumDuration: TimeInterval](uivideoeditorcontroller/videomaximumduration.md)
  The maximum duration, in seconds, permitted for trimmed movies saved by the video editor.
- [var videoPath: String](uivideoeditorcontroller/videopath.md)
  The filesystem path to the movie to be loaded by the video editor.
- [var videoQuality: UIImagePickerController.QualityType](uivideoeditorcontroller/videoquality.md)
  The video quality to use when saving a trimmed movie.

## Relationships

### Inherits From
- [UINavigationController](uinavigationcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIImagePickerController](uiimagepickercontroller.md)
  A view controller that manages the system interfaces for taking pictures, recording movies, and choosing items from the user’s media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller)*