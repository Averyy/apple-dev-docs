# AddObject

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddObject(IOUserVideoObject *in_object);
```

#### Return Value

Returns kIOReturnSuccess if object was successfully added.

#### Discussion

Add a IOUserVideoObject to the driver

All objects that need to be managed by the host needs to be added to the driver. The objects’s reference count will be incremented if it was successfully added. Caller should also call PropertiesChanged() as necessary to notify host of any changes.

## Parameters

- `in_object`: IOUserVideoObject to be added to the driver.

## See Also

- [RemoveObject](iouservideodriver/removeobject.md)
- [IOUserVideoObject](iouservideoobject.md)
- [GetVideoObjectForObjectID](iouservideodriver/getvideoobjectforobjectid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/addobject)*