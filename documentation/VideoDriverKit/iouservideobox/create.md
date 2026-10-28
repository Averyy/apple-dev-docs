# Create

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Static Method

Static factory method to allocate and initialize a user video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
static OSSharedPtr<IOUserVideoBox> Create(IOUserVideoDriver *in_driver, bool in_is_acquirable, OSString *in_box_uid);
```

## Return Value

A user video box if it was successfully allocated and initialized.

## Discussion

If `IOUserVideoBox` is subclassed to override behavior, don’t use this method to allocate or initialize the custom subclass.

## Parameters

- `in_driver`: The video driver that owns this object.
- `in_is_acquirable`: A Boolean value that indicates whether the video box is aquirable.
- `in_box_uid`: The box unique identifier.

## See Also

### Creating a video box
- [init](./init.md)
  Initializes a video box.
- [IOUserVideoDriver](../iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/create)*