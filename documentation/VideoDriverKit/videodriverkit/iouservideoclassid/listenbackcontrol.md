# ListenbackControl

**Framework**: VideoDriverKit  
**Kind**: case

An `IOUserVideoBooleanControl` where true means that the listenback channel is audible.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
ListenbackControl
```

#### Discussion

This control is for listenback channels that are handled outside of the regular IO channels. If the listenback channel is among the normal IO channels, it will use `IOUserVideoMuteControl`.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid/listenbackcontrol)*