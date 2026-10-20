# Apple Pencil updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to Apple Pencil.

#### Overview

Browse notable changes in [Apple Pencil](../ApplePencil/ApplePencil.md).

#### June 2024

##### UIKit

- Implement custom low-latency drawing if your app doesn’t use PencilKit. Participate in UI updates and influence UI update behavior using [`UIUpdateLink`](../UIKit/uiupdatelink.md).

##### PencilKit

- Offer a wider variety of marking tools by creating a configurable tool picker. Create a [`PKToolPicker`](../PencilKit/pktoolpicker.md), add standard system tools or define your own custom tools with [`PKToolPickerCustomItem`](../PencilKit/pktoolpickercustomitem.md), and specify which order the tools appear in. Include an optional [`accessoryItem`](../PencilKit/pktoolpicker/accessoryitem.md) in the tool picker to provide quick access to additional features directly from the picker.

#### May 2024

##### SwiftUI and UIKit

- Perform actions in your app in response to squeeze interactions on Apple Pencil Pro. People can choose their preferred squeeze action in Settings > Apple Pencil > Actions > Squeeze, such as switching drawing tools, showing a contextual palette, or performing an App Shortcut. You can also implement a custom action for squeeze and give people the choice to use your app’s custom behavior instead. In SwiftUI, use [`onPencilSqueeze(perform:)`](../SwiftUI/view/onpencilsqueeze%28perform%29.md). In UIKit, use [`pencilInteraction(_:didReceiveSqueeze:)`](../UIKit/uipencilinteractiondelegate/pencilinteraction%28_,didreceivesqueeze%29.md).
- Perform actions in your app in response to double-tap interactions on Apple Pencil. People can choose their preferred double-tap action in Settings > Apple Pencil > Actions > Double Tap. In SwiftUI, use [`onPencilDoubleTap(perform:)`](../SwiftUI/view/onpencildoubletap%28perform%29.md). In UIKit, update your implementation to use [`pencilInteraction(_:didReceiveTap:)`](../UIKit/uipencilinteractiondelegate/pencilinteraction%28_,didreceivetap%29.md), which replaces the deprecated [`pencilInteractionDidTap(_:)`](../UIKit/uipencilinteractiondelegate/pencilinteractiondidtap%28_%29.md).
- Leverage the hover pose of Apple Pencil to support more complex interactions in response to a double tap or squeeze. Information about the hover pose — such as azimuth, altitude, and hover distance — is available when a person holds a supported model of Apple Pencil close to the screen during a double tap or squeeze. In SwiftUI, use [`PencilHoverPose`](../SwiftUI/pencilhoverpose.md). In UIKit, use [`UIPencilHoverPose`](../UIKit/uipencilhoverpose.md).
- Provide tactile feedback on Apple Pencil Pro by playing haptics in response to certain actions, such as snapping objects to a grid. In SwiftUI, use [`SensoryFeedback`](../SwiftUI/sensoryfeedback.md). In UIKit, use [`UIFeedbackGenerator`](../UIKit/uifeedbackgenerator.md).
- Track the barrel-roll angle of Apple Pencil Pro to create more expressive drawing experiences and hover previews using [`rollAngle`](../UIKit/uitouch/rollangle.md).

- Check the value of the hover tool preview preference from the Apple Pencil section of the Settings app using [`prefersHoverToolPreview`](../UIKit/uipencilinteraction/prefershovertoolpreview.md).

##### PencilKit

- Take advantage of barrel-roll tracking for Apple Pencil Pro when a person makes marker and fountain pen strokes. Support [`PKContentVersion.version3`](../PencilKit/pkcontentversion/version3.md), which includes the version of the inks that incorporate barrel-roll data.

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.
- [AVKit updates](./avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/applepencil)*