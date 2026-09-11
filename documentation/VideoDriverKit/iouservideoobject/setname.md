# SetName

**Framework**: VideoDriverKit  
**Kind**: method

Sets the name of the video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetName(OSString *in_name);
```

#### Discussion

If the object can change the name dynamically, the object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## Parameters

- `in_name`: OSString name to set.

## See Also

- [GetName](iouservideoobject/getname.md)
  Gets the name of the video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/setname)*