# setMinDB

**Framework**: Kernel  
**Kind**: instm

Sets the minimum value in db that the control may have

## Declaration

```swift
virtual void setMinDB(
 IOFixedminDB);
```

#### Overview

This value is represented as an IOFixed value which is a fixed point number. The IOFixed type is a 16.16 fixed point value.

## Parameters

- `minDB`: The minimum value in db for the control

## See Also

- [create](ioaudiolevelcontrol/1811861-create.md)
  Allocates a new level control with the given attributes
- [init](ioaudiolevelcontrol/1811868-init.md)
  Initializes a newly allocated IOAudioLevelControl with the given attributes
- [setLinearScale](ioaudiolevelcontrol/1811880-setlinearscale.md)
  This function tells CoreAudio if it should apply a curve to the scaler representation of the volume.
- [setMaxDB](ioaudiolevelcontrol/1811889-setmaxdb.md)
  Sets the maximum value in db that the control may have
- [setMaxValue](ioaudiolevelcontrol/1811896-setmaxvalue.md)
  Sets the maximum value the control may have
- [setMinValue](ioaudiolevelcontrol/1811910-setminvalue.md)
  Sets the minimum value the control may have


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol/1811907-setmindb)*