# name

**Framework**: Webkit  
**Kind**: property

The name of a custom content world.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var name: String? { get }
```

#### Discussion

This property contains a valid string only for content worlds you retrieve using the [`world(name:)`](wkcontentworld/world(name:).md) function. The value of this property is `nil` for the content worlds in the [`defaultClient`](wkcontentworld/defaultclient.md) and [`page`](wkcontentworld/page.md) properties.

## See Also

- [class func world(name: String) -> WKContentWorld](wkcontentworld/world(name:).md)
  Returns the custom content world with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/name)*