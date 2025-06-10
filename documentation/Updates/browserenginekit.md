# BrowserEngineKit updates

**Framework**: Updates

Learn about important changes in BrowserEngineKit.

#### Overview

Browse notable changes in [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit).

#### June 2025

##### Text Selection Views

Implement text selection in the [`BETextInput`](https://developer.apple.com/documentation/BrowserEngineKit/BETextInput) protocol by using a view below the text with [`selectionContainerViewBelowText`](https://developer.apple.com/documentation/BrowserEngineKit/BETextInput/selectionContainerViewBelowText) or a view above the text with [`selectionContainerViewAboveText`](https://developer.apple.com/documentation/BrowserEngineKit/BETextInput/selectionContainerViewAboveText). As optional properties, you can leave the views unspecified and implement text selection using a subview of [`textInputView`](https://developer.apple.com/documentation/BrowserEngineKit/BETextInput/textInputView).

##### Extension Management

Create XPC connections for an extension process with the [`BEExtensionProcess`](https://developer.apple.com/documentation/BrowserEngineKit/BEExtensionProcess) protocol [`makeLibXPCConnectionError()`](https://developer.apple.com/documentation/BrowserEngineKit/BEExtensionProcess/makeLibXPCConnectionError()) method. Stop an extension process with [`invalidate()`](https://developer.apple.com/documentation/BrowserEngineKit/BEExtensionProcess/invalidate()).

##### Interprocess Rendering

Render over raw mach messaging using the [`LayerHierarchyHandle`](https://developer.apple.com/documentation/BrowserEngineKit/LayerHierarchyHandle) methods, [`init(port:data:)`](https://developer.apple.com/documentation/BrowserEngineKit/LayerHierarchyHandle/init(port:data:)) and [`encode(_:)`](https://developer.apple.com/documentation/BrowserEngineKit/LayerHierarchyHandle/encode(_:)). Similarly for [`LayerHierarchyHostingTransactionCoordinator`](https://developer.apple.com/documentation/BrowserEngineKit/LayerHierarchyHostingTransactionCoordinator), use the methods, [`init(port:data:)`](https://developer.apple.com/documentation/BrowserEngineKit/LayerHierarchyHostingTransactionCoordinator/init(port:data:)) and [`encode(_:)`](https://developer.apple.com/documentation/BrowserEngineKit/LayerHierarchyHostingTransactionCoordinator/encode(_:)).

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
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/browserenginekit)*