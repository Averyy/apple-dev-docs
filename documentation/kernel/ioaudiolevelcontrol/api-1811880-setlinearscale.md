# setLinearScale

**Framework**: Kernel  
**Kind**: instm

This function tells CoreAudio if it should apply a curve to the scaler representation of the volume.

## Declaration

```swift
virtual void setLinearScale(
 booluseLinearScale);
```

## Parameters

- `useLinearScale`: TRUE instructs CoreAudio to not apply a curve to the scaler representation of the volume, FALSE instructs CoreAudio to apply a curve, which is CoreAudio's default behavior.

## See Also

- [create](ioaudiolevelcontrol/1811861-create.md)
  Allocates a new level control with the given attributes
- [init](ioaudiolevelcontrol/1811868-init.md)
  Initializes a newly allocated IOAudioLevelControl with the given attributes
- [setMaxDB](ioaudiolevelcontrol/1811889-setmaxdb.md)
  Sets the maximum value in db that the control may have
- [setMaxValue](ioaudiolevelcontrol/1811896-setmaxvalue.md)
  Sets the maximum value the control may have
- [setMinDB](ioaudiolevelcontrol/1811907-setmindb.md)
  Sets the minimum value in db that the control may have
- [setMinValue](ioaudiolevelcontrol/1811910-setminvalue.md)
  Sets the minimum value the control may have


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol/1811880-setlinearscale)*