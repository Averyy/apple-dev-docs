# SoloControl

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A Boolean control where true means that solo is enabled, making just that element audible and the other elements inaudible.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
SoloControl
```

## See Also

### Identifying miscellaneous control types
- [ClipLightControl](./cliplightcontrol.md)
  A Boolean control where true means that the signal for the element has exceeded the sample range.
- [ClockSourceControl](./clocksourcecontrol.md)
  A video selector control that identifies where the timing info for the object is coming from.
- [DirectionControl](./directioncontrol.md)
  The class identifier for the `IOUserVideoDirectionControl` class.
- [HighPassFilterControl](./highpassfiltercontrol.md)
  A video selector control that indicates the setting for the high pass filter on the given element.
- [JackControl](./jackcontrol.md)
  A Boolean control where true means something is plugged into that element.
- [ListenbackControl](./listenbackcontrol.md)
  An `IOUserVideoBooleanControl` where true means that the listenback channel is audible.
- [PhantomPowerControl](./phantompowercontrol.md)
  A Boolean control where true means that the element’s hardware has phantom power enabled.
- [PhaseInvertControl](./phaseinvertcontrol.md)
  A Boolean control where true means that the phase of the signal on the given element is being inverted by 180 degrees.
- [StereoPanControl](./stereopancontrol.md)
  The class identifier for the `IOUserVideoStereoPanControl` class.
- [TalkbackControl](./talkbackcontrol.md)
  A Boolean control where true means that the talkback channel is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid/solocontrol)*