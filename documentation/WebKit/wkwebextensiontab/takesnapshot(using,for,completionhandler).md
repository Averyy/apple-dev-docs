# takeSnapshot(using:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to capture a snapshot of the current webpage as an image.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
optional func takeSnapshot(using configuration: WKSnapshotConfiguration, for context: WKWebExtensionContext, completionHandler: @escaping (UIImage?, (any Error)?) -> Void)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
optional func snapshot(using configuration: WKSnapshotConfiguration, for context: WKWebExtensionContext) async throws -> UIImage?
```

*macOS*

```swift
optional func takeSnapshot(using configuration: WKSnapshotConfiguration, for context: WKWebExtensionContext, completionHandler: @escaping (NSImage?, (any Error)?) -> Void)
```

*macOS*

```swift
optional func snapshot(using configuration: WKSnapshotConfiguration, for context: WKWebExtensionContext) async throws -> NSImage?
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (void) takeSnapshotUsingConfiguration:(WKSnapshotConfiguration *) configuration forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(UIImage *webpageImage, NSError *error)) completionHandler;
```

*macOS*

```objc
- (void) takeSnapshotUsingConfiguration:(WKSnapshotConfiguration *) configuration forWebExtensionContext:(WKWebExtensionContext *) context completionHandler:(void (^)(NSImage *webpageImage, NSError *error)) completionHandler;
```

## Discussion

Defaults to capturing the visible area of the tab’s web view if not implemented.

## Parameters

- `configuration`: An object that specifies how the snapshot is configured.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. The block takes two arguments: the captured image of the webpage (or `nil` if capturing failed) and an error, which should be provided if any errors occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/takesnapshot(using:for:completionhandler:))*