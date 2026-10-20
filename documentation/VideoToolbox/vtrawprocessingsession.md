# VTRAWProcessingSession

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

An object that processes frames in camera native formats such as RAW or Bayer.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VTRAWProcessingSession
```

```c
typedef struct OpaqueVTRAWProcessingSession * VTRAWProcessingSessionRef;
```

#### Overview

A RAW processing session supports processing of frames that have been output from decoders in camera native formats, such as RAW or Bayer formats.

The session reference is a reference-counted CF object.

## Topics

### Configuring parameters
- [func parameters() -> any AsyncSequence<[VTRAWProcessingSession.Parameter], Never>](./vtrawprocessingsession/parameters%28%29.md)
  Returns an asynchronous sequence that provides updates to the processing Parameter array if the processing extension makes changes to the set of Parameters.
- [func updateParameter(values: [String : Any]) throws](./vtrawprocessingsession/updateparameter%28values%29.md)
  Sets the value for one or more of the processing parameters.
- [var processingParameters: [VTRAWProcessingSession.Parameter]](./vtrawprocessingsession/processingparameters.md)
  An array of processing parameters available for this RAW processing session.
- [VTRAWProcessingSession.Parameter](./vtrawprocessingsession/parameter.md)
  A parameter expresses a control or a set of controls that influence frame processing.
### Processing frames
- [func process(frame: CVPixelBuffer) async throws -> CVPixelBuffer](./vtrawprocessingsession/process%28frame%29.md)
  Processes an input pixel buffer.
### Configuring the Metal device
- [var metalDevice: (any MTLDevice)?](./vtrawprocessingsession/metaldevice.md)
  The preferred device to use for any Metal-based processing performed by the RAW Processing Extension.
### Initializers
- [init(referencing: VTRAWProcessingSession)](./vtrawprocessingsession/init%28referencing%29.md)
### Type Aliases
- [VTRAWProcessingSession.T](./vtrawprocessingsession/t.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession)*