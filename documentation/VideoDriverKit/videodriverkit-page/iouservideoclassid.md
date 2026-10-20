# IOUserVideoClassID

**Framework**: VideoDriverKit  
**Kind**: enum  
**Role**: Enumeration

Video class identifiers of an video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
enum IOUserVideoClassID : uint32_t;
```

## Topics

### Identifying VideoDriverKit types
- [Object](./iouservideoclassid/object.md)
  The class identifier for the `IOUserVideoObject` class.
- [Driver](./iouservideoclassid/driver.md)
  The class identifier for the `IOUserVideoDriver` class.
- [Box](./iouservideoclassid/box.md)
  The class identifier for the `IOUserVideoBox` class.
- [Clock](./iouservideoclassid/clock.md)
  The class identifier for the `IOUserVideoClockDevice` class.
- [Buffer](./iouservideoclassid/buffer.md)
  The class identifier for the `IOUserVideoBuffer` class.
- [Device](./iouservideoclassid/device.md)
  The class identifier for the `IOUserVideoDevice` class.
- [Stream](./iouservideoclassid/stream.md)
  The class identifier for the `IOUserVideoStream` class.
### Identifying generic control types
- [Control](./iouservideoclassid/control.md)
  The class identifier for the `IOUserVideoControl` class.
- [BooleanControl](./iouservideoclassid/booleancontrol.md)
  The class identifier for the `IOUserVideoBooleanControl` class.
- [LevelControl](./iouservideoclassid/levelcontrol.md)
  The class identifier for the `IOUserVideoLevelControl` class.
- [SliderControl](./iouservideoclassid/slidercontrol.md)
  The class identifier for the `IOUserVideoSliderControl` class.
- [SelectorControl](./iouservideoclassid/selectorcontrol.md)
  The class identifier for the `IOUserVideoSelectorControl` class.
### Identifying volume control types
- [VolumeControl](./iouservideoclassid/volumecontrol.md)
  The class identifier for the `IOUserVideoVolumeControl` class.
- [MuteControl](./iouservideoclassid/mutecontrol.md)
  The class identifier for the `IOUserVideoMuteControl` class.
- [LFEVolumeControl](./iouservideoclassid/lfevolumecontrol.md)
  A subclass of the `IOUserVideoLevelControl` class for an LFE channel that results from bass management.
- [LFEMuteControl](./iouservideoclassid/lfemutecontrol.md)
  A Boolean control where true means that mute is enabled, making that LFE element inaudible.
- [LineLevelControl](./iouservideoclassid/linelevelcontrol.md)
  A video selector control that identifies the nominal line level for the element.
### Identifying data control types
- [DataSourceControl](./iouservideoclassid/datasourcecontrol.md)
  A video selector control that identifies where the data for the element is coming from.
- [DataDestinationControl](./iouservideoclassid/datadestinationcontrol.md)
  A video selector control that identifies where the data for the element is going.
### Identifying miscellaneous control types
- [ClipLightControl](./iouservideoclassid/cliplightcontrol.md)
  A Boolean control where true means that the signal for the element has exceeded the sample range.
- [ClockSourceControl](./iouservideoclassid/clocksourcecontrol.md)
  A video selector control that identifies where the timing info for the object is coming from.
- [DirectionControl](./iouservideoclassid/directioncontrol.md)
  The class identifier for the `IOUserVideoDirectionControl` class.
- [HighPassFilterControl](./iouservideoclassid/highpassfiltercontrol.md)
  A video selector control that indicates the setting for the high pass filter on the given element.
- [JackControl](./iouservideoclassid/jackcontrol.md)
  A Boolean control where true means something is plugged into that element.
- [ListenbackControl](./iouservideoclassid/listenbackcontrol.md)
  An `IOUserVideoBooleanControl` where true means that the listenback channel is audible.
- [PhantomPowerControl](./iouservideoclassid/phantompowercontrol.md)
  A Boolean control where true means that the element’s hardware has phantom power enabled.
- [PhaseInvertControl](./iouservideoclassid/phaseinvertcontrol.md)
  A Boolean control where true means that the phase of the signal on the given element is being inverted by 180 degrees.
- [SoloControl](./iouservideoclassid/solocontrol.md)
  A Boolean control where true means that solo is enabled, making just that element audible and the other elements inaudible.
- [StereoPanControl](./iouservideoclassid/stereopancontrol.md)
  The class identifier for the `IOUserVideoStereoPanControl` class.
- [TalkbackControl](./iouservideoclassid/talkbackcontrol.md)
  A Boolean control where true means that the talkback channel is enabled.

## See Also

### Getting information about the class
- [GetClassID](../iouservideobooleancontrol/getclassid.md)
  Gets the class identifier of the object
- [GetBaseClassID](../iouservideobooleancontrol/getbaseclassid.md)
  Gets the class identifier of the base class object


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid)*