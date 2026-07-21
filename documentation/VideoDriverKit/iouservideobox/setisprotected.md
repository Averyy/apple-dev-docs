# SetIsProtected

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIsProtected(bool in_is_protected);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the value indicating the box’s protection state

A notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_is_protected`: Bool value for the box’s protection state

## See Also

- [IsProtected](iouservideobox/isprotected.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setisprotected)*