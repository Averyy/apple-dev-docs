# init(widthInPixels:heightInPixels:pixelsPerInch:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Create a display configuration with the specified pixel dimensions and pixel density.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(widthInPixels: Int, heightInPixels: Int, pixelsPerInch: Int)
```

```objc
- (instancetype) initWithWidthInPixels:(NSInteger) widthInPixels heightInPixels:(NSInteger) heightInPixels pixelsPerInch:(NSInteger) pixelsPerInch;
```

## Parameters

- `widthInPixels`: The width of the display, in pixels.
- `heightInPixels`: The height of the display, in pixels.
- `pixelsPerInch`: The pixel density as a number of pixels per inch.

## See Also

### Creating the display configuration
- [convenience init(for: NSScreen, sizeInPoints: NSSize)](./init%28for,sizeinpoints%29.md)
  Create a display configuration suitable for showing on the specified screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdisplayconfiguration/init(widthinpixels:heightinpixels:pixelsperinch:))*