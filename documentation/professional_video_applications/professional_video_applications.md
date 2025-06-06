# Professional Video Applications

**Framework**: Professional Video Applications  
**Kind**: module

Exchange data with Final Cut Pro, and create effects plug-ins for Final Cut Pro and Motion.

#### Overview

Final Cut Pro XML (FCPXML) offers a way for video producers to streamline the exchange of media and metadata between apps and Final Cut Pro. Use FCPXML to send media and metadata from your app to Final Cut Pro for editing, and receive rendered projects—along with their edit descriptions and metadata—from Final Cut Pro into your app.

You can choose to build a workflow extension for your app and integrate the app’s workflow within the Final Cut Pro interface. Workflow extensions provide a seamless experience by allowing users to access your app’s workflow without leaving the Final Cut Pro interface.

The FxPlug SDK provides a complete API for creating custom effects plug-ins. Your plug-ins are fully integrated with Final Cut Pro and Motion so video editors can easily add them in post-production.

The Compressor Extension SDK comes with APIs that allow you to add output file formats that the Compressor app does not provide by default. Use the SDK to integrate your custom output formats into the Compressor app settings and allow users to export their Final Cut Pro projects to your custom file formats.

For information about Final Cut Pro concepts, see [`What are libraries`](https://developer.apple.comhttps://support.apple.com/guide/final-cut-pro/what-are-libraries-verfdd5c590e/mac) and [`Intro to metadata in Final Cut Pro`](https://developer.apple.comhttps://support.apple.com/guide/final-cut-pro/intro-to-metadata-verc392f8885/mac).

## Topics

### Effects
- [FxPlug](../professional-video-applications/fxplug.md)
  Create custom effects plug-ins for Final Cut Pro and Motion.
- [Create an effect template for use in Final Cut Pro](../professional-video-applications/create-an-effect-template-for-use-in-final-cut-pro.md)
  Use Motion to create custom filters, generators, and transitions for Final Cut Pro.
### XML Data Exchange
- [Content and Metadata Exchanges with Final Cut Pro](../professional-video-applications/content-and-metadata-exchanges-with-final-cut-pro.md)
  Send media assets and timeline sequences to Final Cut Pro for editing, and receive rendered media and editing decisions in your app.
- [Workflow Extensions](../professional-video-applications/workflow-extensions.md)
  Integrate your app’s workflow within the Final Cut Pro interface to streamline data exchange.
- [FCPXML Reference](../professional-video-applications/fcpxml-reference.md)
  Create documents that describe the data your app or workflow extension exchanges with Final Cut Pro.
### Compressor Encoder Extensions
- [Encoder Extensions](../professional-video-applications/encoder-extensions.md)
  Add custom output file formats to the Final Cut Pro workflow.
### Reference
- [Professional Video Applications Enumerations](../professional-video-applications/professional-video-applications-enumerations.md)
- [Professional Video Applications Constants](../professional-video-applications/professional-video-applications-constants.md)
- [Professional Video Applications Data Types](../professional-video-applications/professional-video-applications-data-types.md)
- [Professional Video Applications Protocols](../professional-video-applications/professional-video-applications-protocols.md)
### Variables
- [var kFxPropertyKey_ChangesOutputSize: String](kfxpropertykey_changesoutputsize.md)
  A key that determines whether your filter has the ability to change the size of its output to be different than the size of its input.
- [var kFxPropertyKey_DesiredProcessingColorInfo: String](kfxpropertykey_desiredprocessingcolorinfo.md)
  A key that determines whether your plug-in renders in linear or gamma-corrected color space.
- [var kFxPropertyKey_NeedsFullBuffer: String](kfxpropertykey_needsfullbuffer.md)
  A key that determines whether the plug-in needs the entire image to do its processing, and can’t tile its rendering.
- [var kFxPropertyKey_VariesWhenParamsAreStatic: String](kfxpropertykey_varieswhenparamsarestatic.md)
  A key that determines whether your rendering varies even when the parameters remain the same.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications)*