# VTMotionEstimationSession

**Framework**: Video Toolbox  
**Role**: API Collection

## Topics

### Creating a session
- [class VTMotionEstimationSession](./vtmotionestimationsession.md)
- [let kVTMotionEstimationSessionCreationOption_Label: CFString!](./kvtmotionestimationsessioncreationoption_label.md)
  A label you use to log and track resources.
- [let kVTMotionEstimationSessionCreationOption_MotionVectorSize: CFString!](./kvtmotionestimationsessioncreationoption_motionvectorsize.md)
  The size of the search blocks that motion estimation session uses.
- [let kVTMotionEstimationSessionCreationOption_UseMultiPassSearch: CFString!](./kvtmotionestimationsessioncreationoption_usemultipasssearch.md)
  An option to use for higher quality motion estimation.
- [VTMotionEstimationSessionCreate](./vtmotionestimationsessioncreate.md)
  Creates a session you use to generate a pixel buffer of motion vectors from two pixel buffers.
- [kVTMotionEstimationSessionCreationOption_DetectTrueMotion](./kvtmotionestimationsessioncreationoption_detecttruemotion.md)
  Enable multi pass true motion detection.
### Handling output
- [typealias VTMotionEstimationOutputHandler](./vtmotionestimationoutputhandler.md)
  A block invoked by motion-estimation session when frame processing is complete.
- [VTMotionEstimationSessionCompleteFrames](./vtmotionestimationsessioncompleteframes.md)
  Directs the motion-estimation session to emit all pending frames and waits for completion.
- [VTMotionEstimationSessionCopySourcePixelBufferAttributes](./vtmotionestimationsessioncopysourcepixelbufferattributes.md)
  Copies the attributes for source pixel buffers expected by motion-estimation session.
- [VTMotionEstimationSessionEstimateMotionVectors](./vtmotionestimationsessionestimatemotionvectors.md)
  Creates a new pixel buffer that contains motion vectors between the input pixel buffers.
### Invalidating a session
- [VTMotionEstimationSessionInvalidate](./vtmotionestimationsessioninvalidate.md)
  Tears down a motion-estimation session.
### Accessing the type identifier
- [VTMotionEstimationSessionGetTypeID](./vtmotionestimationsessiongettypeid.md)
  Get the CoreFoundation type identifier for motion-estimation session type.
### Data types
- [VTMotionEstimationSessionRef](./vtmotionestimationsessionref.md)
  A reference to a Video Toolbox motion-estimation session.
- [VTMotionEstimationFrameFlags](./vtmotionestimationframeflags.md)
  Flags to control processing of a frame you pass to the motion-estimation session.
- [VTMotionEstimationInfoFlags](./vtmotionestimationinfoflags.md)
  Directives that provide information back to you with the results of motion-estimation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsession-api-collection)*