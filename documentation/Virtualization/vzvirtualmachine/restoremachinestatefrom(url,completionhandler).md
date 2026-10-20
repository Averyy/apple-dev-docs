# restoreMachineStateFrom(url:completionHandler:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Restores a VM from a previously saved state.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func restoreMachineStateFrom(url saveFileURL: URL, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
func restoreMachineStateFrom(url saveFileURL: URL) async throws
```

```objc
- (void) restoreMachineStateFromURL:(NSURL *) saveFileURL completionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

#### Discussion

Use this method to restore a stopped VM to a state previously saved to file through [`saveMachineStateTo(url:completionHandler:)`](./savemachinestateto%28url,completionhandler%29.md).

The method fails if any of the following conditions are true:

- The Virtualization framework can’t open or read the file.
- The file contents are incompatible with the current configuration.
- The VM you’re trying to restore isn’t in the [`VZVirtualMachine.State.stopped`](./state-swift.enum/stopped.md) state.

If this method fails, the framework returns an error, and the VM state doesn’t change.

If this method is successful, the framework restores the VM and places it in the paused state.

## Parameters

- `saveFileURL`: An [`NSURL`](../../Foundation/nsurl.md) that indicates the location where the framework reads the saved state of the VM.
- `completionHandler`: A block the framework calls after the VM has been successfully restored or upon an error.

## See Also

### Saving and restoring the VM state
- [func saveMachineStateTo(url: URL, completionHandler: ((any Error)?) -> Void)](./savemachinestateto%28url,completionhandler%29.md)
  Saves the state of a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/restoremachinestatefrom(url:completionhandler:))*