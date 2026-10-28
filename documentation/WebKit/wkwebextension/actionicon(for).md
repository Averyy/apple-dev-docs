# actionIcon(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the default action icon for the specified size.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func actionIcon(for size: CGSize) -> UIImage?
```

*macOS*

```swift
func actionIcon(for size: CGSize) -> NSImage?
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (UIImage *) actionIconForSize:(CGSize) size;
```

*macOS*

```objc
- (NSImage *) actionIconForSize:(CGSize) size;
```

## Return Value

The action icon, or `nil` if the icon was unable to be loaded.

## Discussion

This icon serves as a default and should be used to represent the extension in contexts like action sheets or toolbars prior to the extension being loaded into an extension context. Once the extension is loaded, use the [`action(for:)`](../wkwebextensioncontext/action%28for%29.md) API to get the tab-specific icon.

The returned image will be the best match for the specified size that is available in the extension’s action icon set. If no matching icon is available, the method will fall back to the extension’s icon.

## Parameters

- `size`: The size to use when looking up the action icon.

## See Also

### Related Documentation
- [func icon(for: CGSize) -> UIImage?](./icon%28for%29.md)
  Returns the extension’s icon image for the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/actionicon(for:))*