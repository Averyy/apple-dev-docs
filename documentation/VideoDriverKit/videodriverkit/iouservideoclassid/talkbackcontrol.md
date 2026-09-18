# TalkbackControl

**Framework**: VideoDriverKit  
**Kind**: case

A Boolean control where true means that the talkback channel is enabled.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
TalkbackControl
```

#### Discussion

This control is for talkback channels that are handled outside of the regular IO channels. If the talkback channel is among the normal IO channels, it will use IOUserVideoMuteControl.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid/talkbackcontrol)*