# create

**Framework**: Kernel  
**Kind**: instm

Allocates a new level control with the given attributes

## Declaration

```swift
static IOAudioLevelControl *create(
 SInt32 initialValue, 
 SInt32 minValue, 
 SInt32 maxValue, 
 IOFixed minDB, 
 IOFixed maxDB, 
 UInt32 channelID, 
 const char *channelName = 0, 
 UInt32 cntrlID = 0, 
 UInt32 subType = 0, 
 UInt32 usage = 0);
```

#### Return_value

Returns a newly allocted and initialized level IOAudioControl

## Parameters

- `initialValue`: The initial value of the control
- `minValue`: The lowest possible value the control may have
- `maxValue`: The highest possible value the control may have
- `minDB`: A fixed point representation of the db value matching minValue
- `maxDB`: A fixed point representation of the db value matching maxValue
- `channelID`: The ID of the channel(s) that the control acts on. Common IDs are located in IOAudioTypes.h.
- `channelName`: An optional name for the channel. Common names are located in IOAudioTypes.h.
- `cntrlID`: An optional ID for the control that can be used to uniquely identify controls.

## See Also

- [init](ioaudiolevelcontrol/1811868-init.md)
  Initializes a newly allocated IOAudioLevelControl with the given attributes
- [setLinearScale](ioaudiolevelcontrol/1811880-setlinearscale.md)
  This function tells CoreAudio if it should apply a curve to the scaler representation of the volume.
- [setMaxDB](ioaudiolevelcontrol/1811889-setmaxdb.md)
  Sets the maximum value in db that the control may have
- [setMaxValue](ioaudiolevelcontrol/1811896-setmaxvalue.md)
  Sets the maximum value the control may have
- [setMinDB](ioaudiolevelcontrol/1811907-setmindb.md)
  Sets the minimum value in db that the control may have
- [setMinValue](ioaudiolevelcontrol/1811910-setminvalue.md)
  Sets the minimum value the control may have


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol/1811861-create)*