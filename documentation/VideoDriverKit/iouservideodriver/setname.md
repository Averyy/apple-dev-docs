# SetName

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the name of the video driver.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetName(OSString *in_name);
```

#### Return Value

A kern_return_t value indicating success or failure.

#### Discussion

If the object can change the name dynamically, the object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to this value.

## Parameters

- `in_name`: An OSString name to set.

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
- [GetName](./getname.md)
  Gets the name of the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/setname)*