# displayDidEndReconfiguration(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when the reconfiguration operation ends.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func displayDidEndReconfiguration(_ display: VZGraphicsDisplay)
```

```objc
- (void) displayDidEndReconfiguration:(VZGraphicsDisplay *) display;
```

## Discussion

Frame updates have arrived at the most recently requested display size and configuration.

The framework invokes this method on the VM’s queue.

## Parameters

- `display`: The [`VZGraphicsDisplay`](../vzgraphicsdisplay.md) whose state is changing.

## See Also

### Reacting to changes in display configuration
- [func displayDidBeginReconfiguration(VZGraphicsDisplay)](./displaydidbeginreconfiguration%28_%29.md)
  The method the framework calls when the reconfiguration operation has begun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplayobserver/displaydidendreconfiguration(_:))*