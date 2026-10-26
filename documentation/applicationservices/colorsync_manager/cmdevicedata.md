# CMDeviceData

**Framework**: Application Services  
**Kind**: tag

## Declaration

```c
struct CMDeviceData {
   UInt32 dataVersion;
   CMDeviceSpec deviceSpec;
   CMDeviceScope deviceScope;
   CMDeviceState deviceState;
   CMDeviceProfileID defaultProfileID;
   UInt32 profileCount;
   UInt32 reserved;
};
typedef struct CMDeviceData CMDeviceData;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmdevicedata)*