# image

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

A representation of the screenshot as a platform-native image object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
@NSCopying
var image: UIImage { get }
```

*macOS*

```swift
@NSCopying
var image: NSImage { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (copy, readonly) UIImage * image;
```

*macOS*

```objc
@property (copy, readonly) NSImage * image;
```

## See Also

### Screenshot representations
- [var pngRepresentation: Data](./pngrepresentation.md)
  A representation of the screenshot as PNG image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreenshot/image)*