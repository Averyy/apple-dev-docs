# name

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The name of a custom content world.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var name: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * name;
```

## Discussion

This property contains a valid string only for content worlds you retrieve using the [`world(name:)`](./world%28name%29.md) function. The value of this property is `nil` for the content worlds in the [`defaultClient`](./defaultclient.md) and [`page`](./page.md) properties.

## See Also

### Retrieving a Custom Content World
- [class func world(name: String) -> WKContentWorld](./world%28name%29.md)
  Returns the custom content world with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/name)*