# customVirtioDeviceShouldRestore(_:saveState:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when a device restores its state.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func customVirtioDeviceShouldRestore(_ device: VZCustomVirtioDevice, saveState: Data) -> Bool
```

```objc
- (BOOL) customVirtioDeviceShouldRestore:(VZCustomVirtioDevice *) device saveState:(NSData *) saveState;
```

## Discussion

This method should return `NO` if restore operation failed.

## Parameters

- `device`: The device invoking the delegate method.
- `saveState`: The data that the delegate returned from [`customVirtioDeviceSaveState(forRestore:)`](./customvirtiodevicesavestate%28forrestore%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodeviceshouldrestore(_:savestate:))*