# world(name:)

**Framework**: WebKit  
**Kind**: method

Returns the custom content world with the specified name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func world(name: String) -> WKContentWorld
```

#### Return Value

The content world with the specified name.

#### Discussion

Use this method to create unique content worlds for your script code. For example, if you execute scripts from multiple JavaScript extensions, you might use this method to create a content world based on a unique string associated with that extension.

## Parameters

- `name`: The name of the content world you want. If no content world with that name exists, this method creates a new   object and returns it. The next time you request a content world with the same name, this method returns the object it previously created.

## See Also

- [var name: String?](wkcontentworld/name.md)
  The name of a custom content world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/world(name:))*