# displayDidBeginReconfiguration(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when the reconfiguration operation has begun.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func displayDidBeginReconfiguration(_ display: VZGraphicsDisplay)
```

```objc
- (void) displayDidBeginReconfiguration:(VZGraphicsDisplay *) display;
```

#### Discussion

The framework issued a configuration change, such as a resize, and you can expect new frames with a new size or configuration.

The framework invokes this method on the VM’s queue.

## Parameters

- `display`: The [`VZGraphicsDisplay`](../vzgraphicsdisplay.md) whose state is changing.

## See Also

### Reacting to changes in display configuration
- [func displayDidEndReconfiguration(VZGraphicsDisplay)](./displaydidendreconfiguration%28_%29.md)
  The method the framework calls when the reconfiguration operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplayobserver/displaydidbeginreconfiguration(_:))*