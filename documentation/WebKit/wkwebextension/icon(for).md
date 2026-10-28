# icon(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the extension’s icon image for the specified size.

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

## Return Value

The extension’s icon image, or `nil` if the icon was unable to be loaded.

## Discussion

This icon should represent the extension in settings or other areas that show the extension. The returned image will be the best match for the specified size that is available in the extension’s icon set. If no matching icon can be found, the method will return `nil`.

## Parameters

- `size`: The size to use when looking up the icon.

## See Also

### Related Documentation
- [func actionIcon(for: CGSize) -> UIImage?](./actionicon%28for%29.md)
  Returns the default action icon for the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/icon(for:))*