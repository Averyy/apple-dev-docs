# RemoveObject

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveObject(IOUserVideoObject *in_object);
```

#### Return Value

Returns kIOReturnSuccess if object was successfully removed.

#### Discussion

Remove a IOUserVideoObject from the driver

The objects’s reference count will be decremented if it was successfully removed. Caller should also call PropertiesChanged() as necessary to notify host of any changes.

## Parameters

- `in_object`: IOUserVideoObject to be removed from the driver.

## See Also

- [AddObject](iouservideodriver/addobject.md)
- [IOUserVideoObject](iouservideoobject.md)
- [GetVideoObjectForObjectID](iouservideodriver/getvideoobjectforobjectid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/removeobject)*