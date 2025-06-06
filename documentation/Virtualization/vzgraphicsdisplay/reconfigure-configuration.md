# reconfigure(configuration:)

**Framework**: Virtualization  
**Kind**: method

Reconfigure this display with the new display configuration you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func reconfigure(configuration: VZGraphicsDisplayConfiguration) throws
```

#### Discussion

> ❗ **Important**:  The type of configuration you pass to this method needs to match the corresponding type that you used to create this display.

 The type of configuration you pass to this method needs to match the corresponding type that you used to create this display.

If successful, the framework passes the new configuration to the guest, but the guest may or may not respond to parts of the configuration. If the guest doesn’t use the new configuration, the Virtualization framework doesn’t return an error.

Reconfiguration of the display triggers a display state change that you can track by adopting the [`VZGraphicsDisplayObserver`](vzgraphicsdisplayobserver.md) protocol.

## Parameters

- `configuration`: The new   configuration.

## See Also

- [func reconfigure(sizeInPixels: CGSize) throws](vzgraphicsdisplay/reconfigure(sizeinpixels:).md)
  Resize this display with the new dimensions you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay/reconfigure(configuration:))*