# remoteWindow(of:reply:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests that the host application creates a window to display custom UI.

**Availability**:
- FxPlug 4.2.1+

## Declaration

```swift
func remoteWindow(of contentSize: CGSize, reply: ((NSView?, (any Error)?) -> Void)!)
```

```swift
func remoteWindow(of contentSize: CGSize) async throws -> NSView?
```

```objc
- (void) remoteWindowOfSize:(CGSize) contentSize reply:(void (^)(NSView * parentView, NSError * error)) reply;
```

#### Discussion

Call this method to request that the host creates a new window to display custom user-interface elements. The reply block returns the window for your custom view. If there are any problems creating the window, `parentView` is `nil` and `error` contains an [`NSError`](../../Foundation/nserror.md) that describes the problem.

Each plug-in instance is limited to a single window. If a user doesn’t close the window that contains the custom user-interface elements, subsequent calls to this method return the same parent view.

## Parameters

- `contentSize`: The desired size for the content rectangle of the window.
- `reply`: Called when the window has been created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxremotewindowapi/remotewindow(of:reply:))*