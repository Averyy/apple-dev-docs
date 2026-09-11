# VideoDriverKit

**Framework**: VideoDriverKit  
**Kind**: namespace

A namespace that holds supporting types used by VideoDriverKit functions.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
namespace VideoDriverKit;
```

## Topics

### Working with class identifiers
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Working with object identifiers
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
  A handle for a a specific video object.
- [kIOUserVideoObjectIDDriver](videodriverkit/kiouservideoobjectiddriver.md)
  The video object identifier of the driver.
### Working with object properties
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyElementMain](videodriverkit/iouservideoobjectpropertyelementmain.md)
  The value for properties that apply to the main element or to the entire scope.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
- [IOUserVideoObjectPropertySelector](videodriverkit/iouservideoobjectpropertyselector.md)
  A four character code which, along with the scope and element, specifies a specific piece of information about a video object.
### Working with video streams
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [IOUserVideoFormatID](videodriverkit/iouservideoformatid.md)
  Identifiers used for formats of audio data.
- [IOUserVideoFormatFlags](videodriverkit/iouservideoformatflags.md)
  Standard format flags for a basic description.
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
  The direction of a video stream.
- [IOUserVideoStreamTerminalType](videodriverkit/iouservideostreamterminaltype.md)
  The terminal type of video stream.
### Working with I/O operations
- [IOUserVideoIOOperation](videodriverkit/iouservideoiooperation.md)
  The IO operation being called on the operation handler block.
- [IOUserVideoIOOperationBeginRead](videodriverkit/iouservideoiooperationbeginread.md)
  This operation is called just prior to reading data from the device’s stream buffers.
- [IOUserVideoIOOperationWriteEnd](videodriverkit/iouservideoiooperationwriteend.md)
  This operation is called just after writing data to the device’s stream buffers.
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform an IOUserVideoIOOperation.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
### Working with custom properties
- [IOUserVideoCustomPropertyInfo](videodriverkit/iouservideocustompropertyinfo.md)
  A description of a a custom property that allow the Host to marshal the data between the Host and its clients.
- [IOUserVideoObjectPropertyAddress](videodriverkit/iouservideoobjectpropertyaddress.md)
  A data structure that contains all the three parts to identify a specific property, for easy transmission.
- [IOUserVideoCustomPropertyDataType](videodriverkit/iouservideocustompropertydatatype.md)
  Data qualifier types used for custom properties.
### Working with clock device behavior
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
### Working with channel layouts
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.
### Working with transport types
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
  The transport type of a video stream.
### Working with transport states
- [IOUserVideoDeviceTransportState](videodriverkit/iouservideodevicetransportstate.md)
  The current transport state of the device.
### Working with configuration changes
- [IOUserVideoReservedConfigChangeAction](videodriverkit/iouservideoreservedconfigchangeaction.md)
  Reserved configuration change identifiers when changing object state that requires a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit)*