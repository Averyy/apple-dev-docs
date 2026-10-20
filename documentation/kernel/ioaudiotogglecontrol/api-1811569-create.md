# create

**Framework**: Kernel  
**Kind**: instm

Allocates a new mute control with the given attributes

## Declaration

```c
static IOAudioToggleControl *create(
 bool initialValue, 
 UInt32 channelID, 
 const char *channelName = 0, 
 UInt32 cntrlID = 0, 
 UInt32 subType = 0, 
 UInt32 usage = 0);
```

#### Return Value

Returns a newly allocated and initialized mute IOAudioControl

## Parameters

- `initialValue`: The initial value of the control
- `channelID`: The ID of the channel(s) that the control acts on. Common IDs are located in IOAudioTypes.h.
- `channelName`: An optional name for the channel. Common names are located in IOAudioPort.h.
- `cntrlID`: An optional ID for the control that can be used to uniquely identify controls

## See Also

### Miscellaneous
- [createPassThruMuteControl](./api-1811586-createpassthrumutecontrol.md)
  Allocates a new pass through mute control with the given attributes
- [init](./api-1811599-init.md)
  Initializes a newly allocated IOAudioToggleControl with the given attributes


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiotogglecontrol/1811569-create)*