# extensionWithAppExtensionBundle:completionHandler:

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns a web extension initialized with a specified app extension bundle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```objc
+ (void) extensionWithAppExtensionBundle:(NSBundle *) appExtensionBundle completionHandler:(void (^)(WKWebExtension *extension, NSError *error)) completionHandler;
```

## Discussion

The app extension bundle must contain a `manifest.json` file in its resources directory. If the manifest is invalid or missing, or the bundle is otherwise improperly configured, an error will be returned.

## Parameters

- `appExtensionBundle`: The bundle to use for the new web extension.
- `completionHandler`: A block to be called with an initialized web extension, or `nil` if the object could not be initialized due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/extensionwithappextensionbundle:completionhandler:)*