# LFEMuteControl

**Framework**: VideoDriverKit  
**Kind**: case

A Boolean control where true means that mute is enabled, making that LFE element inaudible.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
LFEMuteControl
```

#### Discussion

This control is for LFE channels that result from bass management. Note that LFE channels that are represented as normal audio channels must use an VideoMuteControl.

## See Also

- [VolumeControl](videodriverkit/iouservideoclassid/volumecontrol.md)
  The class identifier for the `IOUserVideoVolumeControl` class.
- [MuteControl](videodriverkit/iouservideoclassid/mutecontrol.md)
  The class identifier for the `IOUserVideoMuteControl` class.
- [LFEVolumeControl](videodriverkit/iouservideoclassid/lfevolumecontrol.md)
  A subclass of the `IOUserVideoLevelControl` class for an LFE channel that results from bass management.
- [LineLevelControl](videodriverkit/iouservideoclassid/linelevelcontrol.md)
  A video selector control that identifies the nominal line level for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid/lfemutecontrol)*