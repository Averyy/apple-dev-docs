# open(_:options:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Attempts to open the resource at the specified URL asynchronously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func open(_ url: URL, options: UIScene.OpenExternalURLOptions?, completionHandler completion: ((Bool) -> Void)? = nil)
```

```swift
func open(_ url: URL, options: UIScene.OpenExternalURLOptions?) async -> Bool
```

```objc
- (void) openURL:(NSURL *) url options:(UISceneOpenExternalURLOptions *) options completionHandler:(void (^)(BOOL success)) completion;
```

## Discussion

Use this method to open the specified resource. If the specified URL scheme is handled by another app, iOS launches that app and passes the URL to it. Launching the app brings the other app to the foreground.

## Parameters

- `url`: A URL (Universal Resource Locator). The resource identified by this URL may be local to the current app or handled by a different app. UIKit supports many common schemes, including the `http`, `https`, `tel`, `facetime`, and `mailto` schemes.
- `options`: The options to use when opening the URL.
- `completion`: The block to execute with the results. Provide a value for this parameter if you want to be informed of the success or failure of opening the URL. This block is executed asynchronously on your app’s main thread. The block has no return value and takes the following parameter:

  - **success**: A Boolean value indicating whether the system successfully opened the URL. If no app is capable of handling the specified URL, this parameter is [`false`](../../Swift/false.md).

## See Also

### Opening URLs
- [UIScene.OpenExternalURLOptions](./openexternalurloptions.md)
  Options you specify when asking a scene to open a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/open(_:options:completionhandler:))*