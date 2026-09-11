# LineLevelControl

**Framework**: VideoDriverKit  
**Kind**: case

A video selector control that identifies the nominal line level for the element.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
LineLevelControl
```

#### Discussion

Note that this is not a gain stage but rather indicating the voltage standard (if any) used for the element, such as +4dBu, -10dBV, or instrument.

## See Also

- [VolumeControl](videodriverkit/iouservideoclassid/volumecontrol.md)
  The class identifier for the `IOUserVideoVolumeControl` class.
- [MuteControl](videodriverkit/iouservideoclassid/mutecontrol.md)
  The class identifier for the `IOUserVideoMuteControl` class.
- [LFEVolumeControl](videodriverkit/iouservideoclassid/lfevolumecontrol.md)
  A subclass of the `IOUserVideoLevelControl` class for an LFE channel that results from bass management.
- [LFEMuteControl](videodriverkit/iouservideoclassid/lfemutecontrol.md)
  A Boolean control where true means that mute is enabled, making that LFE element inaudible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid/linelevelcontrol)*