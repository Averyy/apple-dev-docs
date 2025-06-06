# reconfigure(sizeInPixels:)

**Framework**: Virtualization  
**Kind**: method

Resize this display with the new dimensions you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func reconfigure(sizeInPixels: CGSize) throws
```

#### Discussion

If successful, the framework passes the new size to the guest but the guest may or may not respond to the new size. If the guest doesn’t use the new size, the Virtualization framework doesn’t return an error.

Resizing the display triggers a display state change that you can track by adopting the [`VZGraphicsDisplayObserver`](vzgraphicsdisplayobserver.md) protocol.

## Parameters

- `sizeInPixels`: The new display width and height in pixels.

## See Also

- [func reconfigure(configuration: VZGraphicsDisplayConfiguration) throws](vzgraphicsdisplay/reconfigure(configuration:).md)
  Reconfigure this display with the new display configuration you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay/reconfigure(sizeinpixels:))*