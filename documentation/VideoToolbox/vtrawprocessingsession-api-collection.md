# VTRAWProcessingSession

**Framework**: Video Toolbox  
**Role**: API Collection

An object that processes frames in camera native formats such as RAW or Bayer.

## Topics

### Configuring a session
- [RAW processing parameters](./raw-processing-parameters.md)
  Parameters to set on a RAW processing session.
- [RAW Processing Properties](./raw-processing-properties.md)
  Properties that you use to configure a RAW processing session.
- [VTRAWProcessingSessionCopyProcessingParameters](./vtrawprocessingsessioncopyprocessingparameters.md)
  Copies an array of dictionaries describing the parameters provided by the RAW Processor for frame processing.
- [VTRAWProcessingSessionSetProcessingParameters](./vtrawprocessingsessionsetprocessingparameters.md)
  Sets a collection of RAW Processing parameters.
- [VTRAWProcessingSessionSetParameterChangedHandler](./vtrawprocessingsessionsetparameterchangedhandler.md)
- [VTCopyRAWProcessorExtensionProperties](./vtcopyrawprocessorextensionproperties.md)
  Returns information about the Media Extension RAW processor supporting the specified format.
### Data types
- [class VTRAWProcessingSession](./vtrawprocessingsession.md)
  An object that processes frames in camera native formats such as RAW or Bayer.
- [VTRAWProcessingParameterChangeHandler](./vtrawprocessingparameterchangehandler.md)
  A function the system calls when processing parameters change.
- [VTRAWProcessingSessionSetParameterChangedHander](./vtrawprocessingsessionsetparameterchangedhander.md)
  Provides a block which will be called when the session changes the set of processing parameters.
- [VTRAWProcessingOutputHandler](./vtrawprocessingoutputhandler.md)
  A block the system calls when frame processing is complete.
### Creating a session
- [VTRAWProcessingSessionCreate](./vtrawprocessingsessioncreate.md)
  Creates a RAW video frame processing session.
### Processing frames
- [VTRAWProcessingSessionProcessFrame](./vtrawprocessingsessionprocessframe.md)
  Submits RAW frames for format-specific processing using sequence and frame level parameters.
- [VTRAWProcessingSessionCompleteFrames](./vtrawprocessingsessioncompleteframes.md)
  Forces the RAW Processor to complete processing frames.
### Invalidating a session
- [VTRAWProcessingSessionInvalidate](./vtrawprocessingsessioninvalidate.md)
  Tears down a RAW processing session.
### Accessing the type identifier
- [VTRAWProcessingSessionGetTypeID](./vtrawprocessingsessiongettypeid.md)
  Returns the type identifier for a RAW processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession-api-collection)*