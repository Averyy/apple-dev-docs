# setMaxDB

**Framework**: Kernel  
**Kind**: instm

Sets the maximum value in db that the control may have

## Declaration

```cpp
virtual void setMaxDB(
 IOFixedmaxDB);
```

## Overview

This value is represented as an IOFixed value which is a fixed point number. The IOFixed type is a 16.16 fixed point value.

## Parameters

- `maxDB`: The maximum value in db for the control

## See Also

### Miscellaneous
- [create](./api-1811861-create.md)
  Allocates a new level control with the given attributes
- [init](./api-1811868-init.md)
  Initializes a newly allocated IOAudioLevelControl with the given attributes
- [setLinearScale](./api-1811880-setlinearscale.md)
  This function tells CoreAudio if it should apply a curve to the scaler representation of the volume.
- [setMaxValue](./api-1811896-setmaxvalue.md)
  Sets the maximum value the control may have
- [setMinDB](./api-1811907-setmindb.md)
  Sets the minimum value in db that the control may have
- [setMinValue](./api-1811910-setminvalue.md)
  Sets the minimum value the control may have


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol/1811889-setmaxdb)*