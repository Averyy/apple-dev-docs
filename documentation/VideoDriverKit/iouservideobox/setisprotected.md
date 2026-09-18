# SetIsProtected

**Framework**: VideoDriverKit  
**Kind**: method

Sets the value indicating the box’s protection state.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIsProtected(bool in_is_protected);
```

#### Discussion

The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## Parameters

- `in_is_protected`: The box’s protection state.

## See Also

- [IsProtected](iouservideobox/isprotected.md)
  A Boolean value indicating if box is protected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/setisprotected)*