# LFEVolumeControl

**Framework**: VideoDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A subclass of the `IOUserVideoLevelControl` class for an LFE channel that results from bass management.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
LFEVolumeControl
```

## Discussion

If a driver represents LFE channels as normal audio channels, it must use [`VolumeControl`](./volumecontrol.md) to manipulate the level.

## See Also

### Identifying volume control types
- [VolumeControl](./volumecontrol.md)
  The class identifier for the `IOUserVideoVolumeControl` class.
- [MuteControl](./mutecontrol.md)
  The class identifier for the `IOUserVideoMuteControl` class.
- [LFEMuteControl](./lfemutecontrol.md)
  A Boolean control where true means that mute is enabled, making that LFE element inaudible.
- [LineLevelControl](./linelevelcontrol.md)
  A video selector control that identifies the nominal line level for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoclassid/lfevolumecontrol)*