# RemoveObject

**Framework**: VideoDriverKit  
**Kind**: method

Removes a video object from the driver.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveObject(IOUserVideoObject *in_object);
```

#### Return Value

`kIOReturnSuccess` if object was successfully removed.

#### Discussion

The objects’s reference count will be decremented if it was successfully removed. Caller should also call PropertiesChanged() as necessary to notify host of any changes.

## Parameters

- `in_object`: IOUserVideoObject to be removed from the driver.

## See Also

- [AddObject](iouservideodriver/addobject.md)
  Adds a video object to the driver.
- [IOUserVideoObject](iouservideoobject.md)
  The base class for all video objects.
- [GetVideoObjectForObjectID](iouservideodriver/getvideoobjectforobjectid.md)
  Gets the video object that corresponds to a video object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/removeobject)*