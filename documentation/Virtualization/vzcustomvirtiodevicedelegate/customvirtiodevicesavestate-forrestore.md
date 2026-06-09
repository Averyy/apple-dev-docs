# customVirtioDeviceSaveState(forRestore:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when a device needs to save its state.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioDeviceSaveState(forRestore device: VZCustomVirtioDevice) -> Data?
```

#### Discussion

Return the state data to save in an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object. If there is no state to save, return an empty NSData object ([NSData data]).

If you return `nil` from this method, the save operation fails.

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicesavestate(forrestore:))*