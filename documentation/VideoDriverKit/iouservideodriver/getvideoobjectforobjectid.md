# GetVideoObjectForObjectID

**Framework**: VideoDriverKit  
**Kind**: method

Gets the video object that corresponds to a video object identifier.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IOUserVideoObject> GetVideoObjectForObjectID(IOUserVideoObjectID in_object_id);
```

#### Return Value

OSSharedPtr to an IOUserVideoObject if in_object_id was found.

## Parameters

- `in_object_id`: IOUserVideoObjectID of an object that was previously added to the driver.

## See Also

- [AddObject](iouservideodriver/addobject.md)
  Adds a video object to the driver.
- [RemoveObject](iouservideodriver/removeobject.md)
  Removes a video object from the driver.
- [IOUserVideoObject](iouservideoobject.md)
  The base class for all video objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/getvideoobjectforobjectid)*