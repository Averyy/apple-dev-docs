# IOVideoDevice

**Framework**: Kernel  
**Kind**: cl

A class that represents a video device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class IOVideoDevice : IOService
```

## Topics

### Miscellaneous
- [getStream](iovideodevice/1809409-getstream.md)
- [getStreamCount](iovideodevice/1809412-getstreamcount.md)
- [newUserClient](iovideodevice/1809416-newuserclient.md)
  See the documentation for the IOService method newUserClient.
- [setStreamMode](iovideodevice/1809422-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iovideodevice/1809424-startstream.md)
  Start sending data on a stream.
- [stopStream](iovideodevice/1809428-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iovideodevice/1809431-suspendstream.md)
  Temporarily suspend data flow on the stream.
### Instance Methods
- [- addStream](iovideodevice/1557550-addstream.md)
- [- closeStream](iovideodevice/1557546-closestream.md)
- [- free](iovideodevice/1557562-free.md)
- [- getMetaClass](iovideodevice/1557567-getmetaclass.md)
- [- getStream](iovideodevice/1557552-getstream.md)
- [- getStreamCount](iovideodevice/1557561-getstreamcount.md)
- [- init](iovideodevice/1557566-init.md)
- [- inputCallback](iovideodevice/1557563-inputcallback.md)
- [- inputSyncCallback](iovideodevice/1557560-inputsynccallback.md)
- [- newUserClient](iovideodevice/1557556-newuserclient.md)
- [- openStream](iovideodevice/1557557-openstream.md)
- [- registerNotificationPort](iovideodevice/1557553-registernotificationport.md)
- [- releaseStreams](iovideodevice/1557558-releasestreams.md)
- [- removeStream](iovideodevice/1557564-removestream.md)
- [- sendMultiNotification](iovideodevice/1557551-sendmultinotification.md)
- [- sendSingleNotification](iovideodevice/1557547-sendsinglenotification.md)
- [- setControlValue](iovideodevice/1557565-setcontrolvalue.md)
- [- setStreamFormat](iovideodevice/1557548-setstreamformat.md)
- [- setStreamMode](iovideodevice/1557559-setstreammode.md)
- [- startStream](iovideodevice/1557554-startstream.md)
- [- startStream](iovideodevice/3516812-startstream.md)
- [- stopStream](iovideodevice/1557555-stopstream.md)
- [- stopStream](iovideodevice/3516813-stopstream.md)
- [- suspendStream](iovideodevice/1557549-suspendstream.md)
- [- suspendStream](iovideodevice/3516814-suspendstream.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IONVRAMController](ionvramcontroller.md)
- [IOVideoControlDictionary](iovideocontroldictionary.md)
- [IOVideoStream](iovideostream.md)
  A class representing a stream of video data buffers passed from kernel to user space and back again.
- [IOVideoStreamDictionary](iovideostreamdictionary.md)
- [IOVideoStreamFormatDictionary](iovideostreamformatdictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevice)*