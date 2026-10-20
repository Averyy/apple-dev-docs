# init(for:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Returns a web extension context initialized with a specified extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
init(for extension: WKWebExtension)
```

```objc
- (instancetype) initForExtension:(WKWebExtension *) extension;
```

#### Return Value

An initialized web extension context.

#### Discussion

This is a designated initializer.

## Parameters

- `extension`: The extension to use for the new web extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/init(for:))*