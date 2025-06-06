# Writing Tools

**Framework**: UIKit

Add support for Writing Tools to your app’s text views.

#### Overview

Writing Tools provides a simple way for people to improve what they write using your app. Text views that support Writing Tools gain the ability to proofread, rewrite, summarize, or compose content with the help of system-provided large language models (LLMs) and Apple Intelligence.

Writing Tools supports both the standard system views and custom text views you create. The [`UITextView`](uitextview.md) and [`UITextField`](uitextfield.md) classes automatically support Writing Tools, but you can customize that support to suit your app’s requirements. You can also add Writing Tools support to any [`UIView`](uiview.md) in your app that contains text.

## Topics

### Configuration
- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md)
  Modify the behavior of Writing Tools in standard iOS text views, and adjust your app’s behavior while the feature is active.
- [enum UIWritingToolsBehavior](uiwritingtoolsbehavior.md)
  Constants that specify the writing tools experience for the underlying view.
- [struct UIWritingToolsResultOptions](uiwritingtoolsresultoptions.md)
  Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.
### Writing Tools for custom views
- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)
  Add Writing Tools support, including support for inline replacement animations, to your custom iOS views that contain text.
- [class UIWritingToolsCoordinator](uiwritingtoolscoordinator.md)
  An object that manages interactions between Writing Tools and your custom text view.
- [UIWritingToolsCoordinator.Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.
- [UIWritingToolsCoordinator.Context](uiwritingtoolscoordinator/context.md)
  A data object that you use to share your custom view’s text with Writing Tools.
- [UIWritingToolsCoordinator.AnimationParameters](uiwritingtoolscoordinator/animationparameters.md)
  An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.
### Text previews
- [class UITargetedPreview](uitargetedpreview.md)
  An object describing the view to use during preview-related animations.
- [class UIPreviewParameters](uipreviewparameters.md)
  Additional parameters to use when animating a preview interface.
- [class UIPreviewTarget](uipreviewtarget.md)
  An object that specifies the container view to use for animations.

## See Also

- [Text display and fonts](text-display-and-fonts.md)
  Display text, manage fonts, and check spelling.
- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Keyboards and input](keyboards-and-input.md)
  Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.
- [Handwriting recognition](handwriting-recognition.md)
  Configure text fields and custom views that accept text to handle input from Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/writing-tools)*