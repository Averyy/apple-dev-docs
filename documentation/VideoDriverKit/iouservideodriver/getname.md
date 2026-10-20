# GetName

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the name of the driver.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<OSString> GetName();
```

#### Return Value

The driver’s name.

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Getting information about the class
- [GetClassID](./getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](./getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](../videodriverkit-page/iouservideoclassid.md)
  Video class identifiers of an video object.
- [GetWorkQueue](./getworkqueue.md)
  Gets the work queue created by the video object.
- [SetName](./setname.md)
  Sets the name of the video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/getname)*