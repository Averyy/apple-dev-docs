# AddObject

**Framework**: VideoDriverKit  
**Kind**: method

Adds a video object to the driver.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t AddObject(IOUserVideoObject *in_object);
```

#### Return Value

`kIOReturnSuccess` if object was successfully added.

#### Discussion

All objects that need to be managed by the host needs to be added to the driver. The objects’s reference count will be incremented if it was successfully added. Caller should also call PropertiesChanged() as necessary to notify host of any changes.

## Parameters

- `in_object`: The video object being added to the driver.

## See Also

- [RemoveObject](iouservideodriver/removeobject.md)
  Removes a video object from the driver.
- [IOUserVideoObject](iouservideoobject.md)
  The base class for all video objects.
- [GetVideoObjectForObjectID](iouservideodriver/getvideoobjectforobjectid.md)
  Gets the video object that corresponds to a video object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/addobject)*