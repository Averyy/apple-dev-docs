# displayDidEndReconfiguration(_:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when the reconfiguration operation ends.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func displayDidEndReconfiguration(_ display: VZGraphicsDisplay)
```

#### Discussion

Frame updates have arrived at the most recently requested display size and configuration.

The framework invokes this method on the VM’s queue.

## Parameters

- `display`: The   whose state is changing.

## See Also

- [func displayDidBeginReconfiguration(VZGraphicsDisplay)](vzgraphicsdisplayobserver/displaydidbeginreconfiguration(_:).md)
  The method the framework calls when the reconfiguration operation has begun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplayobserver/displaydidendreconfiguration(_:))*