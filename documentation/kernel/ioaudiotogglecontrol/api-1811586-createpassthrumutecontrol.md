# createPassThruMuteControl

**Framework**: Kernel  
**Kind**: instm

Allocates a new pass through mute control with the given attributes

## Declaration

```swift
static IOAudioToggleControl *createPassThruMuteControl (
 boolinitialValue, 
 UInt32channelID, 
 const char *channelName, 
 UInt32cntrlID);
```

#### Return_value

Returns a newly allocated and initialized mute IOAudioControl

## Parameters

- `initialValue`: The initial value of the control
- `channelID`: The ID of the channel(s) that the control acts on. Common IDs are located in IOAudioTypes.h.
- `channelName`: An optional name for the channel. Common names are located in IOAudioPort.h.
- `cntrlID`: An optional ID for the control that can be used to uniquely identify controls

## See Also

- [create](ioaudiotogglecontrol/1811569-create.md)
  Allocates a new mute control with the given attributes
- [init](ioaudiotogglecontrol/1811599-init.md)
  Initializes a newly allocated IOAudioToggleControl with the given attributes


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiotogglecontrol/1811586-createpassthrumutecontrol)*