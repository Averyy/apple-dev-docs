# IOAudioToggleControl

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.1+

## Declaration

```cpp
class IOAudioToggleControl : IOAudioControl
```

## Topics

### Miscellaneous
- [create](./ioaudiotogglecontrol/api-1811569-create.md)
  Allocates a new mute control with the given attributes
- [createPassThruMuteControl](./ioaudiotogglecontrol/api-1811586-createpassthrumutecontrol.md)
  Allocates a new pass through mute control with the given attributes
- [init](./ioaudiotogglecontrol/api-1811599-init.md)
  Initializes a newly allocated IOAudioToggleControl with the given attributes
### Instance Methods
- [- getMetaClass](./ioaudiotogglecontrol/api-1416489-getmetaclass.md)
- [- init](./ioaudiotogglecontrol/api-1416491-init.md)
### Type Methods
- [+ create](./ioaudiotogglecontrol/api-1416495-create.md)
- [+ createMuteControl](./ioaudiotogglecontrol/api-1416498-createmutecontrol.md)
- [+ createPassThruMuteControl](./ioaudiotogglecontrol/api-1416493-createpassthrumutecontrol.md)

## Relationships

### Inherits From
- [IOAudioControl](./ioaudiocontrol.md)

## See Also

### Interfaces
- [IOAudioLevelControl](./ioaudiolevelcontrol.md)
- [IOAudioSelectorControl](./ioaudioselectorcontrol.md)
- [IOAudioControl](./ioaudiocontrol.md)
  Represents any controllable attribute of an IOAudioDevice.
- [IOAudioEngine](./ioaudioengine.md)
  Abstract base class for a single audio audio / I/O engine.
- [IOAudioStream](./ioaudiostream.md)
  This class wraps a single sample buffer in an audio driver.
- [IOAudioPort](./ioaudioport.md)
  Represents a logical or physical port or functional unit in an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiotogglecontrol)*