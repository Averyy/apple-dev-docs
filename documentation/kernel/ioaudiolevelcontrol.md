# IOAudioLevelControl

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.1+

## Declaration

```cpp
class IOAudioLevelControl : IOAudioControl
```

## Topics

### Miscellaneous
- [create](./ioaudiolevelcontrol/api-1811861-create.md)
  Allocates a new level control with the given attributes
- [init](./ioaudiolevelcontrol/api-1811868-init.md)
  Initializes a newly allocated IOAudioLevelControl with the given attributes
- [setLinearScale](./ioaudiolevelcontrol/api-1811880-setlinearscale.md)
  This function tells CoreAudio if it should apply a curve to the scaler representation of the volume.
- [setMaxDB](./ioaudiolevelcontrol/api-1811889-setmaxdb.md)
  Sets the maximum value in db that the control may have
- [setMaxValue](./ioaudiolevelcontrol/api-1811896-setmaxvalue.md)
  Sets the maximum value the control may have
- [setMinDB](./ioaudiolevelcontrol/api-1811907-setmindb.md)
  Sets the minimum value in db that the control may have
- [setMinValue](./ioaudiolevelcontrol/api-1811910-setminvalue.md)
  Sets the minimum value the control may have
### Instance Methods
- [- addNegativeInfinity](./ioaudiolevelcontrol/api-1493460-addnegativeinfinity.md)
- [- addRange](./ioaudiolevelcontrol/api-1493455-addrange.md)
- [- free](./ioaudiolevelcontrol/api-1493472-free.md)
- [- getMaxDB](./ioaudiolevelcontrol/api-1493469-getmaxdb.md)
- [- getMaxValue](./ioaudiolevelcontrol/api-1493448-getmaxvalue.md)
- [- getMetaClass](./ioaudiolevelcontrol/api-1493452-getmetaclass.md)
- [- getMinDB](./ioaudiolevelcontrol/api-1493462-getmindb.md)
- [- getMinValue](./ioaudiolevelcontrol/api-1493454-getminvalue.md)
- [- init](./ioaudiolevelcontrol/api-1493466-init.md)
- [- setLinearScale](./ioaudiolevelcontrol/api-1493478-setlinearscale.md)
- [- setMaxDB](./ioaudiolevelcontrol/api-1493467-setmaxdb.md)
- [- setMaxValue](./ioaudiolevelcontrol/api-1493457-setmaxvalue.md)
- [- setMinDB](./ioaudiolevelcontrol/api-1493464-setmindb.md)
- [- setMinValue](./ioaudiolevelcontrol/api-1493474-setminvalue.md)
- [- validateValue](./ioaudiolevelcontrol/api-1493446-validatevalue.md)
### Type Methods
- [+ create](./ioaudiolevelcontrol/api-1493476-create.md)
- [+ createPassThruVolumeControl](./ioaudiolevelcontrol/api-1493450-createpassthruvolumecontrol.md)
- [+ createVolumeControl](./ioaudiolevelcontrol/api-1493470-createvolumecontrol.md)

## Relationships

### Inherits From
- [IOAudioControl](./ioaudiocontrol.md)

## See Also

### Interfaces
- [IOAudioSelectorControl](./ioaudioselectorcontrol.md)
- [IOAudioToggleControl](./ioaudiotogglecontrol.md)
- [IOAudioControl](./ioaudiocontrol.md)
  Represents any controllable attribute of an IOAudioDevice.
- [IOAudioEngine](./ioaudioengine.md)
  Abstract base class for a single audio audio / I/O engine.
- [IOAudioStream](./ioaudiostream.md)
  This class wraps a single sample buffer in an audio driver.
- [IOAudioPort](./ioaudioport.md)
  Represents a logical or physical port or functional unit in an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol)*