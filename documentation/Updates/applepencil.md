# Apple Pencil updates

**Framework**: Updates

Learn about important changes to Apple Pencil.

#### Overview

Browse notable changes in [`Apple Pencil`](https://developer.apple.com/documentation/applepencil).

#### June 2024

##### Uikit

- Implement custom low-latency drawing if your app doesn’t use PencilKit. Participate in UI updates and influence UI update behavior using [`UIUpdateLink`](https://developer.apple.com/documentation/uikit/uiupdatelink).

##### Pencilkit

- Offer a wider variety of marking tools by creating a configurable tool picker. Create a [`PKToolPicker`](https://developer.apple.com/documentation/pencilkit/pktoolpicker), add standard system tools or define your own custom tools with [`PKToolPickerCustomItem`](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitem), and specify which order the tools appear in. Include an optional [`accessoryItem`](https://developer.apple.com/documentation/pencilkit/pktoolpicker/accessoryitem) in the tool picker to provide quick access to additional features directly from the picker.

#### May 2024

##### Swiftui and Uikit

- Perform actions in your app in response to squeeze interactions on Apple Pencil Pro. People can choose their preferred squeeze action in Settings > Apple Pencil > Actions > Squeeze, such as switching drawing tools, showing a contextual palette, or performing an App Shortcut. You can also implement a custom action for squeeze and give people the choice to use your app’s custom behavior instead. In SwiftUI, use [`onPencilSqueeze(perform:)`](https://developer.apple.com/documentation/swiftui/view/onpencilsqueeze(perform:)). In UIKit, use [`pencilInteraction(_:didReceiveSqueeze:)`](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate/pencilinteraction(_:didreceivesqueeze:)).
- Perform actions in your app in response to double-tap interactions on Apple Pencil. People can choose their preferred double-tap action in Settings > Apple Pencil > Actions > Double Tap. In SwiftUI, use [`onPencilDoubleTap(perform:)`](https://developer.apple.com/documentation/swiftui/view/onpencildoubletap(perform:)). In UIKit, update your implementation to use [`pencilInteraction(_:didReceiveTap:)`](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate/pencilinteraction(_:didreceivetap:)), which replaces the deprecated [`pencilInteractionDidTap(_:)`](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate/pencilinteractiondidtap(_:)).
- Leverage the hover pose of Apple Pencil to support more complex interactions in response to a double tap or squeeze. Information about the hover pose — such as azimuth, altitude, and hover distance — is available when a person holds a supported model of Apple Pencil close to the screen during a double tap or squeeze. In SwiftUI, use [`PencilHoverPose`](https://developer.apple.com/documentation/swiftui/pencilhoverpose). In UIKit, use [`UIPencilHoverPose`](https://developer.apple.com/documentation/uikit/uipencilhoverpose).
- Provide tactile feedback on Apple Pencil Pro by playing haptics in response to certain actions, such as snapping objects to a grid. In SwiftUI, use [`SensoryFeedback`](https://developer.apple.com/documentation/swiftui/sensoryfeedback). In UIKit, use [`UIFeedbackGenerator`](https://developer.apple.com/documentation/uikit/uifeedbackgenerator).
- Track the barrel-roll angle of Apple Pencil Pro to create more expressive drawing experiences and hover previews using [`rollAngle`](https://developer.apple.com/documentation/uikit/uitouch/rollangle).

- Check the value of the hover tool preview preference from the Apple Pencil section of the Settings app using [`prefersHoverToolPreview`](https://developer.apple.com/documentation/uikit/uipencilinteraction/prefershovertoolpreview).

##### Pencilkit

- Take advantage of barrel-roll tracking for Apple Pencil Pro when a person makes marker and fountain pen strokes. Support [`PKContentVersion.version3`](https://developer.apple.com/documentation/pencilkit/pkcontentversion/version3), which includes the version of the inks that incorporate barrel-roll data.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Background Tasks updates](backgroundtasks.md)
  Learn about important changes in Background Tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/applepencil)*