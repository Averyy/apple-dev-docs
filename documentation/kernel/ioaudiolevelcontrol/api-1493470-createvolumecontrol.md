# createVolumeControl

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 10.4+ - Deprecated in 10.10

## Declaration

```c
static IOAudioLevelControl * createVolumeControl(SInt32 initialValue, SInt32 minValue, SInt32 maxValue, IOFixed minDB, IOFixed maxDB, UInt32 channelID, const char *channelName, UInt32 cntrlID, UInt32 usage);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol/1493470-createvolumecontrol)*