# IOUserVideoStreamBasicDescription

**Framework**: VideoDriverKit  
**Kind**: struct

A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
struct IOUserVideoStreamBasicDescription;
```

#### Overview

This structure is sufficient to describe any constant bit rate format that has channels that are the same size. Extensions are required for variable bit rate data and for constant bit rate data where the channels have unequal sizes. However, where applicable, the appropriate fields will be filled out correctly for these kinds of formats (the extra data is provided via separate properties). In all fields, a value of 0 indicates that the field is either unknown, not applicable or otherwise is inappropriate for the format and should be ignored. Note that 0 is still a valid value for most formats in the `mFormatFlags` field.

In audio data a frame is one sample across all channels. In non-interleaved audio, the per frame fields identify one channel. In interleaved audio, the per frame fields identify the set of n channels. In uncompressed audio, a Packet is one frame, (`mFramesPerPacket == 1`). In compressed audio, a Packet is an indivisible chunk of compressed data, for example an AAC packet will contain 1024 sample frames.

## Topics

### Accessing the frame rate
- [mFrameRate](videodriverkit/iouservideostreambasicdescription/mframerate.md)
### Identifying the codec
- [mVideoCodecType](videodriverkit/iouservideostreambasicdescription/mvideocodectype.md)
- [IOUserVideoFormatID](videodriverkit/iouservideoformatid.md)
  Identifiers used for formats of audio data.
- [mVideoCodecFlags](videodriverkit/iouservideostreambasicdescription/mvideocodecflags.md)
- [IOUserVideoFormatFlags](videodriverkit/iouservideoformatflags.md)
  Standard format flags for a basic description.
### Accessing spatial properties
- [mWidth](videodriverkit/iouservideostreambasicdescription/mwidth.md)
- [mHeight](videodriverkit/iouservideostreambasicdescription/mheight.md)
### Accessing timing properties
- [mFrameTimeScale](videodriverkit/iouservideostreambasicdescription/mframetimescale.md)
- [mFrameTimeValue](videodriverkit/iouservideostreambasicdescription/mframetimevalue.md)
### Accessing reserved properties
- [mReserved1](videodriverkit/iouservideostreambasicdescription/mreserved1.md)
- [mReserved2](videodriverkit/iouservideostreambasicdescription/mreserved2.md)

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
  Sets the current stream format.
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
  Gets the current basic description of the stream.
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
  Sets the available descriptions for the stream.
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
  Gets the available basic descriptions for the stream.
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
  Gets the number of available description for the stream.
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
  Gets the direction of the stream.
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
  The direction of a video stream.
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
  Sets whether that the stream is active and doing IO.
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)
  Gets the stream activity state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideostreambasicdescription)*