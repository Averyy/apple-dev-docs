# GetVideoObjectForObjectID

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IOUserVideoObject> GetVideoObjectForObjectID(IOUserVideoObjectID in_object_id);
```

#### Return Value

Returns OSSharedPtr to an IOUserVideoObject if in_object_id was found.

#### Discussion

Get a IOUserVideoObject OSSharedPtr that corresponds to a IOUserVideoObjectID

## Parameters

- `in_object_id`: IOUserVideoObjectID of an object that was previously added to the driver.

## See Also

- [AddObject](iouservideodriver/addobject.md)
- [RemoveObject](iouservideodriver/removeobject.md)
- [IOUserVideoObject](iouservideoobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/getvideoobjectforobjectid)*