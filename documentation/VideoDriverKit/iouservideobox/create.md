# Create

**Framework**: VideoDriverKit  
**Kind**: method

Static factory method to allocate and initialize an IOUserVideoBox.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoBox> Create(IOUserVideoDriver *in_driver, bool in_is_acquirable, OSString *in_box_uid);
```

#### Return Value

OSSharedPtr to an IOUserVideoBox if it was successfully allocated and initialized

#### Discussion

If IOUserVideoBox is subclassed to override behavior, don’t use this method to allocate or initialize the custom subclass.

## Parameters

- `in_is_acquirable`: Bool value
- `in_box_uid`: An OSString pointer for the box unique identifier

## See Also

- [init](iouservideobox/init.md)
  Initializes a video box.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/create)*