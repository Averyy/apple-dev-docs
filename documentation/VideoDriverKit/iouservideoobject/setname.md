# SetName

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetName(OSString *in_name);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the name of the IOUserVideoObject

If object can change the name dynamically, a notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_name`: OSString name to set.

## See Also

- [GetName](iouservideoobject/getname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/setname)*