# IOUserVideoStreamTerminalType

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoStreamTerminalType : uint32_t;
```

#### Overview

Various constants that describe the terminal type of an IOUserVideoStream.

The ID used when the terminal type for the IOUserVideoStream is not known.

The ID for a terminal type of a line level stream. Note that this applies to both input streams and output streams

The ID for a terminal type of stream from/to a digital audio interface as defined by ISO 60958 (aka SPDIF or AES/EBU). Note that this applies to both input streams and output streams

The ID for a terminal type of a speaker.

The ID for a terminal type of headphones.

The ID for a terminal type of a speaker for low frequency effects.

The ID for a terminal type of a speaker on a telephone handset receiver.

The ID for a terminal type of a microphone.

The ID for a terminal type of a microphone attached to an headset.

The ID for a terminal type of a microphone on a telephone handset receiver.

The ID for a terminal type of a device providing a TTY signal.

The ID for a terminal type of a stream from/to an HDMI port.

The ID for a terminal type of a stream from/to an DisplayPort port.

## Topics

### Terminal types
- [Line](videodriverkit/iouservideostreamterminaltype/line.md)
- [DigitalVideoInterface](videodriverkit/iouservideostreamterminaltype/digitalvideointerface.md)
- [Speaker](videodriverkit/iouservideostreamterminaltype/speaker.md)
- [Headphones](videodriverkit/iouservideostreamterminaltype/headphones.md)
- [LFESpeaker](videodriverkit/iouservideostreamterminaltype/lfespeaker.md)
- [ReceiverSpeaker](videodriverkit/iouservideostreamterminaltype/receiverspeaker.md)
- [Microphone](videodriverkit/iouservideostreamterminaltype/microphone.md)
- [HeadsetMicrophone](videodriverkit/iouservideostreamterminaltype/headsetmicrophone.md)
- [ReceiverMicrophone](videodriverkit/iouservideostreamterminaltype/receivermicrophone.md)
- [TTY](videodriverkit/iouservideostreamterminaltype/tty.md)
- [HDMI](videodriverkit/iouservideostreamterminaltype/hdmi.md)
- [DisplayPort](videodriverkit/iouservideostreamterminaltype/displayport.md)
- [Unknown](videodriverkit/iouservideostreamterminaltype/unknown.md)

## See Also

- [SetTerminalType](iouservideostream/setterminaltype.md)
- [GetTerminalType](iouservideostream/getterminaltype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideostreamterminaltype)*