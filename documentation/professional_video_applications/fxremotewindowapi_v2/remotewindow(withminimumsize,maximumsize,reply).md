# remoteWindow(withMinimumSize:maximumSize:reply:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests the host application to create a window with a minimum and maximum size that displays a custom UI.

**Availability**:
- FxPlug 4.2.3+

## Declaration

```swift
func remoteWindow(withMinimumSize minContentSize: CGSize, maximumSize maxContentSize: CGSize, reply: ((NSView?, (any Error)?) -> Void)!)
```

```swift
func remoteWindow(withMinimumSize minContentSize: CGSize, maximumSize maxContentSize: CGSize) async throws -> NSView?
```

```objc
- (void) remoteWindowWithMinimumSize:(CGSize) minContentSize maximumSize:(CGSize) maxContentSize reply:(void (^)(NSView * parentView, NSError * error)) reply;
```

## Discussion

Call this method to request that the host creates a new window where your plug-in displays custom-user interface elements. The maximum window size is limited to 80% of the host application’s main window size. The reply block returns the window for your custom view.

If there are any problems creating the window, `parentView` is `nil` and `error` contains an NSError that describes the problem.

> **Note**: Each plug-in instance is limited to a single window. If a user doesn’t close the window that contains the custom-user interface elements, subsequent calls to this method return the same parent view.

## Parameters

- `minContentSize`: The minimum content size for the requested window.
- `maxContentSize`: The maximum content size for the requested window.
- `reply`: Called when the window is created or if an error occurs during window creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxremotewindowapi_v2/remotewindow(withminimumsize:maximumsize:reply:))*