# init(for:sizeInPoints:)

**Framework**: Virtualization  
**Kind**: init

Create a display configuration suitable for showing on the specified screen.

**Availability**:
- macOS 12.0+

## Declaration

```swift
convenience init(for screen: NSScreen, sizeInPoints: NSSize)
```

#### Discussion

The framework initializes the pixel dimensions and pixel density based on the specified screen and size. An instance of macOS running in the VM may not necessarily provide a display mode with a backing scale factor matching the specified screen.

## Parameters

- `screen`: The screen on which you intend to present the   for the display.
- `sizeInPoints`: The intended logical size of the display.

## See Also

- [init(widthInPixels: Int, heightInPixels: Int, pixelsPerInch: Int)](vzmacgraphicsdisplayconfiguration/init(widthinpixels:heightinpixels:pixelsperinch:).md)
  Create a display configuration with the specified pixel dimensions and pixel density.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdisplayconfiguration/init(for:sizeinpoints:))*