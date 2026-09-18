# GetName

**Framework**: VideoDriverKit  
**Kind**: method

Gets the name of the driver.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<OSString> GetName();
```

#### Return Value

The driver’s name.

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

- [GetClassID](iouservideodriver/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideodriver/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
- [GetWorkQueue](iouservideodriver/getworkqueue.md)
  Gets the work queue created by the video object.
- [SetName](iouservideodriver/setname.md)
  Sets the name of the video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/getname)*