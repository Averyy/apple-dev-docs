# extensionWithResourceBaseURL:completionHandler:

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns a web extension initialized with a specified resource base URL, which can point to either a directory or a ZIP archive.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```objc
+ (void) extensionWithResourceBaseURL:(NSURL *) resourceBaseURL completionHandler:(void (^)(WKWebExtension *extension, NSError *error)) completionHandler;
```

## Discussion

The URL must be a file URL that points to either a directory with a `manifest.json` file or a ZIP archive containing a `manifest.json` file. If the manifest is invalid or missing, or the URL points to an unsupported format or invalid archive, an error will be returned.

## Parameters

- `resourceBaseURL`: The file URL to use for the new web extension.
- `completionHandler`: A block to be called with an initialized web extension, or `nil` if the object could not be initialized due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/extensionwithresourcebaseurl:completionhandler:)*