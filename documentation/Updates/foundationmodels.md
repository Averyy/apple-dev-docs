# Foundation Models updates

**Framework**: Updates

Learn about important changes to Foundation Models.

#### Overview

Browse notable changes in [`Foundation Models`](https://developer.apple.com/documentation/FoundationModels).

#### February 2026

- Use the latest on-device large language model that improves instruction-following and tool-calling abilities. Because the model changes when a person updates to iOS 26.4, iPadOS 26.4, macOS 26.4, and visionOS 26.4, test your prompts with the new model to verify your app’s behavior. If necessary, update and maintain prompts for each model version.
- Reduce the possibility of blocking benign content with improved guardrails for [`SystemLanguageModel`](https://developer.apple.com/documentation/FoundationModels/SystemLanguageModel).
- Measure how many tokens your prompt, instructions, or entire session transcript uses with [`tokenCount(for:)`](https://developer.apple.com/documentation/FoundationModels/SystemLanguageModel/tokenCount(for:)).
- Use the [`contextSize`](https://developer.apple.com/documentation/FoundationModels/SystemLanguageModel/contextSize) property to get the maximum context size — in tokens — that the [`SystemLanguageModel`](https://developer.apple.com/documentation/FoundationModels/SystemLanguageModel) supports.
- Use the `#Playground` macro in Xcode to view an estimate of the usage of 4,096 tokens in the available context window. When you run the canvas, the output displays Input Token Count and Response Token Count separately.

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/foundationmodels)*