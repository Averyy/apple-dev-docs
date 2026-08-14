# Foundation Models updates

**Framework**: Updates

Learn about important changes to Foundation Models.

#### Overview

Browse notable changes in [`Foundation Models`](https://developer.apple.com/documentation/foundationmodels).

#### June 2026

##### General

- Build multimodal agentic app experiences by using the [`LanguageModelSession.DynamicProfile`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile) API.
- Use the improved error types, like [`LanguageModelError`](https://developer.apple.com/documentation/foundationmodels/languagemodelerror) for model-specific errors, [`SystemLanguageModel.Error`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/error) for on-device Apple Foundation model errors, and [`LanguageModelSession.Error`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/error) for errors related to the session but not the model.

##### Models

- Use the latest on-device [`SystemLanguageModel`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel) that follows instructions more accurately and produces better results, including in complex scenarios. Because the model changes when a person updates to iOS 27, iPadOS 27, macOS 27, and visionOS 27, test your prompts with the new model to verify your app’s behavior.
- Adopt the [`LanguageModel`](https://developer.apple.com/documentation/foundationmodels/languagemodel) protocol to use any large language model — server or on-device — with the Foundation Models framework.
- Use [`PrivateCloudComputeLanguageModel`](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel) to access more reasoning capabilities and a larger context size.
- Perform image analysis tasks by including an image in your prompt and using tools the [`Vision`](https://developer.apple.com/documentation/vision) framework provides, like [`OCRTool`](https://developer.apple.com/documentation/vision/ocrtool) and [`BarcodeReaderTool`](https://developer.apple.com/documentation/vision/barcodereadertool).

##### Tool Calling

- Control how the model interacts with tools for your request by using [`GenerationOptions.ToolCallingMode`](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct).

##### Instruments

- Use the updated [`Analyzing the runtime performance of your Foundation Models app`](https://developer.apple.com/documentation/foundationmodels/analyzing-the-runtime-performance-of-your-foundation-models-app) to get detailed insight into the complex workflows you build. The instrument provides insight into latency, prompts sent to the model, model output, tools and token usage, and so on.

##### Open Source

- Get the [`Foundation Models framework utilities`](https://developer.apple.comhttps://github.com/apple/foundation-models-utilities) to access a collection of building blocks to help you explore emerging practices in working with large language models.
- Use [`CoreAILanguageModel`](https://developer.apple.comhttps://github.com/apple/coreai-models) and [`MLXLanguageModel`](https://developer.apple.comhttps://github.com/ml-explore/mlx-swift-lm) to integrate on-device models with the Foundation Models framework.

#### March 2026

- Use the [`Foundation Models SDK for Python`](https://developer.apple.comhttps://github.com/apple/python-apple-fm-sdk) to access the on-device foundation model at the core of Apple Intelligence.

#### February 2026

- Use the latest on-device large language model that improves instruction-following and tool-calling abilities. Because the model changes when a person updates to iOS 26.4, iPadOS 26.4, macOS 26.4, and visionOS 26.4, test your prompts with the new model to verify your app’s behavior. If necessary, update and maintain prompts for each model version.
- Reduce the possibility of blocking benign content with improved guardrails for [`SystemLanguageModel`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel).
- Measure how many tokens your prompt, instructions, or entire session transcript uses with [`tokenCount(for:)`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/tokencount(for:)).
- Use the [`contextSize`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/contextsize) property to get the maximum context size — in tokens — that the [`SystemLanguageModel`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel) supports.
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