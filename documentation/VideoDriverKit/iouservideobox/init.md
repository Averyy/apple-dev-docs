# init

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes a video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
virtual bool init(IOUserVideoDriver *in_driver, bool in_is_acquirable, OSString *in_box_uid);
```

#### Return Value

True on success.

#### Discussion

Always pass in the `IOUserVideoDriver` and arguments; calling `init()` always returns false.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_is_acquirable`: A Boolean value that indicates whether the video box is aquirable.
- `in_box_uid`: An OSString pointer for the box unique identifier

## See Also

### Creating a video box
- [Create](./create.md)
  Static factory method to allocate and initialize a user video box.
- [IOUserVideoDriver](../iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/init)*