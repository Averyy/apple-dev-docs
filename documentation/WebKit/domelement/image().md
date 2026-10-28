# image()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns an image associated with the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func image() -> NSImage!
```

```objc
- (NSImage *) image;
```

## Discussion

Returns an `NSImage` for the receiver if it is a `DOMHTMLImageElement` object—a `DOMHTMLObjectElement` object with an image loaded or a `DOMHTMLInputElement` object of type image. Returns `nil` if there is an error loading the image or the element does not contain an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domelement/image())*