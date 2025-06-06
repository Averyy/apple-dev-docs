# saveMachineStateTo(url:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Saves the state of a VM.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func saveMachineStateTo(url saveFileURL: URL) async throws
```

#### Discussion

Use this method to save a paused VM to a file. You can use the contents of this file later to restore the state of the paused VM.

This call fails if the VM isn’t in a paused state or if the Virtualization framework can’t save the VM. If this method fails, the framework returns an error, and the VM state remains unchanged.

If this method is successful, the framework writes the file, and the VM state remains unchanged.

## Parameters

- `saveFileURL`: An   that indicates the location where the framework writes the saved state of the VM.
- `completionHandler`: The error parameter passed to the block is   if the save was successful.

## See Also

- [func restoreMachineStateFrom(url: URL, completionHandler: ((any Error)?) -> Void)](vzvirtualmachine/restoremachinestatefrom(url:completionhandler:).md)
  Restores a VM from a previously saved state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/savemachinestateto(url:completionhandler:))*