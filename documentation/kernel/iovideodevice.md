# IOVideoDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

A class that represents a video device.

**Availability**:
- macOS 10.7+

## Declaration

```cpp
class IOVideoDevice : IOService
```

## Topics

### Miscellaneous
- [getStream](./iovideodevice/api-1809409-getstream.md)
- [getStreamCount](./iovideodevice/api-1809412-getstreamcount.md)
- [newUserClient](./iovideodevice/api-1809416-newuserclient.md)
  See the documentation for the IOService method newUserClient.
- [setStreamMode](./iovideodevice/api-1809422-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./iovideodevice/api-1809424-startstream.md)
  Start sending data on a stream.
- [stopStream](./iovideodevice/api-1809428-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](./iovideodevice/api-1809431-suspendstream.md)
  Temporarily suspend data flow on the stream.
### Instance Methods
- [- addStream](./iovideodevice/api-1557550-addstream.md)
- [- closeStream](./iovideodevice/api-1557546-closestream.md)
- [- free](./iovideodevice/api-1557562-free.md)
- [- getMetaClass](./iovideodevice/api-1557567-getmetaclass.md)
- [- getStream](./iovideodevice/api-1557552-getstream.md)
- [- getStreamCount](./iovideodevice/api-1557561-getstreamcount.md)
- [- init](./iovideodevice/api-1557566-init.md)
- [- inputCallback](./iovideodevice/api-1557563-inputcallback.md)
- [- inputSyncCallback](./iovideodevice/api-1557560-inputsynccallback.md)
- [- newUserClient](./iovideodevice/api-1557556-newuserclient.md)
- [- openStream](./iovideodevice/api-1557557-openstream.md)
- [- registerNotificationPort](./iovideodevice/api-1557553-registernotificationport.md)
- [- releaseStreams](./iovideodevice/api-1557558-releasestreams.md)
- [- removeStream](./iovideodevice/api-1557564-removestream.md)
- [- sendMultiNotification](./iovideodevice/api-1557551-sendmultinotification.md)
- [- sendSingleNotification](./iovideodevice/api-1557547-sendsinglenotification.md)
- [- setControlValue](./iovideodevice/api-1557565-setcontrolvalue.md)
- [- setStreamFormat](./iovideodevice/api-1557548-setstreamformat.md)
- [- setStreamMode](./iovideodevice/api-1557559-setstreammode.md)
- [- startStream](./iovideodevice/api-1557554-startstream.md)
- [- startStream](./iovideodevice/api-3516812-startstream.md)
- [- stopStream](./iovideodevice/api-1557555-stopstream.md)
- [- stopStream](./iovideodevice/api-3516813-stopstream.md)
- [- suspendStream](./iovideodevice/api-1557549-suspendstream.md)
- [- suspendStream](./iovideodevice/api-3516814-suspendstream.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Video
- [IONVRAMController](./ionvramcontroller.md)
- [IOVideoControlDictionary](./iovideocontroldictionary.md)
- [IOVideoStream](./iovideostream.md)
  A class representing a stream of video data buffers passed from kernel to user space and back again.
- [IOVideoStreamDictionary](./iovideostreamdictionary.md)
- [IOVideoStreamFormatDictionary](./iovideostreamformatdictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevice)*