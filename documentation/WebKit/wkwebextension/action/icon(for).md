# icon(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the action icon for the specified size.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func icon(for size: CGSize) -> UIImage?
```

*macOS*

```swift
func icon(for size: CGSize) -> NSImage?
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (UIImage *) iconForSize:(CGSize) size;
```

*macOS*

```objc
- (NSImage *) iconForSize:(CGSize) size;
```

#### Return Value

The action icon, or `nil` if the icon was unable to be loaded.

#### Discussion

This icon should represent the extension in action sheets or toolbars. The returned image will be the best match for the specified size that is available in the extension’s action icon set. If no matching icon is available, the method will fall back to the extension’s icon.

## Parameters

- `size`: The size to use when looking up the action icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/icon(for:))*