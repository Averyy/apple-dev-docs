# VideoDriverKit

**Framework**: VideoDriverKit  
**Kind**: namespace  
**Role**: Namespace

A namespace that holds supporting types used by VideoDriverKit functions.

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
namespace VideoDriverKit;
```

## Topics

### Working with class identifiers
- [IOUserVideoClassID](./videodriverkit-page/iouservideoclassid.md)
  Video class identifiers of an video object.
### Working with object identifiers
- [IOUserVideoObjectID](./videodriverkit-page/iouservideoobjectid.md)
  A handle for a a specific video object.
- [kIOUserVideoObjectIDDriver](./videodriverkit-page/kiouservideoobjectiddriver.md)
  The video object identifier of the driver.
### Working with object properties
- [IOUserVideoObjectPropertyElement](./videodriverkit-page/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyElementMain](./videodriverkit-page/iouservideoobjectpropertyelementmain.md)
  The value for properties that apply to the main element or to the entire scope.
- [IOUserVideoObjectPropertyScope](./videodriverkit-page/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
- [IOUserVideoObjectPropertySelector](./videodriverkit-page/iouservideoobjectpropertyselector.md)
  A four character code which, along with the scope and element, specifies a specific piece of information about a video object.
### Working with video streams
- [IOUserVideoStreamBasicDescription](./videodriverkit-page/iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [IOUserVideoFormatID](./videodriverkit-page/iouservideoformatid.md)
  Identifiers used for formats of audio data.
- [IOUserVideoFormatFlags](./videodriverkit-page/iouservideoformatflags.md)
  Standard format flags for a basic description.
- [IOUserVideoStreamDirection](./videodriverkit-page/iouservideostreamdirection.md)
  The direction of a video stream.
- [IOUserVideoStreamTerminalType](./videodriverkit-page/iouservideostreamterminaltype.md)
  The terminal type of video stream.
### Working with I/O operations
- [IOUserVideoIOOperation](./videodriverkit-page/iouservideoiooperation.md)
  The IO operation being called on the operation handler block.
- [IOUserVideoIOOperationBeginRead](./videodriverkit-page/iouservideoiooperationbeginread.md)
  This operation is called just prior to reading data from the device’s stream buffers.
- [IOUserVideoIOOperationWriteEnd](./videodriverkit-page/iouservideoiooperationwriteend.md)
  This operation is called just after writing data to the device’s stream buffers.
- [IOOperationHandler](./videodriverkit-page/iooperationhandler.md)
  A block that tells the device to perform a video IO operation.
- [IOUserVideoStartStopFlags](./videodriverkit-page/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
### Working with custom properties
- [IOUserVideoCustomPropertyInfo](./videodriverkit-page/iouservideocustompropertyinfo.md)
  A description of a a custom property that allow the Host to marshal the data between the Host and its clients.
- [IOUserVideoObjectPropertyAddress](./videodriverkit-page/iouservideoobjectpropertyaddress.md)
  A data structure that contains all the three parts to identify a specific property, for easy transmission.
- [IOUserVideoCustomPropertyDataType](./videodriverkit-page/iouservideocustompropertydatatype.md)
  Data qualifier types used for custom properties.
### Working with clock device behavior
- [IOUserVideoClockAlgorithm](./videodriverkit-page/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
### Working with channel layouts
- [IOUserVideoChannelLabel](./videodriverkit-page/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.
### Working with transport types
- [IOUserVideoTransportType](./videodriverkit-page/iouservideotransporttype.md)
  The transport type of a video stream.
### Working with transport states
- [IOUserVideoDeviceTransportState](./videodriverkit-page/iouservideodevicetransportstate.md)
  The current transport state of the device.
### Working with configuration changes
- [IOUserVideoReservedConfigChangeAction](./videodriverkit-page/iouservideoreservedconfigchangeaction.md)
  Reserved configuration change identifiers when changing object state that requires a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit)*