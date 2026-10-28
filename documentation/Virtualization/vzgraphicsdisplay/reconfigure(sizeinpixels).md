# reconfigure(sizeInPixels:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Resize this display with the new dimensions you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func reconfigure(sizeInPixels: CGSize) throws
```

```objc
- (BOOL) reconfigureWithSizeInPixels:(CGSize) sizeInPixels error:(NSError **) error;
```

## Discussion

If successful, the framework passes the new size to the guest but the guest may or may not respond to the new size. If the guest doesn’t use the new size, the Virtualization framework doesn’t return an error.

Resizing the display triggers a display state change that you can track by adopting the [`VZGraphicsDisplayObserver`](../vzgraphicsdisplayobserver.md) protocol.

## Parameters

- `sizeInPixels`: The new display width and height in pixels.

## See Also

### Changing the display configuration
- [func reconfigure(configuration: VZGraphicsDisplayConfiguration) throws](./reconfigure%28configuration%29.md)
  Reconfigure this display with the new display configuration you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay/reconfigure(sizeinpixels:))*