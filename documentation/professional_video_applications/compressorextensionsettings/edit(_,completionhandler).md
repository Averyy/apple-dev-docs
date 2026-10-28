# edit(_:completionHandler:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Displays a view that enables users to edit the current encoder settings, and then calls a handler upon completion.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func edit(_ viewController: NSViewController!, completionHandler handler: ((NSApplication.ModalResponse) -> Void)!)
```

```swift
func edit(_ viewController: NSViewController!) async -> NSApplication.ModalResponse
```

```objc
- (void) editSettings:(NSViewController *) viewController completionHandler:(void (^)(NSModalResponse returnCode)) handler;
```

## Discussion

The Compressor app typically calls this method when a user tries to configure the encoder settings. The default `ProExtensionPrincipalViewController` object includes a view that you can use to present the current encoder settings in the Compressor app interface. Users can edit these settings from the UI to customize the encoded output. When they finish editing, if the extension calls the completion handler with the `NSModalResponseOK` return code, the Compressor app calls the [`settingsString()`](./settingsstring%28%29.md) method to get the updated settings from the extension. The Compressor app saves the current settings as XML and provides them back to the extension when the extension restarts or during the encoding process.

## Parameters

- `viewController`: The Compressor app view controller that hosts the encoder settings view.
- `handler`: A block that is called when the extension modal session ends. The block returns no value and takes the following parameter:

  - **`returnCode`**: The return code to send to the completion handler. Choose from one of the return codes defined in the [`NSApplication.ModalResponse`](../../AppKit/nsapplication/modalresponse.md) enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettings/edit(_:completionhandler:))*