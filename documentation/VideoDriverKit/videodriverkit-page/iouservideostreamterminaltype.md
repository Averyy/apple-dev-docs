# IOUserVideoStreamTerminalType

**Framework**: VideoDriverKit  
**Kind**: enum  
**Role**: Enumeration

The terminal type of video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
enum IOUserVideoStreamTerminalType : uint32_t;
```

## Topics

### Terminal types
- [Line](./iouservideostreamterminaltype/line.md)
  The identifier for a terminal type of a line level stream.
- [DigitalVideoInterface](./iouservideostreamterminaltype/digitalvideointerface.md)
  The ID for a terminal type of stream from/to a digital audio interface as defined by ISO 60958 (aka SPDIF or AES/EBU).
- [Speaker](./iouservideostreamterminaltype/speaker.md)
  The identifier for a terminal type of a speaker.
- [Headphones](./iouservideostreamterminaltype/headphones.md)
  The identifier for a terminal type of headphones.
- [LFESpeaker](./iouservideostreamterminaltype/lfespeaker.md)
  The identifier for a terminal type of a speaker for low frequency effects.
- [ReceiverSpeaker](./iouservideostreamterminaltype/receiverspeaker.md)
  The identifier for a terminal type of a speaker on a telephone handset receiver.
- [Microphone](./iouservideostreamterminaltype/microphone.md)
  The identifier for a terminal type of a microphone.
- [HeadsetMicrophone](./iouservideostreamterminaltype/headsetmicrophone.md)
  The identifier for a terminal type of a microphone attached to an headset.
- [ReceiverMicrophone](./iouservideostreamterminaltype/receivermicrophone.md)
  The identifier for a terminal type of a microphone on a telephone handset receiver.
- [TTY](./iouservideostreamterminaltype/tty.md)
  The identifier for a terminal type of a device providing a TTY signal.
- [HDMI](./iouservideostreamterminaltype/hdmi.md)
  The identifier for a terminal type of a stream from/to an HDMI port.
- [DisplayPort](./iouservideostreamterminaltype/displayport.md)
  The identifier for a terminal type of a stream from/to an DisplayPort port.
- [Unknown](./iouservideostreamterminaltype/unknown.md)
  The identifier used when the terminal type for the stream is not known.

## See Also

### Working with stream terminals
- [SetTerminalType](../iouservideostream/setterminaltype.md)
  Sets the terminal type of the stream.
- [GetTerminalType](../iouservideostream/getterminaltype.md)
  Gets the terminal type of the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideostreamterminaltype)*