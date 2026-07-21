# IOUserVideoClassID

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoClassID : uint32_t;
```

#### Overview

IOUserVideoClassID’s are used to identify the class of an IOUserVideooObject.

The IOUserVideoClassID that identifies the IOUserVideoObject class.

The IOUserVideoClassID that identifies the IOUserVideoDriver class

The IOUserVideoClassID that identifies the IOUserVideoBox class

The IOUserVideoClassID that identifies the IOUserVideoClockDevice class

The IOUserVideoClassID that identifies the IOUserVideoDevice class

The IOUserVideoClassID that identifies the IOUserVideoStream class

The IOUserVideoClassID that identifies the IOUserVideoControl class

The IOUserVideoClassID that identifies the IOUserVideoSliderControl class

The IOUserVideoClassID that identifies the IOUserVideoLevelControl class

The IOUserVideoClassID that identifies the IOUserVideoVolumeControl class

A subclass of the IOUserVideoLevelControl class for an LFE channel that results from bass management. Note that LFE channels that are represented as normal audio channels must use IOUserVideoClassID VolumeControl to manipulate the level.

The IOUserVideoClassID that identifies the IOUserVideoBooleanControl class

A subclass of the IOUserVideoBooleanControl class where a true value means that solo is enabled making just that element audible and the other elements inaudible.

A subclass of the IOUserVideoBooleanControl class where a true value means something is plugged into that element.

A subclass of the IOUserVideoBooleanControl class where true means that mute is enabled making that LFE element inaudible. This control is for LFE channels that result from bass management. Note that LFE channels that are represented as normal audio channels must use an VideoMuteControl.

A subclass of the IOUserVideoBooleanControl class where true means that the element’s hardware has phantom power enabled.

A subclass of the IOUserVideoBooleanControl class where true means that the phase of the signal on the given element is being inverted by 180 degrees.

A subclass of the IOUserVideoBooleanControl class where true means that the signal for the element has exceeded the sample range. Once a clip light is turned on, it is to stay on until either the value of the control is set to false or the current IO session stops and a new IO session starts.

An IOUserVideoBooleanControl where true means that the talkback channel is enabled. This control is for talkback channels that are handled outside of the regular IO channels. If the talkback channel is among the normal IO channels, it will use IOUserVideoMuteControl.

An IOUserVideoBooleanControl where true means that the listenback channel is audible. This control is for listenback channels that are handled outside of the regular IO channels. If the listenback channel is among the normal IO channels, it will use IOUserVideoMuteControl.

The IOUserVideoClassID that identifies the IOUserVideoMuteControl class

The IOUserVideoClassID that identifies the IOUserVideoSelectorControl class

A subclass of the IOUserVideoSelectorControl class that identifies where the data for the element is coming from.

A subclass of the IOUserVideoSelectorControl class that identifies where the data for the element is going.

A subclass of the IOUserVideoSelectorControl class that identifies where the timing info for the object is coming from.

A subclass of the IOUserVideoSelectorControl class that identifies the nominal line level for the element. Note that this is not a gain stage but rather indicating the voltage standard (if any) used for the element, such as +4dBu, -10dBV, instrument, etc.

A subclass of the IOUserVideoSelectorControl class that indicates the setting for the high pass filter on the given element.

The IOUserVideoClassID that identifies the IOUserVideoStereoPanControl class

## Topics

### Identifying VideoDriverKit types
- [Object](videodriverkit/iouservideoclassid/object.md)
- [Driver](videodriverkit/iouservideoclassid/driver.md)
- [Box](videodriverkit/iouservideoclassid/box.md)
- [Clock](videodriverkit/iouservideoclassid/clock.md)
- [Buffer](videodriverkit/iouservideoclassid/buffer.md)
- [Device](videodriverkit/iouservideoclassid/device.md)
- [Stream](videodriverkit/iouservideoclassid/stream.md)
### Identifying generic control types
- [Control](videodriverkit/iouservideoclassid/control.md)
- [BooleanControl](videodriverkit/iouservideoclassid/booleancontrol.md)
- [LevelControl](videodriverkit/iouservideoclassid/levelcontrol.md)
- [SliderControl](videodriverkit/iouservideoclassid/slidercontrol.md)
- [SelectorControl](videodriverkit/iouservideoclassid/selectorcontrol.md)
### Identifying volume control types
- [VolumeControl](videodriverkit/iouservideoclassid/volumecontrol.md)
- [MuteControl](videodriverkit/iouservideoclassid/mutecontrol.md)
- [LFEVolumeControl](videodriverkit/iouservideoclassid/lfevolumecontrol.md)
- [LFEMuteControl](videodriverkit/iouservideoclassid/lfemutecontrol.md)
- [LineLevelControl](videodriverkit/iouservideoclassid/linelevelcontrol.md)
### Identifying data control types
- [DataSourceControl](videodriverkit/iouservideoclassid/datasourcecontrol.md)
- [DataDestinationControl](videodriverkit/iouservideoclassid/datadestinationcontrol.md)
### Identifying miscellaneous control types
- [ClipLightControl](videodriverkit/iouservideoclassid/cliplightcontrol.md)
- [ClockSourceControl](videodriverkit/iouservideoclassid/clocksourcecontrol.md)
- [DirectionControl](videodriverkit/iouservideoclassid/directioncontrol.md)
- [HighPassFilterControl](videodriverkit/iouservideoclassid/highpassfiltercontrol.md)
- [JackControl](videodriverkit/iouservideoclassid/jackcontrol.md)
- [ListenbackControl](videodriverkit/iouservideoclassid/listenbackcontrol.md)
- [PhantomPowerControl](videodriverkit/iouservideoclassid/phantompowercontrol.md)
- [PhaseInvertControl](videodriverkit/iouservideoclassid/phaseinvertcontrol.md)
- [SoloControl](videodriverkit/iouservideoclassid/solocontrol.md)
- [StereoPanControl](videodriverkit/iouservideoclassid/stereopancontrol.md)
- [TalkbackControl](videodriverkit/iouservideoclassid/talkbackcontrol.md)

## See Also

- [GetClassID](iouservideobooleancontrol/getclassid.md)
- [GetBaseClassID](iouservideobooleancontrol/getbaseclassid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid)*