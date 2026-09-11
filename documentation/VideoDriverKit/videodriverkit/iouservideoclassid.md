# IOUserVideoClassID

**Framework**: VideoDriverKit  
**Kind**: enum

Video class identifiers of an video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
enum IOUserVideoClassID : uint32_t;
```

## Topics

### Identifying VideoDriverKit types
- [Object](videodriverkit/iouservideoclassid/object.md)
  The class identifier for the `IOUserVideoObject` class.
- [Driver](videodriverkit/iouservideoclassid/driver.md)
  The class identifier for the `IOUserVideoDriver` class.
- [Box](videodriverkit/iouservideoclassid/box.md)
  The class identifier for the `IOUserVideoBox` class.
- [Clock](videodriverkit/iouservideoclassid/clock.md)
  The class identifier for the `IOUserVideoClockDevice` class.
- [Buffer](videodriverkit/iouservideoclassid/buffer.md)
  The class identifier for the `IOUserVideoBuffer` class.
- [Device](videodriverkit/iouservideoclassid/device.md)
  The class identifier for the `IOUserVideoDevice` class.
- [Stream](videodriverkit/iouservideoclassid/stream.md)
  The class identifier for the `IOUserVideoStream` class.
### Identifying generic control types
- [Control](videodriverkit/iouservideoclassid/control.md)
  The class identifier for the `IOUserVideoControl` class.
- [BooleanControl](videodriverkit/iouservideoclassid/booleancontrol.md)
  The class identifier for the `IOUserVideoBooleanControl` class.
- [LevelControl](videodriverkit/iouservideoclassid/levelcontrol.md)
  The class identifier for the `IOUserVideoLevelControl` class.
- [SliderControl](videodriverkit/iouservideoclassid/slidercontrol.md)
  The class identifier for the `IOUserVideoSliderControl` class.
- [SelectorControl](videodriverkit/iouservideoclassid/selectorcontrol.md)
  The class identifier for the `IOUserVideoSelectorControl` class.
### Identifying volume control types
- [VolumeControl](videodriverkit/iouservideoclassid/volumecontrol.md)
  The class identifier for the `IOUserVideoVolumeControl` class.
- [MuteControl](videodriverkit/iouservideoclassid/mutecontrol.md)
  The class identifier for the `IOUserVideoMuteControl` class.
- [LFEVolumeControl](videodriverkit/iouservideoclassid/lfevolumecontrol.md)
  A subclass of the `IOUserVideoLevelControl` class for an LFE channel that results from bass management.
- [LFEMuteControl](videodriverkit/iouservideoclassid/lfemutecontrol.md)
  A Boolean control where true means that mute is enabled, making that LFE element inaudible.
- [LineLevelControl](videodriverkit/iouservideoclassid/linelevelcontrol.md)
  A video selector control that identifies the nominal line level for the element.
### Identifying data control types
- [DataSourceControl](videodriverkit/iouservideoclassid/datasourcecontrol.md)
  A video selector control that identifies where the data for the element is coming from.
- [DataDestinationControl](videodriverkit/iouservideoclassid/datadestinationcontrol.md)
  A video selector control that identifies where the data for the element is going.
### Identifying miscellaneous control types
- [ClipLightControl](videodriverkit/iouservideoclassid/cliplightcontrol.md)
  A Boolean control where true means that the signal for the element has exceeded the sample range.
- [ClockSourceControl](videodriverkit/iouservideoclassid/clocksourcecontrol.md)
  A video selector control that identifies where the timing info for the object is coming from.
- [DirectionControl](videodriverkit/iouservideoclassid/directioncontrol.md)
  The class identifier for the `IOUserVideoDirectionControl` class.
- [HighPassFilterControl](videodriverkit/iouservideoclassid/highpassfiltercontrol.md)
  A video selector control that indicates the setting for the high pass filter on the given element.
- [JackControl](videodriverkit/iouservideoclassid/jackcontrol.md)
  A Boolean control where true means something is plugged into that element.
- [ListenbackControl](videodriverkit/iouservideoclassid/listenbackcontrol.md)
  An `IOUserVideoBooleanControl` where true means that the listenback channel is audible.
- [PhantomPowerControl](videodriverkit/iouservideoclassid/phantompowercontrol.md)
  A Boolean control where true means that the element’s hardware has phantom power enabled.
- [PhaseInvertControl](videodriverkit/iouservideoclassid/phaseinvertcontrol.md)
  A Boolean control where true means that the phase of the signal on the given element is being inverted by 180 degrees.
- [SoloControl](videodriverkit/iouservideoclassid/solocontrol.md)
  A Boolean control where true means that solo is enabled, making just that element audible and the other elements inaudible.
- [StereoPanControl](videodriverkit/iouservideoclassid/stereopancontrol.md)
  The class identifier for the `IOUserVideoStereoPanControl` class.
- [TalkbackControl](videodriverkit/iouservideoclassid/talkbackcontrol.md)
  A Boolean control where true means that the talkback channel is enabled.

## See Also

- [GetClassID](iouservideobooleancontrol/getclassid.md)
  Gets the class identifier of the object
- [GetBaseClassID](iouservideobooleancontrol/getbaseclassid.md)
  Gets the class identifier of the base class object


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid)*